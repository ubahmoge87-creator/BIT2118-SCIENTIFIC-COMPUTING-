
import numpy as np

print("TASK 5: MATRIX ALGEBRA AND GEOMETRIC TRANSFORMATIONS")

# PART 1: ORIGINAL EXAMPLE - TRANSFORMING THE CORNERS OF A SQUARE

points = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1]
])

angle_degrees = 45
angle_radians = np.radians(angle_degrees)

rotation_matrix = np.array([
    [np.cos(angle_radians), -np.sin(angle_radians)],
    [np.sin(angle_radians), np.cos(angle_radians)]
])

scale_matrix = np.array([
    [2, 0],
    [0, 1.5]
])

transformation_matrix = rotation_matrix @ scale_matrix

transformed_points = points @ transformation_matrix.T

print("\nPART 1: ORIGINAL SQUARE")
print("Original points:")
print(points)

print("\nRotation matrix:")
print(rotation_matrix)

print("\nScale matrix:")
print(scale_matrix)

print("\nCombined transformation matrix:")
print(transformation_matrix)

print("\nTransformed points:")
print(np.round(transformed_points, 4))

print("\nDeterminant of transformation matrix:")
print(np.linalg.det(transformation_matrix))

# PART 2: MODIFICATION - CHANGE THE ROTATION AND SCALE

modified_angle_degrees = 30
modified_angle_radians = np.radians(modified_angle_degrees)

modified_rotation_matrix = np.array([
    [np.cos(modified_angle_radians), -np.sin(modified_angle_radians)],
    [np.sin(modified_angle_radians), np.cos(modified_angle_radians)]
])

modified_scale_matrix = np.array([
    [1.5, 0],
    [0, 0.75]
])

modified_transformation_matrix = (
    modified_rotation_matrix @ modified_scale_matrix
)

modified_points = points @ modified_transformation_matrix.T

print("\nPART 2: MODIFIED SQUARE")
print("Modified rotation angle:", modified_angle_degrees, "degrees")
print("Modified scale matrix:")
print(modified_scale_matrix)

print("\nModified transformation matrix:")
print(modified_transformation_matrix)

print("\nModified transformed points:")
print(np.round(modified_points, 4))

print("\nModified transformation determinant:")
print(np.linalg.det(modified_transformation_matrix))

# PART 3: RELATED REAL-WORLD APPLICATION - ROBOT MOVEMENT

robot_position = np.array([
    [2, 1],
    [4, 1],
    [4, 3],
    [2, 3]
])

robot_angle_degrees = 90
robot_angle_radians = np.radians(robot_angle_degrees)

robot_rotation_matrix = np.array([
    [np.cos(robot_angle_radians), -np.sin(robot_angle_radians)],
    [np.sin(robot_angle_radians), np.cos(robot_angle_radians)]
])

robot_scale_matrix = np.array([
    [1, 0],
    [0, 1]
])

robot_transformation_matrix = (
    robot_rotation_matrix @ robot_scale_matrix
)

robot_rotated_points = (
    robot_position @ robot_transformation_matrix.T
)

print("\nPART 3: ROBOT MOVEMENT APPLICATION")
print("Original robot boundary coordinates:")
print(robot_position)

print("\nRobot rotation angle:", robot_angle_degrees, "degrees")
print("Rotated robot boundary coordinates:")
print(np.round(robot_rotated_points, 4))

print("\nInterpretation:")
print("The coordinates show the robot boundary after rotation.")
print("The rotation changes its orientation but preserves its size.")
