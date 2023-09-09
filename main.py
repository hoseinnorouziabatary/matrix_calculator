from time import sleep

from matrix import Matrix


A = Matrix()
B = Matrix()


def input_matrix(variable_name):
    variable: Matrix = globals().get(variable_name)

    variable = Matrix()
    row = input("Please enter matrix row count:")
    if not row.isdigit():
        print("Please enter valid number!")
        return
    row = int(row)
    
    col = input("Please enter matrix column count:")
    if not col.isdigit():
        print("Please enter valid number!")
        return
    col = int(col)
    
    print("Please enter matrix elements(separate numbers with space in each line)")
    for _ in range(row):
        row_elements = input()
        row_elements = list(map(int, row_elements.split(' ')))
        if len(row_elements) != col:
            print("Invalid column elements count.")
            return
        variable.rows.append(row_elements)


def print_matrix(variable_name):
    variable: Matrix = globals().get(variable_name)

    variable.print()


def multiply_constant():
    global A
    constant = input("Enter constant value:")
    if not constant.isdigit():
        print("Please enter valid number")
        return
    constant = int(constant)

    A.multiply_constant(constant)


def add():
    global A, B
    if A.row != B.row or A.col != B.col:
        print("Can not add these matrixes!")
        return

    A.add(B)


def minus():
    global A, B
    if A.row != B.row or A.col != B.col:
        print("Can not minus these matrixes!")
        return

    A.minus(B)


def multiply():
    global A, B
    if A.col != B.row:
        print("Can not multiply these matrixes!")
        return

    A.multiply(B)


def divide():
    global A, B
    if A.col != B.row:
        print("Can not divide these matrixes!")
        return

    A.divide(B)


def determinant_matrix(variable_name):
    variable: Matrix = globals().get(variable_name)

    if variable.row != variable.col:
        print("determinant only can be calculated on square matrixes!")
        return

    print(variable.determinant())


option_mapping = {
    1: lambda: input_matrix('A'),
    2: lambda: input_matrix('B'),
    3: lambda: globals().__setitem__('A', B),
    4: lambda: globals().__setitem__('B', A),
    5: multiply,
    6: add,
    7: divide,
    8: minus,
    9: multiply_constant,
    10: lambda: determinant_matrix('A'),
    11: lambda: determinant_matrix('B'),
    12: lambda: print_matrix('A'),
    13: lambda: print_matrix('B')
}


if __name__ == '__main__':
    while True:
        option:str = input(
"""Select an option:
    1. Get Matrix A
    2. Get Matrix B
    3. Move B to A
    4. Move A to B
    5. Calculate A = A * B
    6. Calculate A = A + B
    7. Calculate A = A / B
    8. Calculate A = A - B
    9. Calculate A = a * A
    10. Determinant of A
    11. Determinant of B
    12. Print A
    13. Print B
    14. Close
""")
        if not option.isdigit():
            print("Select a valid number")
            continue
        option = int(option)
        if option > 14 or option < 1:
            print("Select option between 1 and 14")
            continue

        if option == 14:
            print("See you soon. Bye :)")
            break

        option_mapping[option]()

        sleep(1)
