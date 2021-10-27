import pytest
from src.main import io_detect, fn_detect, construct_target, get_interpreter


@pytest.fixture()
def file_lines():

    lines = [
        'require(some stuff)',
        "x <- read_csv('/path/to/a/file.shp')",
        '',
        'add_five <- function(x){',
        '   return(x + 5)',
        '}',
        '',
        'x <- add_five(x)',
        'write_csv(x, "/path/to/my/output.csv")'
    ]

    return lines


def test_fn_detect_absolute(file_lines):

    res = fn_detect(file_lines)

    assert res == [False, "/path/to/a/file.shp", False, False, False,
                   False, False, False, "/path/to/my/output.csv"]


def test_fn_detect_relative(file_lines):

    file_lines.append('write_csv(x, "path/to/my/output2.csv")')

    res = fn_detect(file_lines)

    assert res == [False, "/path/to/a/file.shp", False, False, False,
                   False, False, False, "/path/to/my/output.csv",
                   "path/to/my/output2.csv"]


def test_io_detect():

    path_positions = [0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1]

    res = io_detect(path_positions)

    assert res[0] == [1, 2, 3, 5]
    assert res[1] == [9, 10]


def test_io_detect_minimal():

    path_positions = [1, 0, 1]

    res = io_detect(path_positions)

    assert res[0] == [0]
    assert res[1] == [2]


def test_io_detect_undefined():
    # when there are two equal length gaps - at least return the
    # division between the first two groups

    path_positions = [1, 1, 0, 0, 1, 0, 0, 1]

    res = io_detect(path_positions)

    assert res[0] == [0, 1]
    assert res[1] == [4, 7]


def test_construct_target():

    fns = [False, False, "test.csv", False, False, "test.rds"]

    res = construct_target("file.R", fns, [[2], [5]], "$(PYTHON)")

    assert res == "\nfile: test.rds\n\ntest.rds: file.R \\ \n\t\ttest.csv\n\t$(PYTHON)\n\n"


def test_get_interpreter():

    config = {"languages": [
        {"name": "python",
         "extensions": [".py"],
         "interpreter": "$(PYTHON)"},
        {"name": "R",
         "extensions": [".R", ".r"],
         "interpreter": "$(R)"}
    ]}

    res = get_interpreter(config, "file/here/test.R")

    assert res == "$(R)"
