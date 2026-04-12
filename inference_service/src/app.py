
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
        single_line_model = tf.keras.models.load_model("models/single_line_model.h5")
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
        left_file = request.files.get("left_image")
        right_file = request.files.get("right_image")

        if left_file is None or right_file is None:
            return jsonify({"error": "Both left_image and right_image are required"}), 400

        # Read images
        left_img = read_image(left_file)
        right_img = read_image(right_file)

        if left_img is None or right_img is None or left_img.shape != (224, 224, 3) or right_img.shape != (224, 224, 3):
            return jsonify({"error": "Invalid image input"}), 400

        # Add batch dimension
        l_feature = np.expand_dims(left_img, axis=0)
        r_feature = np.expand_dims(right_img, axis=0)

        # Model prediction (2 inputs)
        output = single_line_model.predict([l_feature, r_feature])

        scores = output[0].tolist()
        pred_class = CLASS_NAMES[np.argmax(scores)]

        return jsonify({
            "prediction": pred_class,
            "scores": dict(zip(CLASS_NAMES, scores))
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    load_model()
    app.run(host="0.0.0.0", port=8000, debug=True)