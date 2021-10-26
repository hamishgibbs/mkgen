from src.main import project, io_detect


def test_project():

    assert project()


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
