import os
import glob
from mkgen.utils import flat

default_config = {
    "languages": [
        {"name": "python", "extensions": [".py"], "interpreter": "$(PYTHON)"},
        {"name": "R", "extensions": [".R", ".r"], "interpreter": "$(R)"},
    ],
    "src_paths": ["src"],
}


def get_interpreter(config, file):

    config_ext = [x["extensions"] for x in config["languages"]]

    file_ext = "." + file.split(".")[-1]

    language_index = [i for i, x in enumerate(config_ext) if file_ext in x][0]

    return config["languages"][language_index]["interpreter"]


def get_code_files(config):

    extensions = flat([x["extensions"] for x in config["languages"]])

    code_files = []

    for src_path in config["src_paths"]:
        for ext in extensions:
            fns = glob.glob(os.getcwd() + "/" + src_path + "/*" + ext, recursive=True)
            code_files.append(fns)

    return flat(code_files)
