from mkgen.config import get_interpreter, default_config


def test_get_interpreter_py():

    res = get_interpreter(default_config, "path/to/file.py")

    assert res == "$(PYTHON)"


def test_get_interpreter_r():

    res = get_interpreter(default_config, "path/to/file.R")

    assert res == "$(R)"
