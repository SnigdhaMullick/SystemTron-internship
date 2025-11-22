import tkinter as tk
import time
import math

# ----------------------------------------
#   Creating the main window
# ----------------------------------------
window = tk.Tk()
window.title("Analog Clock")
window.geometry("400x400")

# ----------------------------------------
#   Canvas Setup
# ----------------------------------------
canvas = tk.Canvas(window, width=400, height=400, bg="black")
canvas.pack(expand=True, fill="both")

# Load the clock background image
clock_bg = tk.PhotoImage(file="clock.png")
canvas.create_image(200, 200, image=clock_bg)

# Clock center coordinates (middle of the canvas)
center_x = 200
center_y = 200

# Lengths of the three hands
second_hand_length = 95
minute_hand_length = 80
hour_hand_length = 60

# Creating the hands on the clock
second_hand = canvas.create_line(center_x, center_y,
                                 center_x, center_y - second_hand_length,
                                 width=1.5, fill="red")

minute_hand = canvas.create_line(center_x, center_y,
                                 center_x, center_y - minute_hand_length,
                                 width=2, fill="white")

hour_hand = canvas.create_line(center_x, center_y,
                               center_x, center_y - hour_hand_length,
                               width=4, fill="white")


# ----------------------------------------
#   Update Clock Every Second
# ----------------------------------------
def update_clock():
    """Moves each hand of the clock according to the current time."""

    # Fetch current hour, minute, second
    hours = int(time.strftime("%I"))
    minutes = int(time.strftime("%M"))
    seconds = int(time.strftime("%S"))

    # ----- Second Hand -----
    sec_angle = math.radians(seconds * 6)
    sec_x = center_x + second_hand_length * math.sin(sec_angle)
    sec_y = center_y - second_hand_length * math.cos(sec_angle)
    canvas.coords(second_hand, center_x, center_y, sec_x, sec_y)

    # ----- Minute Hand -----
    min_angle = math.radians(minutes * 6)
    min_x = center_x + minute_hand_length * math.sin(min_angle)
    min_y = center_y - minute_hand_length * math.cos(min_angle)
    canvas.coords(minute_hand, center_x, center_y, min_x, min_y)

    # ----- Hour Hand (moves smoothly using minutes & seconds) -----
    hour_angle = math.radians(hours * 30 + minutes * 0.5 + seconds * 0.008)
    hour_x = center_x + hour_hand_length * math.sin(hour_angle)
    hour_y = center_y - hour_hand_length * math.cos(hour_angle)
    canvas.coords(hour_hand, center_x, center_y, hour_x, hour_y)

    # Call this function again after 1 second
    window.after(1000, update_clock)


# Start the clock animation
update_clock()

window.mainloop()
