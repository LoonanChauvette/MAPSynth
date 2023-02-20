from src import mapsynth as ms


def test_hello_no_params():
    assert ms.say_hello() == "Hello, World!"

def test_hello_with_params():
    assert ms.say_hello("Bob") == "Hello, Bob!"
