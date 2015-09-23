from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    exponent1 = placeholders[0]
    exponent2 = placeholders[1]
    answers = get_file_output()
    if answers == ['16 16']:
        passed()
    else:
        failed("Check your answers. At least one of them does not equal 16.")
    if '**' in exponent1:
        passed()
    else:
        failed("Did you use ** in exponent1?")
    if '**' in exponent2:
        passed()
    else:
        failed("Did you use ** in exponent2?")

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()
