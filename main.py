#file import
from data import question_data 
from quiz_brain import QuizBrain
from question_model import Question

question_bank = []
for question in question_data:
    q_text = question["text"]
    q_answer = question["answer"]
    new_question = Question(q_text,q_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

still_has_question = True

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")




