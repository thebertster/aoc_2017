from lib.aoclib import AOCLib

puzzle = (2017, 24)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

components = [tuple(component.split('/')) for component in puzzle_input]

# print(puzzle_input)

# Puzzle solution parts 1 and 2

bridges = [[('0', ), component]
           for component
           in components
           if '0' in component]

complete_bridges = []
strongest_bridge = 0
strongest_longest_bridge = (0, 0)

while bridges:
    bridge = bridges.pop()
    valid_port = (bridge[-1][0]
                  if bridge[-1][1] in bridge[-2]
                  else bridge[-1][1])

    valid_components = [component
                        for component
                        in components
                        if valid_port in component
                        and component not in bridge]

    if valid_components:
        for component in valid_components:
            new_bridge = bridge[:]
            new_bridge.append(component)
            bridges.append(new_bridge)
    else:
        complete_bridges.append(bridge)
        bridge_strength = sum([sum([int(port) for port in component])
                               for component in bridge])
        if bridge_strength > strongest_bridge:
            strongest_bridge = bridge_strength

        if len(bridge) > strongest_longest_bridge[0]:
            strongest_longest_bridge = (len(bridge), bridge_strength)
        elif len(bridge) == strongest_longest_bridge[0]:
            if bridge_strength > strongest_longest_bridge[1]:
                strongest_longest_bridge = (len(bridge), bridge_strength)

aoc.print_solution(1, strongest_bridge)
aoc.print_solution(2, strongest_longest_bridge[1])
