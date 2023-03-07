import src.calculation as calculation

class TestCal(object):

    @classmethod
    def setup_class(cls):
        cls.cal = calculation.Cal()

    def test_add_num_add_double(self):
        os_name = 'mac'
        if os_name == 'mac':
            print('ls')
        elif os_name == 'window':
            print('dir')
        assert self.cal.add_num_and_double(1, 1) == 4