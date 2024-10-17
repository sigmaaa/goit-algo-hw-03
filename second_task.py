import matplotlib.pyplot as plt
import numpy as np


def koch_snowflake_edge(p1, p2, level):
    if level == 0:
        return np.array([p1, p2])
    else:
        # Рекурсивний поділ відрізка на три частини
        p1 = np.array(p1)
        p2 = np.array(p2)
        delta = (p2 - p1) / 3

        # Точки для нових відрізків
        p3 = p1 + delta
        p4 = p2 - delta

        # Поворот для утворення піка сніжинки
        angle = np.pi / 3  # 60 градусів
        rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                    [np.sin(angle), np.cos(angle)]])
        p5 = p3 + np.dot(rotation_matrix, delta)

        # Рекурсивно малюємо чотири нові відрізки
        return np.vstack([koch_snowflake_edge(p1, p3, level - 1),
                          koch_snowflake_edge(p3, p5, level - 1),
                          koch_snowflake_edge(p5, p4, level - 1),
                          koch_snowflake_edge(p4, p2, level - 1)])


def koch_snowflake(level):
    # Початковий рівносторонній трикутник
    p1 = np.array([0, 0])
    p2 = np.array([1, 0])
    angle = 2 * np.pi / 3  # 120 градусів
    rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
                                [np.sin(angle), np.cos(angle)]])
    p3 = np.dot(rotation_matrix, p2 - p1) + p1

    # Створення сніжинки з трьох сторін
    side1 = koch_snowflake_edge(p1, p2, level)
    side2 = koch_snowflake_edge(p2, p3, level)
    side3 = koch_snowflake_edge(p3, p1, level)

    # Повертаємо масив точок для трьох сторін
    return np.vstack([side1, side2, side3])


if __name__ == "__main__":
    level = int(input("Введіть рівень рекурсії: "))

    snowflake = koch_snowflake(level)

    plt.figure(figsize=(15, 15))
    plt.plot(snowflake[:, 0], snowflake[:, 1], color="blue")
    plt.title(f"Сніжинка Коха - рівень {level}")
    plt.axis('equal')
    plt.show()
