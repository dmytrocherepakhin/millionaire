"""
Millionaire
"""
import random
import questions


def menu(num_of_questions, difficulty, question):
    """
    Menu.
    :param num_of_questions:
    :param difficulty:
    :param question:
    :return: None
    """
    global answers
    answer_set = random.sample([0, 1, 2, 3], k=4)
    answer_list = (list(questions.questions_dict[difficulty][question]['answers']['incorrect_answer']))
    answer_list.append(questions.questions_dict[difficulty][question]['answers']['correct_answer'])
    print(f"Запитання №{num_of_questions}: {questions.questions_dict[difficulty][question]['question']}\nВаріанти:")
    option_number = 0
    for i in range(4):
        option_number += 1
        answers[option_number]=answer_list[answer_set[i]]
        print(f"\t{option_number}) {answer_list[answer_set[i]]}")
    for j in range(len(help_me)):
        option_number += 1
        print(f'\t{option_number}) Підказка: {help_me[j]}')
    option_number += 1
    print(f'\t{option_number}) Завершити гру.\n---------------------------')


def get_choice():
    """
    Отримання варіанту відповіді.
    :return: int(new_choice)
    """
    new_choice = None
    while new_choice is None:
        new_choice = input('Відповідь >>> ')
        if new_choice.isdigit() and 0 < int(new_choice) <= (len(help_me) + 5):
            return int(new_choice)
        else:
            print('Invalid choice, try again.')
            new_choice = None


if __name__ == '__main__':

    money = 0
    number_of_questions = 0
    help_me = ['50/50', 'Дзвінок другу', 'Допомога залу']
    questions_easy = list(questions.questions_dict['easy'].keys())
    questions_medium = list(questions.questions_dict['medium'].keys())
    questions_hard = list(questions.questions_dict['hard'].keys())
    answers = {}
    question = None
    answer = None

    print('\t\t\tWelcome!\n >>> Хто хоче стати мільйонером? <<<\n')
    for i in range(15):
        number_of_questions += 1
        if i < 5:
            difficulty = 'easy'
            question = questions_easy.pop(random.randint(0, len(questions_easy) - 1))
            menu(number_of_questions, difficulty, question)

        elif i < 10:
            difficulty = 'medium'
            question = questions_medium.pop(random.randint(0, len(questions_medium) - 1))
            menu(number_of_questions, difficulty, question)

        else:
            difficulty = 'hard'
            question = questions_hard.pop(random.randint(0, len(questions_hard) - 1))
            menu(number_of_questions, difficulty, question)

        choice = get_choice()
        if 0 < choice <= 4:
            print(f'Обрано - {answers[choice]}')
        elif 4 < choice <= (len(help_me) + 4):
            print(f'Обрано - підказка: {help_me[choice - 5]}')
        else:
            print(f'Обрано - Завершити гру.')

        # if

