def log_test(fn):
    ''' Log test decorator - curry for number of sub tests to print
    Example:
        @log_test_with(1)
        def print_hi():
        # ▶️ Asserting 1 "print hi"

    '''
    is_header_log = isinstance(fn, str) or fn.__name__.startswith('Test')
    name = fn if isinstance(fn, str) else fn.__name__.replace("_", " ")
    if is_header_log:
        print('\n==================================\n')

    prefix = '📌' if is_header_log else f"▶️"
    message = f'{prefix} Asserting "{name}"'
    print(message)
    return fn


def log_test_with(tests_number=0):
    ''' Log test decorator - curry for number of sub tests to print
    Example:
        @log_test_with(1)
        def print_hi():
        # ▶️ Asserting 1 "print hi"

    '''
    def log_test(fn):
        message = f'▶️ Asserting {tests_number} "{fn.__name__.replace("_", " ")}"'
        print(message)
        return fn

    return log_test
