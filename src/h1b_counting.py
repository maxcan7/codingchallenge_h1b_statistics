#!/usr/bin/python
#
# The defined function h1bwrite takes the input and output paths and the variable names for SOC name,
# certification status, and state (*args). The order of arguments should be the input path, occupations output path,
# states output path, and the variable names in the dataset for SOC name, certification status, and state.


def h1bwrite(*args):

    import csv
    from collections import Counter

    # Separate input and output paths and variables into separate lists
    inputpath = [i for i in args if "./input/" in i]
    outputpaths = [i for i in args if "./output/" in i]
    variables = args[3:6]

    # Loop through the rows, pulling out the variables
    line_count = 0
    with open(inputpath[0], encoding="utf8") as inputfile:
        # Create a dictReader variable for each input
        data_in = csv.DictReader(inputfile, delimiter=';')
        # Iterate through rows, finding the soc_name, certification, and state, and make it a list
        for row in data_in:
            if line_count == 0:
                h1blist = [[row[variables[0]], row[variables[1]], row[variables[2]]]]
                line_count += 1
            else:
                h1blist.append([row[variables[0]], row[variables[1]], row[variables[2]]])

    # Separate soc_name and certification status, and state for later use
    soc_name = [k[0] for k in h1blist]
    cert = [k[1] for k in h1blist]
    state = [k[2] for k in h1blist]
    # Get a count of soc_names and find the top 10
    top_occ = Counter(soc_name)
    top_occ = top_occ.most_common(10)
    # Get rid of count for top_occ
    top_occ_name = [k[0] for k in top_occ]
    top_occ = top_occ_name
    # Get a count of states and find the top 10
    top_state = Counter(state)
    top_state = top_state.most_common(10)
    # Get rid of count for top_state
    top_state_name = [k[0] for k in top_state]
    top_state = top_state_name

    # Loop through soc_name, find where soc_name is one of the top_occ and cert == 'CERTIFIED'. Update index of
    # cert using cert_idx. If a cert_count has not started, the elif will start the count.
    cert_count = {}
    cert_idx = 0
    for k in soc_name:
        if k in cert_count and k in top_occ and cert[cert_idx] == 'CERTIFIED':
            cert_count[k] = cert_count[k] + 1
        elif k in top_occ and cert[cert_idx] == 'CERTIFIED':
            cert_count[k] = 1
        cert_idx += 1

    # Calculate total certified for later use
    total_cert = cert.count('CERTIFIED')

    # Add certification count and percent to top_occ
    for k in range(0, top_occ.__len__()):
        top_occ[k] = ((top_occ[k],) + (cert_count.get(top_occ[k]),))
    for k in range(0, top_occ.__len__()):
        if top_occ[k][1] is not None:
            top_occ[k] = (top_occ[k] + (str(round((top_occ[k][1] / total_cert)*100, 1)) + '%',))
        else:
            # If there were no CERTIFIED for a given top occupation
            top_occ[k] = (top_occ[k] + ('0%',))

    # Loop through state, find where state is one of the top_state and cert == 'CERTIFIED'. Update index of cert using
    # cert_idx. If a cert_count has not started, the elif will start the count.
    cert_count = {}
    cert_idx = 0
    for k in state:
        if k in cert_count and k in top_state and cert[cert_idx] == 'CERTIFIED':
            cert_count[k] = cert_count[k] + 1
        elif k in top_state and cert[cert_idx] == 'CERTIFIED':
            cert_count[k] = 1
        cert_idx += 1

    # Add certification count and percent to top_state
    for k in range(0, top_state.__len__()):
        top_state[k] = ((top_state[k],) + (cert_count.get(top_state[k]),))
    for k in range(0, top_state.__len__()):
        if top_state[k][1] is not None:
            top_state[k] = (top_state[k] + (str(round((top_state[k][1] / total_cert)*100, 1)) + '%',))
        else:
            # If there were no CERTIFIED for a given top state
            top_state[k] = (top_state[k] + ('0%',))

    # Iterate over each output j
    for j in outputpaths:
        # Open each output and write
        with open(j, 'w', encoding="utf8") as outputfile:
            if j == outputpaths[0]:
                line_count = 0
                for top_out in top_occ:
                    if line_count == 0:
                        occ_vars = ("TOP_OCCUPATIONS", "NUMBER_CERTIFIED_APPLICATIONS", "PERCENTAGE")
                        outputfile.write(';'.join(str(s) for s in occ_vars) + '\n')
                        line_count += 1
                    outputfile.write(';'.join(str(s) for s in top_out) + '\n')
            elif j == outputpaths[1]:
                line_count = 0
                for top_out in top_state:
                    if line_count == 0:
                        state_vars = ("TOP_STATES", "NUMBER_CERTIFIED_APPLICATIONS", "PERCENTAGE")
                        outputfile.write(';'.join(str(s) for s in state_vars) + '\n')
                        line_count += 1
                    outputfile.write(';'.join(str(s) for s in top_out) + '\n')


# Manually change the path names and number of inputs. The last two arguments should be the occupations and states
# outputs, respectively.

h1bwrite('./input/H1B_FY_2014.csv', './output/top_10_occupations.txt', './output/top_10_states.txt',
         'LCA_CASE_SOC_NAME', 'STATUS', 'LCA_CASE_WORKLOC1_STATE')
