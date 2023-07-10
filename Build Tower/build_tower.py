# Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.
#
# For example, a tower with 3 floors looks like this:
#
# [
#   "  *  ",
#   " *** ",
#   "*****"
# ]
# And a tower with 6 floors looks like this:
#
# [
#   "     *     ",
#   "    ***    ",
#   "   *****   ",
#   "  *******  ",
#   " ********* ",
#   "***********"
# ]


print(tower_builder(3))

def tower_builder(n_floors):
    base_width = (2 * n_floors) - 1
    output = []
    for n in range(1, n_floors+1):
        floor = "*" * ((2 * n)-1)
        output.append(f"{floor: ^{base_width}}")
    return output

print(tower_builder(3))

# def tower_builder(n):
#     return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

