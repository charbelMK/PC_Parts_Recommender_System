import os
import time
import json
import pandas as pd
from pcpartpicker import API

api = API()
motherboard_data = api.retrieve("motherboard")
all_data = api.retrieve_all()

sr = pd.motherboard()
sr.to_json()