import os


def construct_target(file, fns, io, interpreter):

    file = file.replace(os.getcwd() + "/", "")

    name = file.split(".")[0].split("/")[-1]

    inputs = [fns[x] for x in io[0]]
    outputs = [fns[x] for x in io[1]]

    target = "\n" + name + ": " + " ".join(outputs) + "\n\n"

    target = target + " ".join(outputs)
    target = target + ": " + file + " \\\n\t\t" + " \\\n\t\t".join(inputs)
    target = target + "\n\t" + interpreter + " $^ $@\n\n"

    return target


def get_mkgen_indices(make_lines):

    start_comment = "# -- mkgen targets start --"
    end_comment = "# -- mkgen targets end --"

    start = [i for i, x in enumerate(make_lines) if start_comment in x][0]
    end = [i for i, x in enumerate(make_lines) if end_comment in x][0]

    return (start, end)


def insert_new_targets(start, end, make_lines, targets):
    """
    Insert new targets in Makefile between mkgen annotations
    """

    return make_lines[: start + 1] + targets + make_lines[end:]
