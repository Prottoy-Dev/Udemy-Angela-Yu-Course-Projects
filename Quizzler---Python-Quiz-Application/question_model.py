"""
Question Class

This class represents a trivia question with text and an associated answer.

Attributes:
    text (str): The text of the trivia question.
    answer (str): The answer to the trivia question.

Methods:
    __init__(self, q_text, q_answer):
        Initializes a new Question object with the provided question text and answer.

Example Usage:
    # Create a new Question object
    question = Question("Is the sky blue?", "True")

    # Access question text and answer
    print(question.text)    # Output: "Is the sky blue?"
    print(question.answer)  # Output: "True"
"""


class Question:

    def __init__(self, q_text, q_answer):
        """
        Initializes a new Question object with the provided question text and answer.

        Args:
            q_text (str): The text of the trivia question.
            q_answer (str): The answer to the trivia question.
        """
        self.text = q_text
        self.answer = q_answer
