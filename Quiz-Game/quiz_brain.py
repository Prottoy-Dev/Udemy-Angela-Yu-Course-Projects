class QuizBrain:
    """
        A class for managing a quiz, keeping track of questions, user answers, and scores.

        Attributes:
            question_number (int): The current question number.
            question_list (list): A list of Question instances representing the quiz questions.
            score (int): The user's current score.

    """

    def __init__(self, q_list):
        """
            Initializes a new QuizBrain instance.

            Args:
                q_list (list): A list of Question instances representing the quiz questions.

        """
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        """
            Checks if there are more questions remaining in the quiz.

            Returns:
                bool: True if there are more questions, False otherwise.

        """
        if self.question_number < len(self.question_list):
            return True

    def next_question(self):
        """
            Presents the next question to the user and checks their answer.

            Displays the question text, prompts the user for an answer, and updates the score.

        """
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        """
            Compares the user's answer to the correct answer and updates the score.

            Args:
                user_answer (str): The user's answer (True or False).
                correct_answer (str): The correct answer for the current question.

        """
        if user_answer == correct_answer:
            print("You got it right!")
            self.score += 1

        else:
            print("You got it wrong")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")
