def handle(email):
    handle.count += 1
    assert handle.count == 1


handle.count = 0
