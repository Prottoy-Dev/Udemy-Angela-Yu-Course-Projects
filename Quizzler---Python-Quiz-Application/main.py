# Import the Question class from the 'question_model' module.
from question_model import Question

# Import the question data from the 'data' module.
from data import question_data

# Import the QuizBrain class from the 'quiz_brain' module.
from quiz_brain import QuizBrain

# Import the QuizInterface class from the 'ui' module.
from ui import QuizInterface

# Create an empty list to store the trivia questions.
question_bank = []

# Iterate through the question data and create Question objects.
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Create a QuizBrain object with the question bank.
quiz = QuizBrain(question_bank)

# Create a QuizInterface to start the quiz.
quiz_ui = QuizInterface(quiz)

# Print a message indicating the quiz is completed.
print("You've completed the quiz")

# Print the final score and the total number of questions.
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
