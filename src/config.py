import json

default_config = {
    "languages": [
        {"name": "python",
         "extensions": [".py"],
         "interpreter": "$(PYTHON)"},
        {"name": "R",
         "extensions": [".R", ".r"],
         "interpreter": "$(R)"}
    ],
    "src_paths": ["src"]
}


def write_config(default_config):

    with open("mkgen.json", "w") as f:
        json.dump(default_config, f)


def read_config():

    with open("mkgen.json") as f:
        config = json.load(f)

    return config
