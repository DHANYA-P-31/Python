from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for i in question_data:
    question_bank.append(Question(i["text"],i["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still():
    quiz.next_question()

print("Quiz complete")
print(f"Score is: {quiz.score}/{len(question_bank)}")