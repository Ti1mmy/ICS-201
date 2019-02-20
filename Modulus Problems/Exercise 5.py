total_cents = int(input('Number of cents: '))
toonies = total_cents // 200
remainder_toonies = total_cents % 200
loonies = remainder_toonies // 100
remainder_loonies = remainder_toonies % 100
quarters = remainder_loonies // 25
remainder_quarters = remainder_loonies % 25
dimes = remainder_quarters // 10
remainder_dimes = remainder_quarters % 10
nickels = remainder_dimes // 5
remainder_nickels = remainder_dimes % 5
pennies = remainder_nickels
print(f'{total_cents} cents is:')
if toonies > 1:
    print(f'{toonies} - toonies')
elif toonies == 1:
    print(f'{toonies} - toonie')
elif toonies == 0:
    print(f'{toonies} - toonies')
if loonies > 1:
    print(f'{loonies} - loonies')
elif loonies == 1:
    print(f'{loonies} - loonie')
elif loonies == 0:
    print(f'{loonies} - loonies')
if quarters > 1:
    print(f'{quarters} - quarters')
elif quarters == 1:
    print(f'{quarters} - quarter')
elif toonies == 0:
    print(f'{quarters} - quarters')
if dimes > 1:
    print(f'{dimes} - dimes')
elif dimes == 1:
    print(f'{dimes} - dime')
elif dimes == 0:
    print(f'{dimes} - dimes')
if nickels > 1:
    print(f'{nickels} - nickels')
elif nickels == 1:
    print(f'{nickels} - nickel')
elif nickels == 0:
    print(f'{nickels} - nickels')
if pennies > 1:
    print(f'{pennies} - pennies')
elif pennies == 1:
    print(f'{pennies} - penny')
elif pennies == 0:
    print(f'{pennies} - pennies')