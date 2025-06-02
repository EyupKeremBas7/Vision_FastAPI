from locust import HttpUser, task, between
import random
import json
from src.utils.test_images import image_links
collect_ignore = ["locust_test.py"]
def predict_test(client, api_url):
    json_body = random.choice(image_links)
    headers = {"Content-Type": "application/json"}
    with client.post(api_url, data=json.dumps(json_body), headers=headers, catch_response=True) as response:
        try:
            if response.status_code == 200:
                response.success()
            else:
                response.failure(f"Status code: {response.status_code}, Body: {response.text}")
            return response.text
        except Exception as e:
            response.failure(f"Exception: {e}")
            return str(e)

class PerformanceTests(HttpUser):
    wait_time = between(1, 1)

    @task(1)
    def test_tf_predict(self):
        res = predict_test(self.client, "/predict/tf/")
        print("res", res)