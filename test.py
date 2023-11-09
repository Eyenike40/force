import main


def test_positive_number():
    """
    The function test the force function by inputting positive mass of the body
    """

    assert main.compute_force(10) == 98.1

    assert main.compute_force(15) == 147.15