# Import necessary libraries for creating a graphical user interface (GUI) and managing the quiz.
from tkinter import *
from quiz_brain import QuizBrain

# Define a theme color for the GUI.
THEME_COLOR = "#375362"

# Create a class called QuizInterface to manage the quiz application.
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        """
        Initializes the QuizInterface.

        Args:
            quiz_brain (QuizBrain): An object that controls the quiz.
        """
        self.quiz = quiz_brain  # Store the quiz brain for later use.
        self.window = Tk()  # Create the main window for the quiz app.
        self.window.title("Quizzler")  # Set the window title.
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)  # Configure window padding and background color.

        # Create a label to show the player's score.
        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)  # Place the label in the window.

        # Create a canvas for displaying trivia questions.
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Create buttons for answering questions.
        wrong_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_image, highlightthickness=0, command=self.wrong)
        self.wrong_button.grid(column=1, row=2)

        right_image = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_image, highlightthickness=0, command=self.right)
        self.right_button.grid(column=0, row=2)

        # Start the quiz by displaying the first question.
        self.get_next_question()

        # Start the main GUI loop.
        self.window.mainloop()

    def get_next_question(self):
        """
        Gets the next question from the quiz and updates the interface.
        """
        self.canvas.config(bg="white")  # Clear the background color.
        if self.quiz.still_has_questions():  # Check if there are more questions.
            self.score_label.config(text=f"Score: {self.quiz.score}/10")  # Update the score label.
            q_text = self.quiz.next_question()  # Get the next question text.
            self.canvas.itemconfig(self.question_text, text=q_text)  # Update the question text.
        else:
            self.canvas.itemconfig(self.question_text, text="Quiz Over")  # Show "Quiz Over" when no more questions.
            self.right_button.config(state="disabled")  # Disable the right button.
            self.wrong_button.config(state="disabled")  # Disable the wrong button.

    def right(self):
        """
        Handles the logic when the 'True' button is clicked.
        """
        self.get_feedback(self.quiz.check_answer("True"))

    def wrong(self):
        """
        Handles the logic when the 'False' button is clicked.
        """
        self.get_feedback(self.quiz.check_answer("False"))

    def get_feedback(self, ans):
        """
        Provides feedback based on the answer and schedules the next question.

        Args:
            ans (bool): True if the answer is correct, False otherwise.
        """
        if ans:
            self.canvas.config(bg="Green")  # Set the canvas background to green for a correct answer.
        else:
            self.canvas.config(bg="Red")  # Set the canvas background to red for a wrong answer.
        # Schedule the next question to be displayed after a delay of 1 second.
        self.window.after(1000, self.get_next_question)
