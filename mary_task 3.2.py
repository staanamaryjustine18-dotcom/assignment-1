#
while True:
    input_password = input("Enter the password: ")
    has_letter = False
    has_digit = False
    
    for char in input_password:
        if char.isalpha():
            has_letter = True
        if char.isdigit():
            has_digit = True
            
    if has_letter and has_digit:
        print("Password accepted.")
        break     
    else:
        print("Invalid password.")