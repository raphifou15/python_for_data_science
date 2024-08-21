import os
import csv
import pandas as pd


def load_csv_dataset(path: str):
    if not path.endswith(".csv"):
        raise ValueError("Invalid file extension")
    if not os.path.isfile(path):
        raise FileNotFoundError("File not found")
    try:
        with open(path, "r") as file:
            csv.reader(file)
        data = pd.read_csv(path)
        if data.empty:
            raise ValueError("Empty file")
        return data
    except Exception as error:
        raise error


def load(path: str):  # -> Dataset
    try:
        data = load_csv_dataset(path)
        print("loading dataset of dimensions {}".format(data.shape))
        return data
    except Exception as error:
        print(error)
        return
