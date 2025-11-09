# Pomodoro GUI Application Documentation

# Import the tkinter library, which provides tools for creating a GUI.
from tkinter import *

# Import the math module for mathematical operations (used for time formatting).
import math

# ---------------------------- CONSTANTS ------------------------------- #

# Define color constants for the UI.
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

# Define the font name for the timer display.
FONT_NAME = "Courier"

# Define the default durations for work, short breaks, and long breaks (in minutes).
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20

# Initialize a counter to keep track of work sessions.
rep = 0

# Initialize a variable to manage the countdown timer.
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

# Define a function to reset the timer and session counter.
def reset_timer():
    # Cancel any ongoing timer.
    window.after_cancel(timer)
    # Reset the timer display text.
    timer_txt.config(text="Timer")
    # Clear the checkmarks.
    check_mark.config(text="")
    # Reset the timer canvas to "00:00."
    canvas.itemconfigure(time, text="00:00")
    # Reset the session counter.
    global rep
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

# Define a function to start the Pomodoro timer.
def start_timer():
    # Access the global session counter.
    global rep
    # Increment the session counter.
    rep += 1
    # Calculate the duration of work, short break, and long break sessions in seconds.
    WORK_sec = WORK_MIN * 60
    SHORT_BREAK_sec = SHORT_BREAK_MIN * 60
    LONG_BREAK_sec = LONG_BREAK_MIN * 60
    # Check if it's time for a long break (every 8 work sessions).
    if rep % 8 == 0:
        # Update the timer display and set the text color to red for a long break.
        timer_txt.config(text="Break", fg=RED)
        # Start the countdown for a long break.
        count_down(LONG_BREAK_sec)
    # Check if it's time for a short break (every 2 work sessions).
    elif rep % 2 == 0:
        # Update the timer display and set the text color to pink for a short break.
        timer_txt.config(text="Break", fg=PINK)
        # Start the countdown for a short break.
        count_down(SHORT_BREAK_sec)
    else:
        # Update the timer display and set the text color to green for work.
        timer_txt.config(text="Work", fg=GREEN)
        # Start the countdown for a work session.
        count_down(WORK_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# Define a function for the countdown mechanism.
def count_down(count):
    # Access the global timer variable.
    global timer
    # Calculate minutes and seconds from the provided count (in seconds).
    minute = math.floor(count / 60)
    sec = count % 60
    # Format seconds to include leading zeros if less than 10.
    if sec < 10:
        sec = f"0{sec}"
    # Update the timer canvas with the formatted time.
    canvas.itemconfigure(time, text=f"{minute}:{sec}")
    # If the countdown is not yet completed:
    if count > 0:
        # Schedule the function to run again in 1000 milliseconds (1 second).
        timer = window.after(1000, count_down, count - 1)
    else:
        # When the countdown reaches zero, start the next session.
        start_timer()
        # Initialize an empty string to track completed work sessions.
        mark = ""
        # Calculate the number of work sessions completed.
        work_session = math.floor(rep / 2)
        # Add a checkmark for each completed work session.
        for x in range(work_session):
            mark += "✔"
        # Update the checkmarks.
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

# Create the main application window.
window = Tk()

# Set the window title.
window.title("Pomodoro")

# Configure padding and background color for the window.
window.config(padx=100, pady=50, bg=YELLOW)

# Create a label for the timer display with specified properties.
timer_txt = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 60, "bold"), highlightthickness=0)

# Place the timer label in the grid layout.
timer_txt.grid(column=1, row=0)

# Create a canvas for visualizing the timer using a tomato image.
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)

# Create a text element in the canvas for displaying the time.
time = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Place the canvas in the grid layout.
canvas.grid(column=1, row=1)

# Create a "Start" button with a specified command to start the timer.
start_button = Button(text="Start", highlightthickness=0, command=start_timer)

# Place the "Start" button in the grid layout.
start_button.grid(column=0, row=2)

# Create a "Reset" button with a specified command to reset the timer.
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)

# Place the "Reset" button in the grid layout.
reset_button.grid(column=2, row=2)

# Create a label for displaying checkmarks to track completed work sessions.
check_mark = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))

# Place the checkmark label in the grid layout.
check_mark.grid(column=1, row=3)

# Start the main application loop.
window.mainloop()
