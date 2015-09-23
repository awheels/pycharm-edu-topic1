from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0] == 'int(number1)':
        passed()
    else:
        failed("Something is number1.")
    if placeholders[1] == 'int(number2)':
        passed()
    else:
        failed("Something is number2.")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()
