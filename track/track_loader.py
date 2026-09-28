import json
import os

def load_track(filename):

    base_dir = os.path.dirname(__file__)

    filepath = os.path.join(
        base_dir,
        filename
    )

    with open(filepath, "r") as f:

        return json.load(f)