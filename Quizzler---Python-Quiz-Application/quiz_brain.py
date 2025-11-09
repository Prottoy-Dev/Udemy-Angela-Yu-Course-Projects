import html


class QuizBrain:

    def __init__(self, q_list):
        """
        Initializes a new QuizBrain object with a list of trivia questions.

        Args:
            q_list (list): A list of Question objects representing the trivia questions.
        """
        self.question_number = 0  # Initialize the question number to zero.
        self.score = 0  # Initialize the player's score to zero.
        self.question_list = q_list  # Store the list of trivia questions.
        self.current_question = None  # Initialize the current_question attribute.

    def still_has_questions(self):
        """
        Checks if there are more questions left to answer.

        Returns:
            bool: True if there are more questions, False otherwise.
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        Retrieves the next trivia question and formats it for display.

        Returns:
            str: The formatted question text.
        """
        self.current_question = self.question_list[self.question_number]  # Get the current question.
        self.question_number += 1  # Increment the question number.
        q_text = html.unescape(self.current_question.text)  # Unescape HTML entities in the question text.
        return f"Q.{self.question_number}: {q_text}"  # Format and return the question.

    def check_answer(self, user_answer):
        """
        Checks if the user's answer matches the correct answer for the current question.

        Args:
            user_answer (str): The user's answer to the question.

        Returns:
            bool: True if the answer is correct, False otherwise.
        """
        correct_answer = self.current_question.answer  # Get the correct answer for the current question.
        if user_answer.lower() == correct_answer.lower():  # Compare user's answer (case-insensitive).
            self.score += 1  # Increment the player's score for a correct answer.
            return True  # Return True if the answer is correct.
        else:
            return False  # Return False if the answer is incorrect.
