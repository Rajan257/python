# # from vpython import *

# # # Create a scene
# # scene = canvas(title='3D Coordinate System with Rotation',
# #                width=800, height=600,
# #                center=vector(0,0,0), background=color.black)

# # # Create axes
# # x_axis_pos = arrow(pos=vector(0,0,0), axis=vector(2,0,0), color=color.red)
# # x_axis_neg = arrow(pos=vector(0,0,0), axis=vector(-2,0,0), color=color.red)

# # y_axis_pos = arrow(pos=vector(0,0,0), axis=vector(0,2,0), color=color.yellow)
# # y_axis_neg = arrow(pos=vector(0,0,0), axis=vector(0,-2,0), color=color.yellow)

# # z_axis_pos = arrow(pos=vector(0,0,0), axis=vector(0,0,2), color=color.blue)
# # z_axis_neg = arrow(pos=vector(0,0,0), axis=vector(0,0,-2), color=color.blue)

# # # Labels
# # label(pos=vector(2.2,0,0), text='X+', box=False, color=color.white)
# # label(pos=vector(-2.2,0,0), text='X-', box=False, color=color.white)
# # label(pos=vector(0,2.2,0), text='Y+', box=False, color=color.white)
# # label(pos=vector(0,-2.2,0), text='Y-', box=False, color=color.white)
# # label(pos=vector(0,0,2.2), text='Z+', box=False, color=color.white)
# # label(pos=vector(0,0,-2.2), text='Z-', box=False, color=color.white)

# # # Create a cube
# # cube_obj = box(pos=vector(1,0,0), size=vector(0.5,0.5,0.5), color=color.red)

# # # Create a cone (similar to your pyramid shape)
# # cone_obj = cone(pos=vector(0,0,1), axis=vector(0.5,0,0), radius=0.3, color=color.magenta)

# # # Animation loop
# # while True:
# #     rate(60)  # 60 frames per second
# #     cube_obj.rotate(angle=0.02, axis=vector(0,1,0), origin=vector(0,0,0))
# #     cone_obj.rotate(angle=0.02, axis=vector(0,1,0), origin=vector(0,0,0))































































# from vpython import *

# # Create scene
# scene = canvas(
#     title='3D Coordinate System (Interactive)',
#     width=800, height=600,
#     center=vector(0, 0, 0),
#     background=color.black
# )
# scene.forward = vector(-1, -1, -1)  # Initial camera angle

# # Function to create axis arrows
# def create_axes(length=2):
#     # X-axis
#     arrow(pos=vector(0,0,0), axis=vector(length,0,0), color=color.red)
#     arrow(pos=vector(0,0,0), axis=vector(-length,0,0), color=color.red)
#     label(pos=vector(length+0.2,0,0), text='X+', box=False, color=color.white)
#     label(pos=vector(-length-0.2,0,0), text='X-', box=False, color=color.white)

#     # Y-axis
#     arrow(pos=vector(0,0,0), axis=vector(0,length,0), color=color.yellow)
#     arrow(pos=vector(0,0,0), axis=vector(0,-length,0), color=color.yellow)
#     label(pos=vector(0,length+0.2,0), text='Y+', box=False, color=color.white)
#     label(pos=vector(0,-length-0.2,0), text='Y-', box=False, color=color.white)

#     # Z-axis
#     arrow(pos=vector(0,0,0), axis=vector(0,0,length), color=color.blue)
#     arrow(pos=vector(0,0,0), axis=vector(0,0,-length), color=color.blue)
#     label(pos=vector(0,0,length+0.2), text='Z+', box=False, color=color.white)
#     label(pos=vector(0,0,-length-0.2), text='Z-', box=False, color=color.white)

# # Create the coordinate axes
# create_axes()

# # Create objects
# cube_obj = box(pos=vector(1,0,0), size=vector(0.5,0.5,0.5), color=color.red)
# cone_obj = cone(pos=vector(0,0,1), axis=vector(0.5,0,0), radius=0.3, color=color.magenta)

# # Animation loop
# while True:
#     rate(60)  # Limit frame rate
#     # No need to rotate axes; user can rotate view with mouse
#     pass









































# from vpython import *

# # Create scene
# scene = canvas(title='Interactive 3D Coordinate System',
#                width=800, height=600,
#                center=vector(0, 0, 0), background=color.black)

