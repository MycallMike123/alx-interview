#!/usr/bin/python3

"""Module for a method that all the boxes in a list can be unlocked"""


def canUnlockAll(boxes):
    """Determines if all the boxes in the list can be unlocked"""

    if not boxes:
        return False

    # Create a list to keep track of visited boxes
    visited = [False] * len(boxes)
    visited[0] = True

    # Create a stack to store boxes to be visited
    stack = [0]

    # Perform depth-first search to visit all boxes
    while stack:
        # Pop the top box from the stack
        box = stack.pop()

        # Iterate through the keys in the current box
        for key in boxes[box]:
            # Check if the key is valid and the corresponding box
            # has not been visited
            if 0 <= key < len(boxes) and not visited[key]:
                # Mark the box as visited
                visited[key] = True
                # Add the box to the stack for further exploration
                stack.append(key)

    # Check if all boxes have been visited
    return all(visited)
