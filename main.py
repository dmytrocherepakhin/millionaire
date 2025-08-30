"""
Millionaire game
"""
import random
import questions


def menu(num_of_questions, difficulty_, question_):
    """
    Menu function.
    :param num_of_questions:
    :param difficulty_:
    :param question_:
    :return: None
    """
    global answers
    global answer_set
    if is_fifty_fifty:
        answers = {}
        answer_set = random.sample([0, 1], k=2)
        answer_list = [(list(questions.questions_dict[difficulty_][question_]['answers']['incorrect_answer']))[
                           random.randint(0, 2)],
                       questions.questions_dict[difficulty_][question_]['answers']['correct_answer']]
    elif helping:
        answer_list = list(answers.values())
    else:
        answer_set = random.sample([0, 1, 2, 3], k=4)
        answer_list = list(questions.questions_dict[difficulty_][question_]['answers']['incorrect_answer'])
        answer_list.append(questions.questions_dict[difficulty_][question_]['answers']['correct_answer'])
    print(f"\nЗапитання №{num_of_questions}: {questions.questions_dict[difficulty_][question_]['question']}\nВаріанти:")
    option_number = 0
    for j in range(len(answer_list)):
        option_number += 1
        answers[option_number] = answer_list[answer_set[j]]
        print(f"\t{option_number}) {answer_list[answer_set[j]]}")
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
        if new_choice.isdigit() and 0 < int(new_choice) <= (len(help_me) + (len(answers) + 1)):
            return int(new_choice)
        else:
            print('Invalid choice, try again.')
            new_choice = None


def call_to_friend():
    """
    Call to friend function.
    :return: None
    """
    friend_answer = answers[random.randint(1, len(answers) )]
    print(f'>>> Друг пропонує відповідь ---> "{friend_answer}"')


def help_of_studio():
    """
    Help of studio function.
    :return: None
    """
    votes = []
    for v in range(len(answers)):
        votes.append(random.randint(0, 100))
    new_votes = []
    for nv in votes:
        new_votes.append(round(nv / sum(votes) * 100))
    print(f'>>> Студія проголосувала за варіанти:\n ')
    for k in range(len(new_votes)):
        print(f'{answers[k + 1]} - {new_votes[k]}%')


if __name__ == '__main__':

    money = 0
    unburned_money = 0
    number_of_questions = 0
    help_me = ['50/50', 'Дзвінок другу', 'Допомога залу']
    questions_easy = list(questions.questions_dict['easy'].keys())
    questions_medium = list(questions.questions_dict['medium'].keys())
    questions_hard = list(questions.questions_dict['hard'].keys())
    answers = {}
    question = None
    answer = None
    difficulty = ''
    helping = ''
    is_fifty_fifty = False
    answer_set = []

    print('\t\t\tWelcome!\n >>> Хто хоче стати мільйонером? <<<')
    for i in range(15):
        if helping:
            i -= i
            match helping:
                case '50/50':
                    is_fifty_fifty = True
                case 'Дзвінок другу':
                    call_to_friend()
                case 'Допомога залу':
                    help_of_studio()
            menu(number_of_questions, difficulty, question)
            helping = ''
            is_fifty_fifty = False
        else:
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
        if 0 < choice <= len(answers):
            print(f'Обрано - {answers[choice]}')
        elif len(answers) < choice <= (len(help_me) + len(answers)):
            print(f'Обрано - підказка: {help_me[choice - len(answers) - 1]}')
            helping = help_me.pop(choice - len(answers) - 1)
            continue
        else:
            print(f'Обрано - Завершити гру.\n\tГРУ ЗАВЕРШЕНО\n\tВи заробили {money} грн')
            break

        if answers[choice] == questions.questions_dict[difficulty][question]['answers']['correct_answer']:
            money = questions.money_for_question[number_of_questions]
            if number_of_questions == 5 or number_of_questions == 10 or number_of_questions == 15:
                unburned_money = questions.money_for_question[number_of_questions]
            print(f'Ви заробили {money} грн.')
        else:
            print('\tНЕВІРНА ВІДПОВІДЬ')
            print(f'\tВи заробили {unburned_money} грн.')
            break
