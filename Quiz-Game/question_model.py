class Question:
    """
        A class representing a question and its corresponding answer.

        Attributes:
            text (str): The text of the question.
            answer (str): The answer to the question.
        """
    def __init__(self, q_text, q_answer):
        """
                Initializes a new Question instance.

                Args:
                    q_text (str): The text of the question.
                    q_answer (str): The answer to the question.
                """
        self.text = q_text
        self.answer = q_answer
