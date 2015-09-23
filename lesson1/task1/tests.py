from test_helper import run_common_tests, failed, passed, get_answer_placeholders

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if (isinstance(placeholders[0], str) and isinstance(int(placeholders[1]), int) and isinstance(float(placeholders[2]), float)):
        passed()
    else:
        failed()


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()
