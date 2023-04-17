import time
import random
уже = False

def Main_Menu():
    global Text, Text_Length, Current_Character, Non_Encrypted_List, Encrypted_List, Num, уже, List, Binary_Code, Code

    Binary_Code = []
    List = []
    Code = []
    
    with open('Cipher_Codes.txt', 'r') as f:
            binary = []
            lists = []
            codes = []
            for line in f:
                parts = line.strip().split('::')
                binary.append(parts[0])
                lists.append(parts[1])
                codes.append(parts[2])

    
    Current_line = 0

    if уже == False:
        
        Choice = input("Generate(G) or Enter a code(E): ").lower()
        if Choice == "g":
            уже = True
            Random_Code_Chooser = random.randint(0, 31)
            Binary_Code = binary[Random_Code_Chooser]
            List = lists[Random_Code_Chooser]
            Code = codes[Random_Code_Chooser]

            print(List)

            Bin = "Generating binary value"
            Cod = "Generating code"
            
            print(Bin, end="")
            for i in range(3):
                print(".", end="")
                time.sleep(1.2)
            print()     
            
            print("Binary Value = ", Binary_Code)

            print(Cod, end="")
            for i in range(2):
                print(".", end="")
                time.sleep(1.4)
            print()     
            
            print("Your code is: ", Code)            
    
        elif Choice == "e":
            Code = input("Enter your code: ")
                
            Val = "Validating code"
            print(Val, end="")
            for i in range(3):
                print(".", end="")
                time.sleep(0.7)
            print()
            print()

            if Code not in codes:
                print("Invalid code!")
                Main_Menu()

            уже = True
            for i in range(32):
                if Code == codes[Current_line]:
                    List = lists[Current_line]
                    Binary_Code = binary[Current_line]
                else:
                    Current_line+=1
        else:
            print("Invalid option!")
            Main_Menu()
        
    
    Main = input("Do you want to Enrcrypt(E), or Decrypt(D): ").lower()

    Non_Encrypted_List = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "]", "{", "}", "|", "\\", ";", ":", ",", ".", "<", ">", "/", "?", "`"]    
    Encrypted_List = List
    
    Num = 0
    Current_Character = 0
    
    if Main == "e":
        Text = input("Enter the text you want to encrypt: ").lower()
        Text_Length = len(Text)
        Encrypter()
    elif Main == "d":
        Text = input("Enter the text you want to decrypt: ").lower()
        Text_Length = len(Text)
        Decrypter()
    else:
        print("Invalid option!")
        Main_Menu()
        

def Encrypter():
    global Text, Text_Length, Current_Character, Non_Encrypted_List, Encrypted_List, Num, уже, List, Binary_Code, Code
   
    Encrypted_Text = ""
    
    for i in range(Text_Length):
        Num = 0
        found_match = False
        while not found_match and Num < len(Non_Encrypted_List):
            if Text[Current_Character] == Non_Encrypted_List[Num]:
                Encrypted_Text += Encrypted_List[Num]
                Current_Character += 1
                found_match = True
            else:
                Num += 1
                
        if not found_match:
            Encrypted_Text += Text[Current_Character]
            Current_Character += 1

    Cipher = "Encrypting text"      

    print(Cipher, end="")
    for i in range(3):
        print(".", end="")
        time.sleep(1.2)
    print()
    
    print("Encrypted Text: ", Encrypted_Text)
    print(List)

    print()
    print("--")
    Main_Menu()

def Decrypter():
    global Text, Text_Length, Current_Character, Non_Encrypted_List, Encrypted_List, Num, уже, List, Binary_Code, Code

    Decrypted_Text = ""
    
    for i in range(Text_Length):
        Num = 0
        found_match = False
        while not found_match and Num < len(Non_Encrypted_List):
            if Text[Current_Character] == Encrypted_List[Num]:
                Decrypted_Text += Non_Encrypted_List[Num]
                Current_Character += 1
                found_match = True
            else:
                Num += 1
                
        if not found_match:
            Decrypted_Text += Text[Current_Character]
            Current_Character += 1

    Cipher = "Decrypting text"        

    print(Cipher, end="")
    for i in range(3):
        print(".", end="")
        time.sleep(1.2)
    print()     
            
    print("Decrypted Text: ", Decrypted_Text)

    print()
    print("--")
    Main_Menu()

Main_Menu()

