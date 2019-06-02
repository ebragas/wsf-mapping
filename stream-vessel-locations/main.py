#!/usr/bin/env python

"""Periodically get new vessel locations from the WSF Vessel Locations API endpoint
and append them to csv file.
"""

import os
import requests
import json
import yaml
import logging
import csv
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)



if __name__ == "__main__":

    # Log start
    exec_start = datetime.now()
    logging.debug("Start time: {}".format(exec_start))

    # Setup
    curr_dir = os.path.dirname(__file__)

    # Read config file
    with open(os.path.join(curr_dir, "config.yaml")) as fp:
        config = yaml.load(fp, Loader=yaml.BaseLoader)
    logging.debug(config)

    # Request vessel locations
    params = {"apiaccesscode": config["api_access_code"]}
    response = requests.get(config["api_url"], params=params)
    data = response.json()
    fieldnames = data[0].keys()

    # Write CSV headers if file not exists
    if not os.path.isfile(os.path.join(curr_dir, "data", "locations.csv")):
        with open(os.path.join(curr_dir, "data", "locations.csv"), "w", newline="") as fp:
            writer = csv.DictWriter(fp, fieldnames=fieldnames)
            writer.writeheader()

    # Write all rows
    with open(os.path.join(curr_dir, "data", "locations.csv"), "a", newline="") as fp:
        writer = csv.DictWriter(fp, fieldnames=fieldnames)
        writer.writerows(data)

    # Log end
    exec_end = datetime.now()
    logging.debug("End time: {}".format(exec_end))
    logging.debug("Duration: {}".format(exec_end - exec_start))
