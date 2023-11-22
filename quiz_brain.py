class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.question_list = questions
        self.score = 0


    def still_has_question(self):
        return self.question_number != len(self.question_list)


    def next_question(self):
        current_question = self.question_list[self.question_number]
        user_answer = input(f'Q.{self.question_number + 1}:{current_question.text}. (True or False?)')
        self.question_number += 1
        self.check_answer(user_answer, current_question.answer)


    def check_answer(self, user_answer, right_answer):
       if user_answer == right_answer:
           self.score += 1
       print(f'Your score {self.score}/{len(self.question_list)}')

