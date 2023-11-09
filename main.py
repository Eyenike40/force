def main():
    """
    The main program
    """
    mass = get_object_mass()
    force = compute_force(mass)
    print(f"The force of the body = {force:,.2f}N")


def get_object_mass():
    """
    This function get the mass of the object

    Paramters
    ---------
    None

    Return
    ------
    It return the mass of the object
    """

    while True:
        try:
            return float(input("Enter the mass of the body (Kg) : "))
        except ValueError:
            print("Enter a valid number : ")


def compute_force(mass: float):
    """
    This function compute the force of a body

    Parameter
    ---------
    The mass of a body

    Return
    ------
    The force of the body
    """
    acceleration = 9.81

    return acceleration * mass


def convert_force(force):
    """
    A function to convert the force of an about
    """

    return force * 2/3


if "__main__" == __name__:
    main()