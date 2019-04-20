# list_exercises.py - this prgm follows along with the DC day 4's list
#                     exercises
#
# jf - 4/18


#######################
### Sum the Numbers ###
#######################


def sum_the_number(lst):
    '''
    param:
        lst -> List
    return:
        ret_val -> Float (or Int, depending)
    '''

    return sum(lst)

def main_0():
    # main function for Sum the Numbers problem

    print(sum_the_number(get_input_values_as_list_of_ints()))


######################
### Largest Number ###
######################


def largest_number_manual(lst):
    '''
    param:
        lst -> List
    return:
        ret_val -> Float (or Int, depending)
    '''

    max_val = lst[0]

    for val in lst[1:]:
        if val > max_val:
            max_val = val

    return max_val

def largest_number_easy(lst):
    '''
    param:
        lst -> List
    return:
        ret_val -> Float (or Int, depending)
    '''

    return max(lst)

def main_1_0():
    # main function 1 of 2 for Largest Number problem

    print(largest_number_manual(get_input_values_as_list_of_ints()))

def main_1_1():
    # main function 2 of 2 for Largest Number problem

    print(largest_number_easy(get_input_values_as_list_of_ints()))


#######################
### Smallest Number ###
#######################


def smallest_number(lst):
    '''
    param:
        lst -> List
    return:
        ret_val -> Float (or Int, depending)
    '''

    return min(lst)

def main_2():
    # main function for Smallest Number problem

    print(smallest_number(get_input_values_as_list_of_ints()))


####################
### Even Numbers ###
####################

def even_numbers(lst):
    '''
    param:
        lst -> List
    return:
        ret_val -> List
    '''

    return [e for e in lst if e % 2 == 0]

def main_3():
    # main function for Even Numbers problem

    print(even_numbers(get_input_values_as_list_of_ints()))


########################
### Positive Numbers ###
########################


def positive_numbers(lst):
    '''
    param:
        lst -> List
    return:
        ret_val -> List
    '''

    return [e for e in lst if e > 0]

def main_4():
    # main function for Positive Numbers problem

    print(positive_numbers(get_input_values_as_list_of_ints()))


###########################
### Positive Numbers II ###
###########################


def positive_numbers_ii(lst):
    '''
    param:
        lst -> List
    return:
        ret_val -> List
    '''

    return positive_numbers(lst)

def main_5():
    # main function for Positive Numbers II problem

    positive_numbers_ii(get_input_values_as_list_of_ints())


#######################
### Multiply a List ###
#######################


def multiply_a_list(lst, scalar):
    '''
    params:
        lst -> List
        scalar -> Float (or Int, depending)
    return:
        ret_val -> List
    '''

    return [e*scalar for e in lst]

def main_6():
    # main function for Multiply a List problem

    print(multiply_a_list(get_input_values_as_list_of_ints(), int(input("Enter a scalar: "))))


########################
### Multiply Vectors ###
########################


def multiply_vectors(v1, v2):
    '''
    params:
        v1 -> List
        v2 -> List
    return:
        ret_val -> List
    '''

    # n.b. this is NOT a dot product of vectors, it's a componentwise product.
    # moreover, assume that the dimensions are appropriate for this particular
    # definition of vector multiplication

    return [v1[i]*v2[i] for i in range(len(v1))]

def main_7():
    # main function for Multiply Vectors problem

    vector1_raw = input("Enter the first vector as a list of numbers, separated by spaces: ").split()
    vector2_raw = input("Enter the second vector as a list of numbers, separated by spaces: ").split()

    vector1_formatted = [int(e) for e in vector1_raw]
    vector2_formatted = [int(e) for e in vector2_raw]

    print(multiply_vectors(vector1_formatted, vector2_formatted))


#######################
### Matrix Addition ###
#######################


def matrix_addition(mtx1, mtx2):
    '''
    params:
        mtx1 -> List[List]
        mtx2 -> List[List]
    ret_val:
        mtx_out -> List[List]
    '''

    # create output matrix
    mtx_out = [list() for _ in range(len(mtx1))]

    # first, iterate over the rows
    for row in range(len(mtx1)):

        # second, iterate over the columns
        for col in range(len(mtx1[0])):

            # c_ij = a_ij + b_ij
            mtx_out[row].append(mtx1[row][col] + mtx2[row][col])

    return mtx_out

def main_8():
    # main function for Matrix Addition problem

    # assume 2x2 matrices are being added

    print(matrix_addition(*get_input_values_for_matrix()))


##########################
### Matrix Addition II ###
##########################


def matrix_addition_ii(mtx1, mtx2):
    '''
    params:
        mtx1 -> List[List]
        mtx2 -> List[List]
    ret_val:
        mtx_out -> List[List]

        can also return None for bad dimensions
    '''

    # first, check that the dimensions are appropriate
    num_rows_mtx1 = len(mtx1)
    num_cols_mtx1 = len(mtx1[0]) if len(mtx1[0]) == len(mtx1[1]) else False

    num_rows_mtx2 = len(mtx2)
    num_cols_mtx2 = len(mtx2[0]) if len(mtx2[0]) == len(mtx2[1]) else False

    # if the dimensions within a particular matrix are out of whack (i.e. it's not appropriately 
    # rectangular, at least) then return
    if num_cols_mtx1 == False or num_cols_mtx2 == False:
        print("Not appropriately rectangular matrix given")
        return None

    # then check the relevant dimensions between the two input matrices
    if not (num_rows_mtx1 == num_rows_mtx2) or not (num_cols_mtx1 == num_cols_mtx2):
        print("Dimensions are off")
        return None

    # since equivalent dimensions test passed, move forward with matrix addition
    return matrix_addition(mtx1, mtx2)

