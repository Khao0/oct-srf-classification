
import os
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import cv2

CLASS_NAMES = ["CSC", "Normal", "PCV", "VKH"]
SCAN_TYPES = {
    "radial":12,
    "raster":25
}

sla_model = None
tsa_fe_model = None
tsa_lstm_model = None


def load_model():
    global sla_model
    global tsa_fe_model
    global tsa_lstm_model
    if os.path.exists("models/sla.h5"):
        sla_model = tf.keras.models.load_model("models/sla.h5")
        sla_model.trainable = False
    else :
        raise FileNotFoundError("Model file not found: models/sla.h5")
    
    if os.path.exists("models/tsa_feature_extractor.h5"):
        full_tsa_fe_model = tf.keras.models.load_model("models/tsa_feature_extractor.h5")
        tsa_fe_model = tf.keras.models.Model(inputs=full_tsa_fe_model.input, outputs=full_tsa_fe_model.layers[-6].output)
        tsa_fe_model.trainable = False
    else :
        raise FileNotFoundError("Model file not found: models/tsa_feature_extractor.h5")
    
    if os.path.exists("models/tsa_lstm.keras"):
        tsa_lstm_model = tf.keras.models.load_model("models/tsa_lstm.keras")
        tsa_lstm_model.trainable = False
    else :
        raise FileNotFoundError("Model file not found: models/tsa_lstm.keras")



app = Flask(__name__)


def read_image(file):
    file_bytes = np.frombuffer(file.read(), np.uint8)
    image = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
    return image


@app.route("/single-line-predict", methods=["POST"])
def single_line_predict():
    try:
        # Get both images
        retinal_fundus = request.files.get("retinal_fundus")
        tomogram = request.files.get("tomogram")

        if retinal_fundus is None or tomogram is None:
            return jsonify({"error": "Both retinal_fundus and tomogram are required"}), 400

        # Read images
        retinal_fundus_img = read_image(retinal_fundus)
        tomogram_img = read_image(tomogram)

        print(f"Received retinal_fundus image shape: {retinal_fundus_img.shape}")
        print(f"Received tomogram image shape: {tomogram_img.shape}")
        if retinal_fundus_img is None or tomogram_img is None or retinal_fundus_img.shape != (256, 256, 3) or tomogram_img.shape != (256, 256, 3):
            return jsonify({"error": "Invalid image input"}), 400

        # Add batch dimension
        retinal_feature = np.expand_dims(retinal_fundus_img, axis=0)
        tomogram_feature = np.expand_dims(tomogram_img, axis=0)

        # Model prediction (2 inputs)
        output = sla_model.predict([retinal_feature, tomogram_feature])

        scores = output[0].tolist()
        pred_class = CLASS_NAMES[np.argmax(scores)]

        # Convert to percentage (2 decimal places)
        scores_percent = [round(s * 100, 2) for s in scores]

        return jsonify({
            "prediction": pred_class,
            "scores": dict(zip(CLASS_NAMES, scores_percent))
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/temporal-sequence-predict", methods=["POST"])
def temporal_sequence_predict():
    radial_sequence = []
    raster_sequence = []
    for st, num_images in SCAN_TYPES.items():
        for i in range(1, num_images + 1):
            file = request.files.get(f"{st}_{i}")
            if file is None:
                return jsonify({"error": f"Missing image: {st}_{i}"}), 400
            img = read_image(file)
            if img is None or img.shape != (600, 600, 3):
                return jsonify({"error": f"Invalid image input: {st}_{i}"}), 400
            if st == "radial":
                radial_sequence.append(img)
            else:
                raster_sequence.append(img)

    radial_features = tsa_fe_model.predict(np.array(radial_sequence))
    raster_features = tsa_fe_model.predict(np.array(raster_sequence))
    radial_features = np.expand_dims(radial_features, axis=0)
    raster_features = np.expand_dims(raster_features, axis=0)
    output = tsa_lstm_model.predict([radial_features, raster_features])

    scores = output[0].tolist()
    pred_class = CLASS_NAMES[np.argmax(scores)]

    # Convert to percentage (2 decimal places)
    scores_percent = [round(s * 100, 2) for s in scores]


    return jsonify({
            "prediction": pred_class,
            "scores": dict(zip(CLASS_NAMES, scores_percent))
    })


if __name__ == "__main__":
    load_model()
    app.run(host="0.0.0.0", port=8000, debug=True)