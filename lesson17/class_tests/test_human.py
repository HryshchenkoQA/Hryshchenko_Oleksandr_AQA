from lesson17.code_for_test import Human


class TestHuman:
    def setup_class(self):
        self.human = Human('Alfred', 78, 'grey')
        print("its teardown class")
    def setup(self):
        print('setup for each test')
    def test_check_age(self):

        self.human.grow()
        assert self.human.age == 79
        # assert human.age == 78

    def test_hair_color_change(self):
        self.human = Human('Alfred', 78, 'grey')
        self.human.change_color('black')
        assert self.human.color == 'black'

    def teardown(self):
        print('teardown for each test')

    def teardown_class(self):
        print("its teardown class")
