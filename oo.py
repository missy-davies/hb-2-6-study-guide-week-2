class Student(object):
    """Student information"""

    def __init__(self, firstname, lastname, address):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address


class Question(object):
    """A question in an exam"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer


    def ask_and_evaluate(self):
        """Print the question to the console and prompt the user for an answer"""

        print(self.question)
        guess = input("> ")

        return guess == self.correct_answer
    

class Exam(object):
    """An exam is a test.

    Exams have zero or more questions"""

    def __init__(self, name):
        self.questions = []
        self.name = name 


    def add_question(self, question):
        """Add a question to the exam"""

        self.questions.append(question)


    def administer(self):
        """Administer an exam and keep track of the score"""

        score = 0

        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1

        return round(100 * (float(score) / len(self.questions)), 2)