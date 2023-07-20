# Snail Sort
# Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
# For better understanding, please follow the numbers of the next array consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
# This image will illustrate things more clearly:
#
#
# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snail shell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].


def snail(snail_map):
    # Get the size of the square matrix (n x n)
    square_length = len(snail_map[0])

    # Calculate the total number of squares in the matrix
    total_squares = square_length ** 2

    # Initialize the starting and ending positions for traversal
    start_position = 0
    end_position = square_length - 1

    # Initialize an empty list to store the snail traversal output
    output = []

    # Continue the traversal until all elements are processed
    while len(output) < total_squares:

        # Check if we have reached the center element of the odd-sized matrix
        if start_position == end_position:
            output.append(snail_map[start_position][start_position])
            break

        # Add elements in the current row (left to right) to the output
        output.extend(snail_map[start_position][start_position:end_position])

        # Add elements in the last column (top to bottom) to the output
        for square in range(start_position, end_position):
            output.append(snail_map[square][end_position])

        # Add elements in the last row (right to left) to the output
        output.extend(snail_map[end_position][end_position:start_position:-1])

        # Add elements in the first column (bottom to top) to the output
        for square2 in reversed(range(start_position + 1, end_position + 1)):
            output.append(snail_map[square2][start_position])

        # Move to the next "inner" square by updating start_position and end_position
        start_position += 1
        end_position -= 1

    return output


print(snail([[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
            ))

print(snail([[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]]
            ))
