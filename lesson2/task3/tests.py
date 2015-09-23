from test_helper import run_common_tests, failed, passed, get_file_output


if __name__ == '__main__':
    run_common_tests()
    answer1 = 'I am 5\'10" tall'
    answer2 = 'Mr. Wheeler\t5\'10"'
    answer3 = 'Greg Smith\t6\'2"'
    answer4 = 'Emily Irk\t5\'5"'
    print(get_file_output())
    if (get_file_output() == [answer1, answer2, answer3, answer4, ''] or get_file_output() == [answer1, answer2, answer3, answer4] ) :
        passed()
    else:
        failed('Some of your escape sequences are incorrect.')
