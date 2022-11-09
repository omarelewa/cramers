# Linear Algebra Fall 2022– Course Project “Cramer’s Rule”
#### By Omar Elewa

## Instructions

Write a programming code using MATLAB, Python, C++ or any programming language to solve a system of 𝑛 linear equations in n variables using Cramer’s Rule.
 - Your code should allow the user to choose the size 𝑛 × 𝑛 of the system.
 - Make sure that your program first checks that the coefficient matrix is invertible.
 - The output of your program must be the unique solution of the system.
 - Use your code to solve exercises 25, 26 of Section 3.4, page 142.
 - Save your code together with the inputs and outputs of exercise 25 or 26 of section 3.4 as a second PDF file, then submit it to its assigned slot on Gradescope.

## Exercise 25

Solve the following system of linear equation using Cramer’s Rule:

>3x_1 − 2x_2 + 9x_3 + 4x_4 = 35
> 
>−x_1 − 9x_3 − 6x_4 =−17
> 
>3x_3 + x_4 = 5
> 
>2x_1 + 2x_2 + 8x4 = −4

### Solution

```
Enter the number of rows and columns: 4
Enter the elements of matrix: 
Enter the elements of row 1
3
-2
9
4
Enter the elements of row 2
-1
0
-9
-6
Enter the elements of row 3
0
0
3
1
Enter the elements of row 4
2
2
0
8
The determinant of the coefficient matrix is:  36
The coefficient matrix is non-singular.
Enter the elements of solution matrix: 
35
-17
5
-4
The solution matrix is:  [35, -17, 5, -4]
The value of x 1 is:  5.0
The value of x 2 is:  -3.0
The value of x 3 is:  2.0
The value of x 4 is:  -1.0

Process finished with exit code 0
```

## Exercise 26

Solve the following system of linear equation using Cramer’s Rule:
−x1 −x2 +x4= −8
3x1 +5x2 +5x3 = 24
2x3 +x4 = −6
−2x1 −3x2 −3x3 = −15
