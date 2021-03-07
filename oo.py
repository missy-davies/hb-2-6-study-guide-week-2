class Student:
    def __init__(self, firstname, lastname, address):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address


class Question:
    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer


class Exam:

    def __init__(self, name):
        self.questions = []
        self.name = name 
