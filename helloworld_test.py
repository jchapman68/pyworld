import helloworld as hw


def test_main():
    assert hw.test_greeting("foobar") == "foobar"

def test_message():
    assert hw.test_greeting("Josh") == "Hello Rob"
