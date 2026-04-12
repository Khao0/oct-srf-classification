
import os
from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import cv2

CLASS_NAMES = ["CSC", "Normal", "PCV", "VKH"]

single_line_model = None
temporal_seq_model = None

def load_model():
    global single_line_model
    global temporal_seq_models
    if os.path.exists("models/model.h5"):
        pass
    else :
        single_line_model = tf.keras.models.load_model("models/single-line-model.h5")
        single_line_model.trainable = False

    # if os.path.exists("models/temporal_seq_model.h5"):
    #     pass
    # else :
    #     temporal_seq_model = tf.keras.models.load_model("models/temporal_seq_model.h5")
    #     temporal_seq_model.trainable = False


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
        output = single_line_model.predict([retinal_feature, tomogram_feature])

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

if __name__ == "__main__":
    load_model()
    app.run(host="0.0.0.0", port=8000, debug=True)