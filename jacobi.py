'''                                 Program made by SOUBIH Meriem and ZELLAL Nourelhouda || L2 G8                                     '''


# importing the NumPy library for numerical operations
import numpy as np
# ------------------------ display welcome and guide message ------------------------
def welcomeAndGuide():

    """Display welcome message and program guide."""

    print("\n\n\t\t\t\t<<-------- Welcome to our program -------->>\n")
    print("\n-> This program solves a linear system of equations using the Jacobi iterative method.")
    print("\n-> The program works with either knowing the number of iterations OR having the convergence error.")

# ------------------------ fill matrix with input values ----------------------------
def fillMatrix(size):

    """Prompt the user to fill the matrix with coefficients."""

    matrix = []
    for y in range(size):
        row = []
        for x in range(size):
            while True:
                value = float(input(f"\tEnter value for [{y}][{x}]: "))
                if x == y and value == 0:
                    print("Diagonal elements must be non-zero. Please re-enter.")
                else:
                    break
            row.append(value)
        matrix.append(row)
    return matrix


# --------------------- fill array with equation constants --------------------------
def fillArray(size):

    """Prompt the user to fill the array with constants."""

    return [float(input(f"\tEnter value of Vector of constant B[{i}]: ")) for i in range(size)]


# ---------------------------- display matrix ---------------------------------------
def displayMatrix(matrix):

    """Display the matrix."""

    for row in matrix:
        print("\t", end="")
        print("\t".join(f"{elem}" for elem in row))


# ---------------------------- display result ---------------------------------------
def displayResult(arr):

    """Display the result of the linear system."""

    print("\n\n\t\t\t\t<<---------- Analysis completed -------->>\n")
    print("The solutions of the provided linear system are: \n")
    print("\n".join(f"x{i}: {elem}" for i, elem in enumerate(arr)))


# ----------------------------- JACOBI ALGORITHM ------------------------------------
def Jacobi(A, b, tolerance, max_iterations = 10000):

    """
    Solve a linear system using the Jacobi iterative method.

    Parameters:
    - A: Coefficient matrix
    - b: Vector of constants
    - tolerance: Convergence error (if -1, the method uses a fixed number of iterations)
    - max_iterations: Maximum number of iterations

    Returns:
    - The solution vector
    """

    n = len(b)
    x = [0] * n
    x_prime = [0] * n
    iteration = 0
    A = np.array(A)
    b = np.array(b)

    while iteration < max_iterations:
        for i in range(n): 
            summation = 0
            for j in range(n): 
                if j != i:
                    summation += A[i][j] * x[j]
            x_prime[i] = (b[i] - summation) / A[i][i]

        # checking for convergence if tolerance is specified
        if tolerance != -1:
            if np.linalg.norm(np.array(x_prime) - np.array(x)) < tolerance:
                print(f"\nFound system solution after {iteration} iterations.")
                return x_prime

        # updating the solution vector
        x = x_prime.copy()
        iteration += 1

    return x


# ------------------- check if matrix is diagonally dominant ------------------------
def isDiagonallyDominant(arr):

    """Check if a matrix is diagonally dominant."""

    size = len(arr)
    for i in range(size):
        diagonal_value = abs(arr[i][i])
        row_sum = sum(abs(arr[i][k]) for k in range(size) if k != i)
        if diagonal_value < row_sum:
            return False
    return True


#  ------------------ check if matrix can be diagonally dominant --------------------
def diagonalDominance(arr):

    """
    Make a matrix diagonally dominant.

    If the matrix is not initially diagonally dominant, attempt to swap rows
    to achieve diagonally dominant properties.

    Parameters:
    - arr: The matrix

    Returns:
    - The modified matrix if successful, otherwise None
    """

    if not isDiagonallyDominant(arr):
        size = len(arr)
        for i in range(size):
            diagonal_value = abs(arr[i][i])
            row_sum = sum(abs(arr[i][k]) for k in range(size) if k != i)
            pos = -1
            if diagonal_value < row_sum:
                # finding a row to swap with to achieve diagonal dominance
                for j in range(size):
                    if j != i and abs(arr[j][i]) >= sum(abs(arr[j][k]) for k in range(size) if k != i):
                        pos = j
                        break
                # swapping rows if a suitable row is found
                if pos >= 0 and i != pos:
                    arr[i], arr[pos] = arr[pos][:], arr[i][:]
                    print(f"\n\tSwapped rows {i} and {pos}")

        if isDiagonallyDominant(arr):
            print("\nMatrix treated and ready to be analyzed!\n")
            return arr
        else:
            print("Could not find rows to swap in order to make the matrix diagonally dominant.\nCannot apply Jacobi iterations on this system!")
            return None

    else:
        print("\nMatrix treated and ready to be analyzed!\n")
        return arr




# ------------------------------ MAIN PROMGRAM --------------------------------------
welcomeAndGuide()
# prompt user to give number of equations in the system
size = int(input("\n\tEnter the number of equations of the system: "))
while size <= 0:
    print ("\nPlease enter a positive integer")
    size = input("\n\tEnter the number of equations of the system: ")

# fill matrix of system
A = fillMatrix(size)

# verify conditions and values of matrix before starting
print("\nTreating system values...\n\nChecking if matrix is diagonally dominant...")

# check for diagonal dominance of the system matrix
A = diagonalDominance(A)

if A != None:
    displayMatrix(A)
    # fill values of resolution 
    b = fillArray(size)
    print("\nIs the system solved using:\n\t- 1 > Number of iterations\n\t- 2 > Convergence error ")
    choice = int(input("Your choice: "))
    while choice != 1 and choice != 2:
        print("\nInvalid choice. Please enter 1 or 2.")
        choice = int(input("\nYour choice: "))
    print("\nAnalyzing system values...")
    if choice == 1:
        # solve system using iteration
        max_iterations = int(input("\nEnter number of iterations for solving this system: "))
        print("\nSolving system using iteration...")
        displayResult(Jacobi(A, b, -1, max_iterations))
    elif choice == 2:
        # solve system using convergence error
        tolerance = float(input("\nEnter convergence error for solving this system: "))
        print("\nSolving system using convergence error...")
        displayResult(Jacobi(A, b, tolerance))
