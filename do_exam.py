# coding: utf-8

options = ('A', 'B', 'C', 'D')
all_answers = ['' for i in range(11)]


def check_answers():
    if question2() and question3() and question4() and question5() and question6() and question7() and question8() \
            and question9():
        print(all_answers[1:])


def question2():
    mapper = {'A': 'C', 'B': 'D', 'C': 'A', 'D': 'B'}
    return mapper[all_answers[2]] == all_answers[5]


def question3():
    mapper = {'A': 3, 'B': 6, 'C': 2, 'D': 4}
    diff_number = mapper[all_answers[3]]
    other_number = filter(lambda a: a != diff_number, mapper.values())
    return len(set([all_answers[number] for number in other_number])) == 1 and all_answers[diff_number] != all_answers[
        other_number[0]]


def question4():
    mapper = {'A': (1, 5), 'B': (2, 7), 'C': (1, 9), 'D': (6, 10)}
    number1 = mapper[all_answers[4]][0]
    number2 = mapper[all_answers[4]][1]
    return all_answers[number1] == all_answers[number2]


def question5():
    mapper = {'A': 8, 'B': 4, 'C': 9, 'D': 7}
    return all_answers[5] == all_answers[mapper[all_answers[5]]]


def question6():
    mapper = {'A': (2, 4), 'B': (1, 6), 'C': (3, 10), 'D': (5, 9)}
    number1 = mapper[all_answers[6]][0]
    number2 = mapper[all_answers[6]][1]
    return all_answers[number1] == all_answers[number2] == all_answers[8]


def question7():
    mapper = {'A': 'C', 'B': 'B', 'C': 'A', 'D': 'D'}
    count_list = [all_answers.count(option) for option in options]
    return all_answers.count(mapper[all_answers[7]]) == min(count_list)


def question8():
    mapper = {'A': 7, 'B': 5, 'C': 2, 'D': 10}
    return abs(ord(all_answers[mapper[all_answers[8]]]) - ord(all_answers[1])) != 1


def question9():
    mapper = {'A': 6, 'B': 10, 'C': 2, 'D': 9}
    return (all_answers[1] == all_answers[6]) ^ (all_answers[mapper[all_answers[9]]] == all_answers[5])


def set_question_answer(index):
    if index == 11:
        check_answers()
        return
    for option in options:
        all_answers[index] = option
        set_question_answer(index + 1)


set_question_answer(1)
