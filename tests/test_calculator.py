from calculator.routers.calculate import do_operation


def test_calc():
    c = do_operation(1, 2, 'add')
    assert c == 3

