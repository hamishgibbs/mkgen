
def project():

    return True


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
