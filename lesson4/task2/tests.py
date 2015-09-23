from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    favnum = placeholders[0]
    answers = get_file_output()
    if answers[1] != 'My favourite number is 5':
        passed()
    else:
        failed("Are you sure you changed the value of the variable?")
    if favnum == 'fav_number':
        passed()
    else:
        failed("Did you put the variable, fav_number, in the placeholder?")

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()
