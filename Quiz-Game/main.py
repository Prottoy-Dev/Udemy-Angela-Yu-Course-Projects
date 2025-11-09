"""
Quiz Game Main Script

This script orchestrates the execution of a quiz game. It imports question data, creates question instances,
initializes a quiz engine, and conducts the quiz by presenting questions to the user.

Usage:
    Run this script to initiate the quiz game. The script loads questions from the data source, processes
    them into question instances, and then starts presenting the questions to the user. After the quiz
    is complete, the user's final score is displayed.

Dependencies:
    - data: A module that provides the question_data list, containing question texts and answers.
    - question_model: A module containing the Question class for representing questions and answers.
    - quiz_brain: A module containing the QuizBrain class responsible for managing the quiz process.

Note:
    Before running the script, ensure that the required modules (data, question_model, quiz_brain) are
    present and correctly defined in the same directory.

"""
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []
for x in question_data:
    question_text = x["text"]
    question_answer = x["answer"]
    question = Question(question_text, question_answer)
    question_bank.append(question)
quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()
print(f"Your final score is {quiz.score}/{quiz.question_number} ")

