from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    addition = placeholders[0]
    subtraction = placeholders[1]
    multiplication = placeholders[2]
    division = placeholders[3]
    answers = get_file_output()
    if answers == ['6 6 6 6.0']:
        passed()
    else:
        failed("Check your answers. At least one of them does not equal 6.")
    if '+' in addition:
        passed()
    else:
        failed("Did you use + in your addition?")
    if '-' in subtraction:
        passed()
    else:
        failed("Did you use - in your subtraction?")
    if '*' in multiplication:
        passed()
    else:
        failed("Did you use * in your multiplication?")
    if '/' in division:
        passed()
    else:
        failed("Did you use / in your division?")

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


