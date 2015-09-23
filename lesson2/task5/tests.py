from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0].replace(" ", "").replace("\'", "\"") == '"Bartholomew!"*10':
        passed()
    else:
        failed()


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()
    answer = 'Bartholomew!'*10
    if get_file_output() == [answer]:
        passed()
    else:
        failed('Did you yell it 10 times?')