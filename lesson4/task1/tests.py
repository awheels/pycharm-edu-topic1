from test_helper import run_common_tests, failed, passed, get_answer_placeholders

def test_answer_placeholders():
    placeholders = get_answer_placeholders()
    fruit = placeholders[0]
    number = placeholders[1]
    cost = placeholders[2]
    sick = placeholders[3]

    if isinstance(fruit, str):
        passed()
    else:
        failed("Is your fruit a string?")

    if '.' in number:
        failed("The number of fruit should be an integer and not a float.")
    else:
        try:
            int(number)
            passed()
        except ValueError:
            failed("Something is wrong with your integer.")

    if '.' in cost:
        try:
            float(cost)
            passed()
        except ValueError:
            failed("Something is wrong with your float.")
    else:
        failed("The cost should be a float.")

    if sick == "True":
        passed()
    elif sick == "False":
        passed()
    else:
        failed("Your boolean value should be True or false (it is important that they are capitalized).")

if __name__ == '__main__':
    run_common_tests()
    test_answer_placeholders()


