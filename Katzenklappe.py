#https://universe.roboflow.com/maschde/katzenklappe-haovi/model/1

from inference_sdk import InferenceHTTPClient

CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="oaPMHkniKynVt28lO5lt"
)

result = CLIENT.infer(2024_04_11_21_37_23_690702_cat_prey.jpg, model_id="katzenklappe-haovi/1")