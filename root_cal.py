from math import sqrt


def disc_quad(a, b, c):
    dis = ((b ** 2) - (4 * a * c))
    return dis


def root_quad(a, b, c):
    dis = ((b ** 2) - (4 * a * c))
    sol1 = (-b - sqrt(dis)) / (2 * a)
    sol2 = (-b + sqrt(dis)) / (2 * a)
    return sol1, sol2