def main_9():
    # main method for Matrix Addition II problem

    ret_val = matrix_addition_ii(*get_input_values_for_matrix())

    # only print the return value if the dimensions were correct
    if ret_val:
        print(ret_val)        


##############    
### De-dup ###
##############


def de_dup(lst):
    '''
    param:
        lst -> List[Lists or Strings]
    return:
        ret_val -> List[Lists or Strings]
    '''

    ret_val = list()

    for item in lst:

        if item not in ret_val:

            ret_val.append(item)

    return ret_val


def main_10():
    # main function for De-dup problem

    nums_or_strings = input("Do you wish to enter numbers or strings? (n/s): ")

    if nums_or_strings == 'n':
        print(de_dup(get_input_values_as_list_of_ints()))
    else:

        list_of_strings = input("Enter a sequence of strings, separated by spaces: ").split()
        print(de_dup(list_of_strings))


####################################
### Bonus: Matrix Multiplication ###
####################################


def matrix_multiplication(matrixA, matrixB):
    '''
    params:
        matrixA -> List[ Lists ]
        matrixB -> List[ Lists ]
    return:
        C -> List[ Lists ]
    '''

    # Assumption: input matrices have the appropriate dimension
    
    # n.b. this is the naive algorithm, so the complexity is O(n^3) -- take into consideration
    # when passing in large matrices


    ######
    #
    # we represent matrices in python as two-dimensional arrays -- i.e., lists of lists
    # wherein each list within the "mother" list represents a row & the entries in said
    # list are the column entries
    #
    # now, while there are several ways to envision matrix multiplication, we assume that
    # we're looking at usual method: a matrix, B, is multiplied on the left by another matrix,
    # A, whose number of columns equals B's number of rows. thus, essentially, we're dotting
    # a column vector of B with a row vector of A for each resultant entry in the resultant
    # matrix, which we'll call C.
    # 
    # as an example, under this context, this is how two 2x2 matrices are multiplied:
    #
    #   A = [ [1, 2],           B = [ [5, 6],           C = [ [ 0, 0],
    #         [3, 4] ]                [7, 8] ]                [ 0, 0] ]
    #
    #   C_row1_column1_entry = dot_product(A_row1, B_column1)
    #                        = A_row1_column1_entry * B_row1_column1_entry +
    #                          A_row1_column2_entry * B_row2_column1_entry
    #                        = 1*5 + 2*7
    #                        = 19
    #
    # Likewise, every other entry of C is a correspondent dot_product(row_from_A, column_from_B)
    #
    # Following this logic, we can establish a concrete formula for each entry of C, from
    # which we can build our above referenced naive algorithm.
    #
    # If i = some row & j = some column, then:
    #
    #   C_ij = sum_over_k(A_ik * B_kj), where k == # rows in B OR == # columns in A
    # 
    # For the above example, this yields the following result:
    # 
    #   C = [ [19, 22],
    #         [43, 50]]
    #
    ######  

    # initialize the resultant matrix
    C = list(list(0 for _ in range(len(matrixB))) for _ in range(len(matrixA[0])))
    
    # loop over the rows in A
    for i in range(len(matrixA)):

        # for each row in A, loop over the columns in B
        for j in range(len(matrixB[0])):

            # perform the dot product, so loop over k, which was established above
            # as == # columns in A OR == # rows in B
            for k in range(len(matrixB)):

                # for each k, add the product of the corresponding matrixA, matrixB
                # entries
                C[i][j] += matrixA[i][k]*matrixB[k][j]

    return C


def main_11():
    # the main function associated with the Matrix Multiplication problem

    A, B = [[1, 2], [3, 4]], [[5, 6], [7, 8]]

    print("Multiplying A:", A, "with B:", B)
    print("--> Result:", matrix_multiplication(A, B))


#######################
### HELPER FUNCTION ###
#######################


def get_input_values_as_list_of_ints():
    # gets user to input numbers, then returns as list of said numbers

    inpt = input("Enter a sequence of numbers, separated by spaces: ")
    nums = [int(e) for e in inpt.split()]

    return nums

def get_input_values_for_matrix():
    # gets user to input numbers by row, then returns two list of lists (i.e. matrices) with numbers
    # as corresponding to the input

    row1_matrix1 = input("Enter first row of first matrix as a list of numbers, separated by spaces: ").split()
    row2_matrix1 = input("Enter second row of first matrix as a list of numbers, separated by spaces: ").split()
    row1_matrix2 = input("Enter first row of second matrix as a list of numbers, separated by spaces: ").split()
    row2_matrix2 = input("Enter second row of second matrix as a list of numbers, separated by spaces: ").split()

    row1_matrix1_formatted = [int(e) for e in row1_matrix1]
    row2_matrix1_formatted = [int(e) for e in row2_matrix1]
    row1_matrix2_formatted = [int(e) for e in row1_matrix2]
    row2_matrix2_formatted = [int(e) for e in row2_matrix2]

    matrix1 = [row1_matrix1_formatted, row2_matrix1_formatted]
    matrix2 = [row1_matrix2_formatted, row2_matrix2_formatted]

    return matrix1, matrix2


# to be run as script
if __name__ == "__main__":
    # main_0()
    # main_1_0()
    # main_1_1()
    # main_2()
    # main_3()
    # main_4()
    # main_5()
    # main_6()
    # main_7()
    # main_8()
    # main_9()
    # main_10()
    main_11()