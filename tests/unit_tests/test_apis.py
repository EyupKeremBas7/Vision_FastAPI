import json
import pytest
from fastapi.testclient import TestClient
from src.app.app import app
from src.utils.test_images import image_links

client = TestClient(app)

@pytest.mark.parametrize("json_body", image_links)
def test_predict_tf(json_body):
    print("Test başlıyor:", json_body)
    try:
        res = client.post(
            "/predict/tf/",
            data=json.dumps(json_body),
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        print("Yanıt geldi:", res.status_code, res.text)
        assert res.status_code == 200
    except Exception as e:
        print("Hata oluştu:", e)
        raise