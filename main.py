from retrive_satellite_imgae import fetch_satellite_image
from Predict import solar_panel_predict
import json


def detector(address, api_key, zoom=18, size="640x640"):
    img_name = fetch_satellite_image(address, api_key, zoom=zoom, size=size)
    prediction, im = solar_panel_predict(img_name)
    return prediction, im


if __name__ == '__main__':
    # import api_key from json
    with open("secret.json") as file:
        api_key = json.load(file)["google_maps_api_key"]
    address = "anger strase 12, gottingen, germany"
    zoom = 20
    prediction, im = detector(address, api_key, zoom=zoom)
    print(prediction)
    im.show()
