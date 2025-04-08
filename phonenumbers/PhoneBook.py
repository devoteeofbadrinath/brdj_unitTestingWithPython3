class PhoneBook:
    def __init__(self):
        self.numbers = {}

    def add(self, name, number):
        self.numbers[name] = number

    def lookup(self, name):
        return self.numbers[name]

    def is_consistent(self):
        for key1, value1 in self.numbers.items():
            for key, value in self.numbers.items():
                if key1 == key:
                    continue
                if value1.startswith(value):
                    return False
        return True

    def get_names(self):
        return self.numbers.keys()

    def get_numbers(self):
        return self.numbers.values()


