# Задача 2. Напишите программу для проверки истинности
# утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


values = [[False, False, False], [True, False, False], [True, True, False], [True, True, True]]
result = True
for (x, y, z) in values:
    if not(not(x or y or z) == (not(x) and not(y) and not(z))):
        result = False
if result:
    print ('Выражение истинно.')
else:
    print ('Выражение ложно.')


