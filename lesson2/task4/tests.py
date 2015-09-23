from test_helper import run_common_tests, failed, passed, get_answer_placeholders


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[1].replace("\'", "\"") == '"hot "' and placeholders[0].replace(" ", "").replace("\'", "\"") == '"grass"+"hopper"' \
            and placeholders[2].replace(" ", "").replace("\'", "\"") == '"l"+"a"+"d"+"y"+"b"+"u"+"g"':
        passed()
    else:
        failed()


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


