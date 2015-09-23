from test_helper import run_common_tests, failed, passed, get_answer_placeholders, get_file_output


def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    if placeholders[0].replace("\"", "\'") == "int('12')":
        passed()
    else:
        failed("Did you convert '12' to an integer?.")
    if placeholders[1].replace("\"", "\'") == "float('3.14')":
        passed()
    else:
        failed("Did you convert '3.15' to a float?.")
    if placeholders[2].replace("\"", "\'") == "str(2015)":
        passed()
    else:
        failed("Did you convert 2015 to a string?.")


if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()

