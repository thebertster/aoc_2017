from lib.aoclib import AOCLib

puzzle = (2017, 20)

# Initialise the helper library

aoc = AOCLib(puzzle[0])

# Get the puzzle input

puzzle_input = aoc.get_puzzle_input(puzzle[1], AOCLib.lines_to_list)

# print(puzzle_input)

particle_p = []
particle_v = []
particle_a = []
particle_c = []
particle_d = []

for config in puzzle_input:
    config_elements = config.split(', ')

    particle_p.append([int(coord)
                       for coord
                       in config_elements[0][3:-1].split(',')])
    particle_v.append([int(coord)
                       for coord
                       in config_elements[1][3:-1].split(',')])
    particle_a.append([int(coord)
                       for coord
                       in config_elements[2][3:-1].split(',')])
    particle_c.append(False)
    particle_d.append(None)

num_particles = len(particle_p)

# Puzzle solution parts 1 & 2
#
# Instead of removing particles when they collide (which would
# potentially affect the answer to part 1), they are marked
# as having collided (particle_c).

ticks = 500

while ticks:
    closest_to_origin = 0
    for particle in range(num_particles):
        particle_v[particle][0] += particle_a[particle][0]
        particle_v[particle][1] += particle_a[particle][1]
        particle_v[particle][2] += particle_a[particle][2]
        particle_p[particle][0] += particle_v[particle][0]
        particle_p[particle][1] += particle_v[particle][1]
        particle_p[particle][2] += particle_v[particle][2]
        particle_d[particle] = sum([abs(coord)
                                    for coord
                                    in particle_p[particle]])

        if particle_d[particle] < particle_d[closest_to_origin]:
            closest_to_origin = particle

    for particle_1 in range(num_particles-1):
        if not particle_c[particle_1]:
            if particle_p[particle_1] in particle_p[particle_1 + 1:]:
                collision = False
                for particle_2 in range(particle_1 + 1, num_particles):
                    if (not particle_c[particle_2]
                        and particle_p[particle_2] == particle_p[particle_1]):
                        particle_c[particle_2] = True
                        collision = True
                if collision:
                    particle_c[particle_1] = True

    ticks -= 1

print('Puzzle Output 1: {}'.format(closest_to_origin))
print('Puzzle Output 2: {}'.format(particle_c.count(False)))
