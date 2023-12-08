# Jacobi Iterative Method Solver

## Introduction

Welcome to the Jacobi Iterative Method Solver! This Python program is designed to solve a linear system of equations using the Jacobi iterative method. The Jacobi method is an iterative numerical technique that provides approximate solutions to systems of linear equations.

## How to Use

1. **Welcome and Guide:**
   - Upon execution, the program welcomes you and provides information about its purpose.

2. **Input System Equations:**
   - You'll be prompted to enter the number of equations in the system.
   - The program then guides you through inputting the coefficients of the system matrix and the constants of the equations.

3. **Matrix Treatment:**
   - The program checks if the system matrix is diagonally dominant, a condition required for Jacobi iteration.
   - If needed, it attempts to adjust the matrix to satisfy the diagonally dominant property.

4. **Matrix Display:**
   - Displays the treated system matrix.

5. **Choose Solution Method:**
   - You can choose between two methods to solve the system:
     - Specify the number of iterations.
     - Specify the convergence error.

6. **Solve the System:**
   - The program then applies the Jacobi iterative method based on your choice and displays the results.

## Functions Overview

1. **`welcomeAndGuide()`:**
   - Displays a welcome message and provides an introduction to the program.

2. **`fillMatrix(size)`:**
   - Takes the size of the system as input and prompts the user to input the coefficients of the system matrix.

3. **`fillArray(size)`:**
   - Takes the size of the system as input and prompts the user to input the constants of the equations.

4. **`displayMatrix(matrix)`:**
   - Displays the provided matrix.

5. **`Jacobi(A, b, tolerance, max_iterations)`:**
   - Implements the Jacobi iterative method to solve the linear system.

6. **`isDiagonallyDominant(arr)`:**
   - Checks if the matrix is diagonally dominant.

7. **`diagonalDominance(arr)`:**
   - Attempts to adjust the matrix to satisfy the diagonally dominant property.

## Main Program Execution

1. Calls `welcomeAndGuide()` to display the welcome message.
2. Prompts the user for the number of equations in the system and fills the system matrix.
3. Checks if the matrix is diagonally dominant and adjusts it if needed.
4. Displays the treated matrix.
5. Prompts the user to choose between solving by the number of iterations or convergence error.
6. Calls the Jacobi algorithm accordingly and displays the result.

## Usage Tips

- Ensure inputting valid numeric values for the matrix coefficients and constants.
- If the matrix is not diagonally dominant, the program attempts to adjust it, but it may not always succeed.
- Choose the solution method based on your preference: the number of iterations or convergence error.

Feel free to explore and analyze various linear systems using this Jacobi Iterative Method Solver!