# # Axes
# x_axis_pos = arrow(pos=vector(0, 0, 0), axis=vector(2, 0, 0), color=color.red)
# x_axis_neg = arrow(pos=vector(0, 0, 0), axis=vector(-2, 0, 0), color=color.red)
# y_axis_pos = arrow(pos=vector(0, 0, 0), axis=vector(0, 2, 0), color=color.yellow)
# y_axis_neg = arrow(pos=vector(0, 0, 0), axis=vector(0, -2, 0), color=color.yellow)
# z_axis_pos = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, 2), color=color.blue)
# z_axis_neg = arrow(pos=vector(0, 0, 0), axis=vector(0, 0, -2), color=color.blue)

# # Labels
# label(pos=vector(2.2, 0, 0), text='X+', box=False, color=color.white)
# label(pos=vector(-2.2, 0, 0), text='X-', box=False, color=color.white)
# label(pos=vector(0, 2.2, 0), text='Y+', box=False, color=color.white)
# label(pos=vector(0, -2.2, 0), text='Y-', box=False, color=color.white)
# label(pos=vector(0, 0, 2.2), text='Z+', box=False, color=color.white)
# label(pos=vector(0, 0, -2.2), text='Z-', box=False, color=color.white)

# # Objects
# cube_obj = box(pos=vector(1, 0, 0), size=vector(0.5, 0.5, 0.5), color=color.red)
# cone_obj = cone(pos=vector(0, 0, 1), axis=vector(0.5, 0, 0), radius=0.3, color=color.magenta)

# # Track mouse drag
# dragging = False
# prev_mouse_pos = None

# def on_mousedown(evt):
#     global dragging, prev_mouse_pos
#     dragging = True
#     prev_mouse_pos = evt.pos

# def on_mouseup(evt):
#     global dragging
#     dragging = False

# def on_mousemove(evt):
#     global prev_mouse_pos
#     if dragging:
#         dx = evt.pos.x - prev_mouse_pos.x
#         dy = evt.pos.y - prev_mouse_pos.y
#         angle_x = dy * 0.01
#         angle_y = dx * 0.01
#         for obj in [x_axis_pos, x_axis_neg, y_axis_pos, y_axis_neg, z_axis_pos, z_axis_neg]:
#             obj.rotate(angle=angle_x, axis=vector(1, 0, 0), origin=vector(0, 0, 0))
#             obj.rotate(angle=angle_y, axis=vector(0, 1, 0), origin=vector(0, 0, 0))
#         prev_mouse_pos = evt.pos

# scene.bind('mousedown', on_mousedown)
# scene.bind('mouseup', on_mouseup)
# scene.bind('mousemove', on_mousemove)

# while True:
#     rate(60)
















import pygame
import math
import sys

pygame.init()

# Window setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Coordinate System - Fast Mouse Rotation")
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 3D points of coordinate system
axis_points = [
    (0, 0, 0), (200, 0, 0),   # X axis
    (0, 0, 0), (0, 200, 0),   # Y axis
    (0, 0, 0), (0, 0, 200)    # Z axis
]

def rotate_x(point, angle):
    x, y, z = point
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    y2 = y * cos_a - z * sin_a
    z2 = y * sin_a + z * cos_a
    return (x, y2, z2)

def rotate_y(point, angle):
    x, y, z = point
    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    z2 = z * cos_a - x * sin_a
    x2 = z * sin_a + x * cos_a
    return (x2, y, z2)

def project(point):
    x, y, z = point
    factor = 500 / (z + 500)
    x_proj = x * factor + WIDTH / 2
    y_proj = -y * factor + HEIGHT / 2
    return (int(x_proj), int(y_proj))

rotation_x = 0
rotation_y = 0

# Hide mouse and lock it to center
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

while True:
    mouse_dx, mouse_dy = pygame.mouse.get_rel()  # Mouse movement delta

    # Increase speed multiplier
    rotation_y += mouse_dx * 0.1
    rotation_x += mouse_dy * 0.1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(WHITE)

    # Draw axes
    for i in range(0, len(axis_points), 2):
        p1 = rotate_x(axis_points[i], rotation_x)
        p1 = rotate_y(p1, rotation_y)
        p2 = rotate_x(axis_points[i + 1], rotation_x)
        p2 = rotate_y(p2, rotation_y)

        p1_proj = project(p1)
        p2_proj = project(p2)

        color = RED if i == 0 else GREEN if i == 2 else BLUE
        pygame.draw.line(screen, color, p1_proj, p2_proj, 3)

    pygame.display.flip()
    clock.tick(60)
