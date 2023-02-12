from urllib.parse import quote_from_bytes
from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_quesion = Question(q_text = question_text , q_answer = question_answer) 
    question_bank.append(new_quesion)
    
    
quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()
    quiz.check_answer()
    
print("You've completed the quiz")
print(f"your final score was: {quiz.score} / {quiz.question_number}")