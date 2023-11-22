from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    text = question['text']
    answer = question['answer']
    question_bank.append(Question(text, answer))


def main():
    quiz = QuizBrain(question_bank)

    while quiz.still_has_question():
        quiz.next_question()

    print(f'Your final score {quiz.score}/{len(quiz.question_list)}')


if __name__ == '__main__':
    main()