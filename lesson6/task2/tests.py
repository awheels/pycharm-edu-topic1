from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    swapcase = placeholders[0]
    replace = placeholders[1]
    answers = get_file_output()
    if answers[0] == 'wE WaNt to SWaP THE CAsE Of EACh LettEr':
        passed()
    else:
        failed("Check your use of swapcase().")
    if answers[1] == 'Mr. McBride is the Head of School at Stratford Hall.':
        passed()
    else:
        failed("Mr. McBride is the new head of school. Does that help?")
if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()

