import re
import os
import glob
import json

from mkgen.config import (
    get_interpreter,
    get_code_files
)
from mkgen.makefile import (
    get_mkgen_indices,
    insert_new_targets,
    construct_target
)
from mkgen.utils import flat


def fn_detect(lines):
    """
    Extracts file paths from code files using a file path regex.
    For a file of n lines, return a n length list of:
        * boolean: False (no path detected)
        * str: Detected file path
    """

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
    """
    Algorithm to partition a list of file paths into two groups [inputs, outputs].

    The algorithm assumes a standard i/o pattern of reading data from files,
    performing operations on data, and writing new files.

    How it works:
        Calculate the distance between detected paths and divide the list at the
        max distance into inputs (first) and outputs (last).

    **Note:** This algorithm will fail for patterns other than the pattern
    described above , for example if all i/o is specified at the top of a script.
    """

    # TODO: Optimise this further for fun
    dist = []

    for i, position in enumerate(path_positions):

        if position:

            try:
                prev_position = dist[-1][0]
            except Exception:
                prev_position = 0

            dist.append((i, i - prev_position))

    max_gap = max([x[1] for x in dist])

    break_point = [x[0] for x in dist if x[1] == max_gap][0] - 1

    inputs = [x[0] for x in dist if x[0] < break_point]

    outputs = [x[0] for x in dist if x[0] > break_point]

    return [inputs, outputs]


def parse_code_file(config, file, lines):

    fns = fn_detect(lines)
    io = io_detect(fns)
    interpreter = get_interpreter(config, file)
    return construct_target(file, fns, io, interpreter)


def main():
    """
    Automatically generate Makefile targets from code files.

    Objective:
        Provide a simple way to automatically build a research project
        while flexibly accomodating multiple languages and coding patterns.

    How it works:
        * Extract file paths from code files (search paths specified in
          mkgen.json config file)
        * Generate Makefile targets
        * Overwrite old Makefile targets with newly generated targets

    Assumptions:
        1. os.getcwd() provides the root directory of the project.
        2. The root has a mkgen.json file.
        3. The root has a Makefile file with comments for autogenerated targets:
            * # -- mkgen targets start --
            * # -- mkgen targets end --

    Shortcomings:
        * Project file names must be unique.
        * File i/o must be explicit. `mkgen` cannot track input or output through
          nested code execution.
        * i/o files must be accesible from your root project directory.
        * Files must perform input and output - `mkgen` will not handle
          creating and writing data without input.

    """

    # TODO: Add a known mkgen comment to ignore a certain file when parsing
    # i.e. # -- mkgen ignore --

    # DEV: We cannot address all coding patterns or cases but can do as much as
    # possible and fail gracefully

    try:
        with open(os.getcwd() + "/mkgen.json") as f:
            config = json.load(f)
    except Exception:
        raise Exception("Unable to find mkgen.json file.")

    try:
        with open(os.getcwd() + "/Makefile", "r") as f:
            make_lines = f.readlines()
    except Exception:
        raise Exception("Unable to find Makefile file.")

    try:
        code_files = get_code_files(config)
    except Exception as e:
        raise Exception(f"Unable to locate files for parsing. Exception: {str(e)}")

    targets = []

    for file in code_files:

        try:
            with open(file, "r") as f:
                code_lines = f.readlines()
            targets.append(parse_code_file(config, file, code_lines))
        except Exception as e:
            print(f"Unable to parse { file } with Exception { str(e) }. Skipping.")
            pass

    start, end = get_mkgen_indices(make_lines)

    try:
        with open(os.getcwd() + "/Makefile", "w") as f:
            [f.write(x) for x in insert_new_targets(start, end, make_lines, targets)]
    except Exception:
        raise Exception("Unable to write new targets.")

    print(f"\U0001F389 Wrote { len(targets) } targets.")
