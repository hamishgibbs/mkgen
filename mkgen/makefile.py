
def construct_target(file, fns, io, interpreter):

    name = file.split(".")[0].split("/")[-1]

    inputs = [fns[x] for x in io[0]]
    outputs = [fns[x] for x in io[1]]

    target = "\n" + name + ": " + " ".join(outputs) + "\n\n"

    target = target + " ".join(outputs) + ": " + file + " \ \n\t\t" + " \ \n\t\t".join(inputs) + "\n\t" + interpreter + "\n\n"

    return target


def get_mkgen_indices(make_lines):

    start = [i for i, x in enumerate(make_lines) if x == "# -- mkgen targets start --\n"][0]
    end = [i for i, x in enumerate(make_lines) if x == "# -- mkgen targets end --\n"][0]

    return (start, end)


def insert_new_targets(start, end, make_lines, targets):
    # remove lines between the auto generated annotations
    # and insert new targets between start and end indices

    return make_lines[:start+1] + targets + make_lines[end:]
