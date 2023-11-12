# Python
...
ПРОВЕРКА ФОРМАТА ВАЛИДНОСТИ ПОЧТЫ
ПРОВЕРКА СУЩЕСТВОВАНИЯ ПОЧТЫ 


valid = validate_email('__', verify=True)
print(valid)

valid = validate_email('__', check_mx=True)
print(valid)