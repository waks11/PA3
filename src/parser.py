def parse_input(lines):
    # Get rid of all whitespace and ignore empty lines
    stripped_lines = []
    for line in lines:
        line = line.strip()
        if line != "":
            stripped_lines.append(line)

    # Iterate through each line and create a dict of char, values
    k_val, values = int(stripped_lines[0]), {}
    for i in range(1, k_val + 1):
        char, val = stripped_lines[i].split()
        values[char] = int(val)

    # Pull out a, b strings
    a = stripped_lines[k_val + 1]
    b = stripped_lines[k_val + 2]

    return values, a, b