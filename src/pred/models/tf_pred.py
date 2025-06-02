import os
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"
import tensorflow as tf
import numpy as np
from PIL import Image
from src.pred.models.class_labels import *

MODEL_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "Trafic_signs_model.keras"))
IMAGE_SHAPE = (30, 30)  # Kendi modelinizin giriş boyutu
model = tf.keras.models.load_model(MODEL_PATH)

def preprocess_img(img):
    img = img.resize(IMAGE_SHAPE)
    img = np.array(img) 
    img = np.expand_dims(img, axis=0)
    return img

def tf_predict(img_original, class_labels):

    img = preprocess_img(img_original)
    predictions = model.predict(img)
    predicted_class_index = np.argmax(predictions, axis=1)[0]
    probability = np.max(predictions, axis=1)[0]
    predicted_label = class_labels[predicted_class_index]
    return {"predicted_label": predicted_label, "probability": float(probability)}