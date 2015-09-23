from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    placeholder = placeholders[0]
    placeholder2 = placeholders[1]
    if 'name' in placeholder:
        passed()
    else:
        failed()
    if '?' in placeholder and '?' in placeholder2:
        passed()
    else:
        failed()
    if placeholder.startswith('input('):
        passed()
    else:
        failed()
    if placeholder2.startswith('age =') or placeholder.startswith('age=') :
        passed()
    else:
        failed()

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()
