class Student(object):
    """Student information"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address


class Question(object):
    """A question in an exam"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer


    def ask_and_evaluate(self):
        """Print the question to the console and prompt the user for an answer"""

        answer = input(self.question + " > ")

        return self.correct_answer == answer
    

class Exam(object):
    """An exam is a test.

    Exams have zero or more questions"""

    def __init__(self, name):
        self.name = name 
        self.questions = []


    def add_question(self, question):
        """Add a question to the exam"""

        self.questions.append(question)


    def administer(self):
        """Administer an exam and keep track of the score"""

        score = 0

        for question in self.questions:
            if question.ask_and_evaluate():
                score += 1

        return 100 * (float(score) / len(self.questions))


class StudentExam(object):
     """Store information for a student, an exam, and the student’s score 
     for that exam"""

     def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = None


     def take_test(self):
        """Administer an exam and save the student score"""

        self.score = self.exam.administer()

        print(f"Your score is {self.score:.2f} percent")


def example():
    """Create an exam with questions, create a student, and administer the test"""

    exam = Exam('midterm')

    ct_q = Question(
        'What is the capital of Connecticut?',
        'Hartford')
    exam.add_question(ct_q)

    ma_q = Question(
        'What is the capital of Massachusetts?',
        'Boston')
    exam.add_question(ma_q)

    ny_q = Question(
        'What is the capital of New York?',
        'Albany')
    exam.add_question(ny_q)

    student = Student(
        'Missy',
        'Davies',
        '42 Travel Street')

    missy_midterm = StudentExam(student, exam)

    missy_midterm.take_test()
