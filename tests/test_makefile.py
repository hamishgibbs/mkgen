from mkgen.makefile import construct_target, get_mkgen_indices, insert_new_targets


def test_construct_target():

    fns = [False, False, "test.csv", False, False, "test.rds"]

    res = construct_target("file.R", fns, [[2], [5]], "$(PYTHON)")

    assert res == "\nfile: test.rds\n\ntest.rds: file.R \\ \n\t\ttest.csv\n\t$(PYTHON)\n\n"


def test_get_mkgen_indices():

    make_lines = [
        "",
        "other stuff",
        "",
        "# -- mkgen targets start --\n",
        "",
        "# -- mkgen targets end --\n"
    ]

    start, end = get_mkgen_indices(make_lines)

    assert start == 3
    assert end == 5


def test_insert_new_targets():

    start, end = (3, 6)
    make_lines = [0, 0, 0, 1, 0, 0, 1, 0]
    targets = [2, 2, 2, 2]

    res = insert_new_targets(start, end, make_lines, targets)

    assert res == [0, 0, 0, 1, 2, 2, 2, 2, 1, 0]
