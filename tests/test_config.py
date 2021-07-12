import pytest


# Function to raise an customize error i.e error which will pop up when input will be out
# of the range.
class NotInRange(Exception):
    def __init__(self, message="value not in range"):
        self.message = message
        super().__init__(self.message)


def test_generic():
    a = 5
    with pytest.raises(NotInRange):
        if a not in range(10, 20):
            raise NotInRange


# Its a convention, it's compulsory to include test_XXX in from of any function, otherwise it won't consider it as a test case

def something():
    a = 5
    b = 5
    assert True


def test_something():
    a = 5
    b = 5
    assert True
