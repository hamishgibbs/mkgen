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


def get_interpreter(config, file):

    config_extensions = [x["extensions"] for x in config["languages"]]

    file_ext = "." + file.split(".")[-1]

    language_index = [i for i, x in enumerate(config_extensions) if file_ext in x][0]

    return config["languages"][language_index]["interpreter"]
