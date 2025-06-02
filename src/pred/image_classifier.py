from src.pred.models.tf_pred import tf_predict
from src.utils.utilities import load_image
from src.pred.models.class_labels import class_labels
from typing import Any

def tf_run_classifier(image: str) -> Any:
    img = load_image(image)
    if img is None:
        return None
    pred_results = tf_predict(img, class_labels)
    pred_results["status_code"] = 200
    return pred_results
