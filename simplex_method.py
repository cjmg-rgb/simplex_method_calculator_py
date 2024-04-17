from fractions import  Fraction


def get_ratio(x, sol):
    print("Ratio: ", end=" ")
    for i in range(len(sol)):
        print(Fraction(sol[i] / x[i]).limit_denominator(), end=" ")
    print("")


def get_new_row(row, multiplier):
    print("New Row: ", end=" ")
    new_row = []
    for i in range(len(row)):
        new_row.append(Fraction(row[i] * multiplier).limit_denominator())
        print(new_row[i], end=" ")
    print("")
    return new_row


def get_new_row_from_that(from_row, ce, this_row):
    new_arr = []
    for i in from_row:
        new_arr.append(Fraction(i * ce).limit_denominator())

    for i in range(len(new_arr)):
        new_arr[i] = Fraction(this_row[i] - new_arr[i]).limit_denominator()

    print("New row from is: ", end=" ")
    for i in new_arr:
        print(i, end=" ")
    print("")


def get_zj(cv, v):
    print("Z: ", end=" ")
    total_arr = []
    for i in range(len(v)):
        total = 0
        for j in range(len(cv)):
            total += cv[j] * v[i][j]
        total_arr.append(total)
        print(Fraction(total).limit_denominator(), end=" ")
    print("")
    return total_arr


def get_cj_zj(cj, zj):
    total = 0
    print("Cj-Zj:", end=" ")
    for i in range(len(cj)):
        print(Fraction(cj[i] - zj[i]).limit_denominator(), end=" ")
    print("")


# Constants
cj = [100, 85, 0, 0,  0]

# Get Ratio
get_ratio([1, 6, 3], [12, 30, 50])

# Create new basis row
main_row = get_new_row([6, 12, 0, 1, 0, 30], 1/6)

# Create new rows from basis
get_new_row_from_that(main_row, 3, [3, 1, 0, 0, 1, 15])

# Get Zjs
zj = get_zj([0, 100, 0], [
    [0,1, 0],
    [1, 2, -5],
    [1, 0, 0],
    [-1/6, 1/6, -1/2],
    [0, 0, 1],
    [7, 5, 35],
])

# Get Cjs - Zjs
get_cj_zj(cj, zj)

