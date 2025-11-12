# from turtle import *
# import colorsys as cs

# # Setup
# width(2)             # Slightly thinner pen for smaller design
# tracer(10)
# bgcolor('black')

# h = 0.2

# for i in range(150):  # Reduced loop count so it fits
#     c = cs.hsv_to_rgb(h, 1, 1)
#     h += 0.005
#     pencolor(c)
#     circle(i / 2, 90)   # Half the original radius
#     forward(15)         # Half the forward step
#     left(100)
#     circle(i / 2, 100)  # Half the original radius
#     forward(150)        # Half the forward step

# done()







from turtle import *
import colorsys as cs

width(4)             # Set pen width
tracer(10)           # Speed up drawing by skipping frames
bgcolor('black')     # Background color

h = 0.2               # Starting hue value
for i in range(300):  # Loop 300 times
    c = cs.hsv_to_rgb(h, 1, 1)  # Convert HSV to RGB color
    h += 0.005                  # Slightly change hue for next loop
    
    pencolor(c)                 # Set pen color
    circle(i, 90)                # Draw partial circle
    forward(30)                  # Move forward
    left(100)                    # Turn left
    circle(i, 100)                # Draw another partial circle
    forward(300)                  # Move forward more

done()
