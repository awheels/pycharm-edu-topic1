from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0].replace(" ", "") == "x*=10":
        passed()
    else:
        failed("Did you increase by a factor of 10?.")
    if placeholders[1].replace(" ", "") == "y-=3":
        passed()
    else:
        failed("Did you decrease by 3?.")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()
