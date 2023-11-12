# TODO решите задачу
import json


def task() -> float:
    with open("input.json") as file:
        data = json.load(file)
    summator = [d["score"] * d["weight"] for d in data]
    return round(sum(summator), ndigits=3)


print(task())
