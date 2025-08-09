from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.display_question()

while quiz.still_has_questions():
    quiz.display_question()


print("You've completed the quiz.")
print(f"Your final score is {quiz.score} / {quiz.question_number}")