def reverse_string(string):
    return string[::-1]


def test_reverse_string():
    test_string = "hello"
    assert reverse_string(test_string) == "olleh"


class Cat:
    def meow(self):
        return "meow, meow"


def test_cat():
    cat = Cat()
    assert cat


def test_cat_():
    cat = Cat()
    assert cat.meow() == "meow, meow"
