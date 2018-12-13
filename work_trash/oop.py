class Car():
    def simple_one(self):
        print('I am a public !')

    def _simple_two(self):
        print('I am 50/50')

    def __private_method(self):
        print('I am private !!!')


auto = Car()
auto.simple_one()
auto._simple_two()
auto._Car__private_method()
