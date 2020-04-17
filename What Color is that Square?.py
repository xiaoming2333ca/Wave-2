Horizontal1 = ['a', 'c', 'e', 'g']
Horizontal2 = ['b', 'd', 'f', 'h']
Vertical1 = ['1', '3', '5', '7']
Vertical2 = ['2', '4', '6', '8']
a = list(input("Please enter a position(letter before number)> "))
if a[0] in Horizontal1:
    if a[1] in Vertical1:
        print("Black")
    else:
        print("White")
else:
    if a[1] in Vertical1:
        print("White")
    else:
        print("Black")
