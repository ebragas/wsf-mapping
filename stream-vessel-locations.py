"""Periodically get new vessel locations from the WSF Vessel Locations API endpoint
and append them to csv file.
"""

import requests
import json
import yaml
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":

    # Log start
    exec_start = datetime.now()
    logging.debug("Start time: {}".format(exec_start))

    # Read config file
    with open("config.yaml") as fp:
        config = yaml.load(fp, Loader=yaml.BaseLoader)

    

    # Log end
    exec_end = datetime.now()
    logging.debug("End time: {}".format(exec_end))
    logging.debug("Execution duration: {}".format(exec_end - exec_start))
