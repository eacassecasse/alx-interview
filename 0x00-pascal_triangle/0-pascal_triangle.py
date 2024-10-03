#!/usr/bin/python3

def pascal_triangle(n):
    triangle = []

    if n > 0:
        for i in range(0, n):
            coefs = []
            for j in range(i+1):
                if (j == 0) or (j == i):
                    coefs.insert(j, 1)
                else:
                    coef = triangle[i-1][j-1] + triangle[i-1][j]
                    coefs.insert(j, coef)
            triangle.append(coefs)

    return triangle
