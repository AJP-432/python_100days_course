# Ajlal Paracha -- June 29, 2022

from data import question_data
from quiz_brain import QuizBrain

class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

question_list = [
    Question(question_data[i]["text"], question_data[i]["answer"]) for i in range(len(question_data))
    ]   

quiz = QuizBrain(question_list)
quiz.next_question()

while True: 
    if not quiz.still_has_questions(): break
    quiz.next_question()

print(f"Quiz Complete--Score: {quiz.score}/{quiz.question_number}")
