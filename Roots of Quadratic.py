import root_cal
print("Quadratic root(s) solver. Please enter the three value a, b, and, c. Separate by [space]")
a = int(input("a> "))
b = int(input("b> "))
c = int(input("c> "))
dis = root_cal.disc_quad(a, b, c)

if a != 0:
    if dis > 0:
        sol1, sol2 = root_cal.root_quad(a, b, c)[0], root_cal.root_quad(a, b, c)[1]
        print(f'Two solutions: x1 = {sol1} and x2 = {sol2}')
    if dis == 0:
        sol = root_cal.root_quad(a, b, c)[0]
        print(f"One solution: x = {sol}")
    if dis < 0:
        print("No solution")
else:
    print("The number you just entered is not belong to a quadratic")
