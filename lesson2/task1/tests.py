from test_helper import run_common_tests, failed, passed, get_file_output

if __name__ == '__main__':
    run_common_tests()
    answer = 'Mr. Wheeler has "great" hair.'
    if get_file_output() == [answer]:
        passed()
    else:
        failed('Did you copy the same message?')
