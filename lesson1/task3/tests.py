from test_helper import run_common_tests, failed, passed, get_file_output

if __name__ == '__main__':
    run_common_tests()
    answer = get_file_output()
    if 'uncomment this' in answer:
        passed()
    else:
        failed()

