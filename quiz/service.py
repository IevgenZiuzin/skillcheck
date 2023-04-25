from quiz.models import Option


def sorted_options(collection):
    """
    :return: dict for user's and right options comparison like:
    {'question_id': [option_id, ...]}
    """
    options = dict()
    for item in collection:
        if isinstance(item, Option):
            question_id = item.question.id
            option_id = item.id
        else:
            question_id = item.option.question.id
            option_id = item.option.id

        if question_id not in options:
            options.setdefault(question_id, [])
        options[question_id].append(option_id)

    return options


def check_question(right_answers, user_answers):
    return set(right_answers) == set(user_answers)


def calculate_result(result):
    percent = round(((result['rights'] / result['total']) * 100))
    rate = round((result['max_score'] * percent / 100))
    return {'percent': percent, 'rate': rate}


def check_quiz(answers_instances):
    quiz = answers_instances[0].option.question.quiz
    query = Option.objects.filter(question__quiz=quiz).filter(is_right=True)
    right_data = sorted_options(query)
    user_data = sorted_options(answers_instances)

    total = len(right_data)
    right = 0

    for question in user_data.keys():
        if check_question(right_data[question], user_data[question]):
            right += 1
    result = {'quiz': quiz, 'category': quiz.category, 'total': total,
              'rights': right, 'max_score': quiz.max_score}
    result.update(calculate_result(result))
    return result
