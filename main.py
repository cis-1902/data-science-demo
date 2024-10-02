import numpy as np
import requests


def get_data():
    requests.get("http://google.com")

    print("Data fetched")


get_data()
