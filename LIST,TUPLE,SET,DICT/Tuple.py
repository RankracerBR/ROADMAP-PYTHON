t1 = (1, 2, 3, 4)

t2 = tuple([1, 2, 3, 4, 5])

t3 = tuple([1, 2, 3, 4, 5, 6])

print(f'Tuple t1: {t1}')
print(f'Tuple t2: {t2}')
print(f'Tuple t3: {t3}')

print(f"The value at index 1 in t2 is: {t2[1]}")

working_hours = {("Rebecca", 1): 38, ("Thomas",2): 40}
print(working_hours)

working_hours = {(["Rebecca", 1]): 38, (["Thomas",2]): 40}
print(working_hours)