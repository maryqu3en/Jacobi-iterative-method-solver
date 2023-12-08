# Jacobi Iterative Method Solver

## Introduction

Welcome to the Jacobi Iterative Method Solver! This Python program is designed to solve a linear system of equations using the Jacobi iterative method. The Jacobi method is an iterative numerical technique that provides approximate solutions to systems of linear equations.

## How to Use

```markdown
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
