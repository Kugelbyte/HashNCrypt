import os  
import os.path  
import hashlib

def encrypt_file():
    filename = input("Enter the path to the file: ")   
    key = int(input("Enter the key: "))
    if (os.path.isfile(filename)):
    
       with open(filename, 'r') as file:
           result = ''
           lines = file.read()
           for line in lines:
               for i in range(len(line)):
                   letter = line[i]
                   try:
                        if (line.isupper()):
                           result += chr((ord(letter) + int(key) - 65) % 26 + 65)
                        elif (line.islower()):
                           result += chr((ord(letter) + int(key) - 97) % 26 + 97)
                    
                   except:
                        print("[-] Could not encrypt. Something went wrong\n")

       file.close()  
       
       with open('encryptedfile.txt', 'w') as f:
        f.writelines(result)
        print("[+] File encrypted\n")

    else:
         print("[-] File not found. Enter the correct path and try again.\n")
         encrypt_file()
                                



def encrypt_text():

    plaintext = input("[+] Enter the plaintext: ")  
    key = int(input("Enter the key: "))
    result = ''  
    for i in range(len(plaintext)):
        letter = plaintext[i]

        try:
            if (letter.isupper()):
                result += chr((ord(letter) + int(key) - 65) % 26 + 65)
            elif (letter.islower()):
                result += chr((ord(letter) + int(key) - 97) % 26 + 97)
        except:
            print ("[-] Could not encrypt. Invalid plaintext!!\n")

    return result


def hash_file():
    filename = input("[+] Enter the path to the file: ") 
    choice = input("[+] Enter the hashing algorithm: ")
    hash = ''
    try:
     match choice:
          case 'md5':
                with open(filename, 'r') as file:
                    content = file.read()
                    file.close() 
                hash = hashlib.md5(content.encode())
                print(hash.hexdigest())

          case 'sha1':
                with open(filename, 'r') as file:
                    content = file.read()
                    file.close() 
                hash = hashlib.sha1(content.encode())
                print(hash.hexdigest())    
    
          case 'sha256':
                with open(filename, 'r') as file:
                    content = file.read()
                    file.close() 
                hash = hashlib.sha256(content.encode())
                print(hash.hexdigest())
    
    except:
      print("[-] Something went wrong. Please try again")
      hash_file() 






if __name__ == '__main__':
     
     while True:
         print(
 '''
[1] Encrypt file         
[2] Encrypt text  
[3] Calculate hash of a file                       
             ''')

         Choice = input()
     
         match Choice:
            case '1':
                encrypt_file()
            case '2':
                print(encrypt_text())
            case '3':
                hash_file()
            case _:
                print("Something went wrong")
                continue

         is_end = input("Do something else (y/n): ")

         if (is_end == 'n'):
            break
                     