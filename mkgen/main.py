import re
import os
import glob

from mkgen.config import read_config


def flat(t):
    return [item for sublist in t for item in sublist]


def fn_detect(lines):
    # Regex to extract paths from file lines

    fn_positions = []

    exp = r"(?:'|\")(.*?\/.*?\.[\w:]+.*)(?:'|\")"

    for line in lines:
        match = re.search(exp, line)

        if match:
            fn_positions.append(match.group(1))
        else:
            fn_positions.append(False)

    return fn_positions


def io_detect(path_positions):
    # Function to take a list of path positions and divide them into "inputs"
    # and "outputs"
    # DEV: doc and optimise this better

    # store index of True and distance from previous true in a tuple
    dist = []

    for i, position in enumerate(path_positions):

        if position:

            try:
                prev_position = dist[-1][0]
            except Exception:
                prev_position = 0

            dist.append((i, i - prev_position))

    # Find the highest distance
    max_gap = max([x[1] for x in dist])

    # Define the break point index between input and output groups
    break_point = [x[0] for x in dist if x[1] == max_gap][0] - 1

    # Split input and output indices
    inputs = [x[0] for x in dist if x[0] < break_point]

    outputs = [x[0] for x in dist if x[0] > break_point]

    return [inputs, outputs]


def get_interpreter(config, file):

    config_extensions = [x["extensions"] for x in config["languages"]]

    file_ext = "." + file.split(".")[-1]

    language_index = [i for i, x in enumerate(config_extensions) if file_ext in x][0]

    return config["languages"][language_index]["interpreter"]


def construct_target(file, fns, io, interpreter):

    name = file.split(".")[0].split("/")[-1]

    inputs = [fns[x] for x in io[0]]
    outputs = [fns[x] for x in io[1]]

    target = "\n" + name + ": " + " ".join(outputs) + "\n\n"

    target = target + " ".join(outputs) + ": " + file + " \ \n\t\t" + " \ \n\t\t".join(inputs) + "\n\t" + interpreter + "\n\n"

    return target


def get_code_files(config):

    extensions = flat([x["extensions"] for x in config["languages"]])

    code_files = []

    for src_path in config["src_paths"]:
        for ext in extensions:
            fns = glob.glob(os.getcwd() + "/" + src_path + "/*" + ext,
                            recursive=True)
            code_files.append(fns)

    return flat(code_files)


def main():

    config = read_config()

    # DEV: need to extract only the correct data files
    # DEV need to do some work to simplify path navigation
    # like by assuming that the program is executed from project root or similar
    # assumption is that execution (cwd) is located at project root
    root_dir = os.getcwd()
    code_files = get_code_files(config)

    targets = []

    # looping through all project code files
    # extract this logic from main function later
    for file in code_files:

        with open(file, "r") as f:
            lines = f.readlines()

        fns = fn_detect(lines)
        io = io_detect(fns)

        targets.append(construct_target(file, fns, io, get_interpreter(config, file)))

    with open(root_dir + "/Makefile", "r") as f:

        make_lines = f.readlines()

    start = [i for i, x in enumerate(make_lines) if x == "# -- mkgen targets start --\n"][0]
    end = [i for i, x in enumerate(make_lines) if x == "# -- mkgen targets end --\n"][0]

    # remove lines between the auto generated annotations
    # and insert new targets between start and end indices
    make_lines = make_lines[:start+1] + targets + make_lines[end:]

    with open(root_dir + "/Makefile", "w") as f:

        [f.write(x) for x in make_lines]
