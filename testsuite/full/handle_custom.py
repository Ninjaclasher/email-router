def handle(email):
    handle.count += 1
    if handle.count == 1:
        assert 'Request' in email.subject
    elif handle.count == 2:
        assert 'github' in email.body.lower()
    else:
        assert False


handle.count = 0
