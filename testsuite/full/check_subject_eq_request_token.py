def check(email, arg1, test_kwarg=0):
    assert arg1 == 'arg1'
    assert test_kwarg == 1

    return email.subject.lower().split() == ['request', 'token']
