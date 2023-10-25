def encode(code):  ## Darvan Cherichel
    
    pass_encoded="" 
    
    for digit in code:
        
        if digit == "1":
            pass_encoded+="4"
        
        elif digit =="2":
            pass_encoded+="5"
        
        elif digit=="3":
            pass_encoded+="6"
            
        elif digit=="4":
            pass_encoded+="7"
            
        elif digit=="5":
            pass_encoded+="8"
        
        elif digit=="6":
            pass_encoded+="9"
        
        elif digit=="7":
            pass_encoded+="0"
        
        elif digit=="8":
            pass_encoded+="1"
        
        elif digit=="9":
            pass_encoded+="2"
        
        elif digit=="0":
            pass_encoded+="3"
        
    
    return pass_encoded


def decode(password):   # Chasden Johns
    total = ''
    for item in str(password):
        if int(item) > 2:
            total += (str(int(item) - 3))
        if item == '0':
            total += '7'
        elif item == '1':
            total += '8'
        elif item == '2':
            total += '9'
    return total



def main():
    og_pass=0
    while True:
        print()
        print("Menu")
        
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        
        menu_opt = int(input("Please enter an Option: "))
        
        if menu_opt == 1:
            og_pass = (input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")

        elif menu_opt == 2:
            encoded_pass=encode(og_pass)
            print(f"The encoded password is {encoded_pass}, and the original password is {decode(encoded_pass)}.")
            
            
           
        
        elif menu_opt == 3:
            break
            
        


if __name__== "__main__":
    main()