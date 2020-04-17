while True:
    a = ['january', 'jan', 'jan.', 'march', 'mar', 'mar.', 'may', 'may.', 'july', 'jul', 'jul.', 'august', 'aug', 'aug.', 'october', 'oct', 'oct.', 'december', 'dec', 'dec.']
    b = ['april', 'apr', 'apr.', 'june', 'jun', 'jun.', 'september', 'sep', 'sep.', 'sept', 'sept.', 'november', 'nov', 'nov.']
    c = ['february', 'feb', 'feb.']
    d = input("Please enter a Month> ").lower()

    if d in a:
        print(f'31 days in {d.capitalize()}')
        break
    elif d in b:
        print(f'30 days in {d.capitalize()}')
        break
    elif d in c:
        print(f'29 or 28 days in {d.capitalize()}')
        break
    else:
        print("Invalid Value")
