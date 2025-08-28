import random
import questions

for i in range(10):
    print(random.sample([1, 2, 3, 4], k=4))

l = (list(questions.questions_dict['easy'][1]['answers']['incorrect_answer']))
l.append(questions.questions_dict['easy'][1]['answers']['correct_answer'])
print(l)

answer_set = random.sample([0, 1, 2, 3], k=4)
answer_list = (list(questions.questions_dict['easy'][1]['answers']['incorrect_answer']))
answer_list.append(questions.questions_dict['easy'][1]['answers']['correct_answer'])
print(f"Запитання №1: {questions.questions_dict['easy'][1]['question']}\n\tВаріанти:\n")
for i in range(4):
    print(f"{i+1}) {answer_list[answer_set[i]]}"'')


questions_easy = list(questions.questions_dict['easy'].keys())
questions_medium = questions.questions_dict['medium'].keys()
questions_hard = questions.questions_dict['hard'].keys()

print(questions_easy)
print(questions_medium)
print(questions_hard)