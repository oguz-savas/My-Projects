class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


question_list = [
    {"text": "Is Python a Programming language?", "answer": "Yes"},
    {"text": "Is Python an OOP language?", "answer": "Yes"},
    {"text": "Which Programming Language is essential for Machine Learning?", "answer": "Python"},
    {"text": "Is Gemini an LLM?", "answer": "Yes"},
    {"text": "Are classes a subject of Python?", "answer": "Yes"}
]

question_bank = []
for q in question_list:
    question_bank.append(Question(q["text"], q["answer"]))


class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1

        user_answer = input(
            f"{self.question_number}. Question: {current_question.text}: "
        )

        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("✅ Correct")
        else:
            print("❌ Wrong")

        print(f"Score: {self.score}/{self.question_number}\n")


quiz = QuizBrain(question_bank)

while quiz.question_number < len(quiz.question_list):
    quiz.next_question()

print("Quiz is finished 🎉")
print(f"Your Final Score: {quiz.score}/{len(quiz.question_list)}")
