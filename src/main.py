import re
import os


def fn_detect(lines):

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
    # Function to take a list of path positions and divide them into "inputs" and "outputs."
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

    # Find the highest different between true index and previous true index
    max_gap = max([x[1] for x in dist])

    # Define the break point between input and output groups
    break_point = [x[0] for x in dist if x[1] == max_gap][0] - 1

    # Split input indices from output indices
    inputs = [x[0] for x in dist if x[0] < break_point]

    outputs = [x[0] for x in dist if x[0] > break_point]

    return [inputs, outputs]


def construct_target(file, fns, io, exec = "$(PYTHON)"):

    name = file.split("/")[0].split(".")[0]

    target = name + ": " + file

    for input in io[0]:

        target = target + " " + fns[input]

    for output in io[1]:

        target = target + " " + fns[output]

    return target + "\n\t" + exec


def main(root_dir):

    # DEV: need to extract only the correct data files

    code_files = os.listdir(root_dir)

    targets = []

    # looping through all project code files
    # extract this logic from main function later
    for file in code_files:

        with open(root_dir + "/" + file, "r") as f:
            lines = f.readlines()

        fns = fn_detect(lines)
        io = io_detect(fns)

        targets.append(construct_target(file, fns, io))


    print(targets)

    ## update Makefile


#main("/Users/hamishgibbs/Documents/productivity/mkgen/tests/data")
