import matplotlib.pyplot as plt
import numpy as np


def koch_snowflake_edge(p1, p2, level):
    if level == 0:
        return np.array([p1, p2])
    else:
        # Recursive division of the segment into three parts
        p1 = np.array(p1)
        p2 = np.array(p2)
        delta = (p2 - p1) / 3

        # Points for the new segments
        p3 = p1 + delta
        p4 = p2 - delta

        # Rotation to form the snowflake peak
        angle = np.pi / 3  # 60 degrees
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                    [np.sin(angle), np.cos(angle)]])
        p5 = p3 + np.dot(rotation_matrix, delta)

        # Recursively draw four new segments
        return np.vstack([koch_snowflake_edge(p1, p3, level - 1),
                          koch_snowflake_edge(p3, p5, level - 1),
                          koch_snowflake_edge(p5, p4, level - 1),
                          koch_snowflake_edge(p4, p2, level - 1)])


def koch_snowflake(level):
    # Initial equilateral triangle
    p1 = np.array([0, 0])
    p2 = np.array([1, 0])
    angle = 2 * np.pi / 3  # 120 degrees
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    p3 = np.dot(rotation_matrix, p2 - p1) + p1

    # Create the snowflake from the three sides
    side1 = koch_snowflake_edge(p1, p2, level)
    side2 = koch_snowflake_edge(p2, p3, level)
    side3 = koch_snowflake_edge(p3, p1, level)

    # Return the array of points for the three sides
    return np.vstack([side1, side2, side3])


if __name__ == "__main__":
    level = int(input("Enter recursion level: "))

    snowflake = koch_snowflake(level)

    plt.figure(figsize=(15, 15))
    plt.plot(snowflake[:, 0], snowflake[:, 1], color="blue")
    plt.title(f"Koch Snowflake - level {level}")
    plt.axis('equal')
    plt.show()
