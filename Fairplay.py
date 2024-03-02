import itertools
def Create_Matrix (key):
    key = key.upper()
    key = key.replace(" ","")
    matrix = [[0 for i in range (5)] for j in range(5)]
    added_letters = []
    row = 0
    col = 0
    for letter in key:
        if letter not in added_letters:
            if (letter == 'J') and ('I' in added_letters):
                continue
            else:
                added_letters.append(letter)
        else:
            continue
    for letter in range(65, 91):
        if (letter == 74):
            continue
        if (chr(letter) not in added_letters):
            added_letters.append(chr(letter))

    index = 0

    #For Matrix checking purpose
    print("Current Key Matrix:")
    for i in range (5):
        for j in range (5):
            matrix[i][j] = added_letters[index]
            index += 1
        print(matrix[i])
    return matrix

def Add_X_letter (message):
    message = message.replace(" ","")
    message = message.upper()
    message = message.replace("J","I")
    ret_msg = ""
    index = 0
    
    if (len(message) < 2):
        ret_msg = message
    for i in range(len(message) - 1):
        ret_msg += message[i]
        if (message[i] == message[i + 1]):
            ret_msg += 'X'
    ret_msg += message[-1]
    if (len(ret_msg) & 1):
        ret_msg += 'X'

    #For Message checking purpose
    print("Prepare Message to Encode:", end = '     ')
    for i in range (0, len(ret_msg) - 1, 2):
        print(ret_msg[i] + ret_msg[i + 1], end = ' ')
    print()
    print(ret_msg)
    return ret_msg

def Check_index(matrix, letter):
    if letter == 'J':
        letter = 'I'
    for i,j in enumerate(matrix):
        for k,l in enumerate(j):
            if l == letter:
                return i, k

def Encrypt():
    key = str(input("ENTER KEY: "))
    matrix = Create_Matrix(key)
    plaintext = str(input("ENTER MESSAGE: "))
    temp_plain = Add_X_letter(plaintext)
    print("CIPHER TEXT:",end=' ')
    ciphertext = ""
    for i in range (0, len(temp_plain) - 1, 2):
        row1, col1 = Check_index(matrix, temp_plain[i])
        row2, col2 = Check_index(matrix, temp_plain[i + 1])
        if row1 == row2:
            ciphertext += matrix[row1][ (col1 + 1) % 5]
            ciphertext += matrix[row2][ (col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[ (row1 + 1) % 5][col1]
            ciphertext += matrix[ (row2 + 1) % 5][col2]
        else:  # rectangle
            ciphertext += matrix[row1][col2]
            ciphertext += matrix[row2][col1]
    print(ciphertext)

def Decrypt():
    key = str(input("ENTER KEY: "))
    matrix = Create_Matrix(key)
    ciphertext = str(input("ENTER ENCRYPTED: "))
    ciphertext = ciphertext.replace(" ","")
    ciphertext = ciphertext.upper()
    ciphertext = ciphertext.replace("J","I")
    print("PLAIN TEXT:",end=' ')
    plaintext = ""
    for i in range (0, len(ciphertext) - 1, 2):
        row1, col1 = Check_index(matrix, ciphertext[i])
        row2, col2 = Check_index(matrix, ciphertext[i + 1])
        if row1 == row2:
            plaintext += matrix[row1][ (col1 - 1) % 5]
            plaintext += matrix[row2][ (col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[ (row1 - 1) % 5][col1]
            plaintext += matrix[ (row2 - 1) % 5][col2]
        else:  # rectangle
            plaintext += matrix[row1][col2]
            plaintext += matrix[row2][col1]
    print(plaintext)
    #other_text1 = plaintext.replace("X", plaintext[plaintext.index('X') + 1])


while True:
    choice = int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT"))
    if choice == 1:
        Encrypt()
    elif choice ==2:
        Decrypt()
    elif choice == 3:
        exit()
    else:
        print("Choose correct choice")


#Encrypt
    #Key    : playfair example
    #Message: hide the gold in the tree stump
    #Cipher : BM OD ZB XD NA BE KU DM UI XM MO UV IF
#Decrypt
    #Key        : playfair example
    #Cipher     : BM OD ZB XD NA BE KU DM UI XM MO UV IF 
    #Plaintext  : HIDETHEGOLDINTHETREXESTUMP
                #(HIDE THE GOLD IN THE TREXE STUMP)        