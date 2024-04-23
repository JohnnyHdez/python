#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import json
from datetime import datetime

def records(path: str):
    my_record = ""

    with open(path, encoding="utf-8") as file:
        my_record = json.load(file)
    
    orden = 1
    for data in my_record:
        print("Anime {}: {}. Estado: {}".format(orden, data.get("Name"), data.get("Estado")))
        print("Proximo: {}".format(data.get("Proximo")))
        print(type(data.get("Proximo")))
        orden += 1

if __name__ == "__main__":
    path = os.path.join("ddbb", "animes.json")
    records(path)
