

from validate_email import validate_email

# import validate_email  
# em_inp = input("Введите email ")
# email = validate_email.validate_email(em_inp)

# if email == True:
#     print ('email is valid ')
# else:
#     print ('email is not valid ')


# print(validate_email('vitaliksigaev@gmail.com'))

valid = validate_email('__', verify=True)
print(valid)

valid = validate_email('__', verify=True)
print(valid)

valid = validate_email('__', check_mx=True)
print(valid)


valid = validate_email('__', verify=True) 
# none
print(valid)

valid = validate_email('__', check_mx=True)
print(valid)