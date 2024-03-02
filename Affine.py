def egcd(a, b):
	x,y, u,v = 0,1, 1,0
	while a != 0:
		q, r = b//a, b%a
		m, n = x-u*q, y-v*q
		b,a, x,y, u,v = a,r, u,v, m,n
	gcd = b
	return gcd, x, y

def modinv(a, m):
	gcd, x, y = egcd(a, m)
	if gcd != 1:
		return None # modular inverse does not exist
	else:
		return x % m



def Encrypt():
	a = int(input("Choose KEY a"))
	b = int(input("Choose KEY b"))
	plaintext = str(input("ENTER MESSAGE: "))
	plaintext = plaintext.upper()
	cipher = ""
	for i in range (len(plaintext)):
		if ( (ord(plaintext[i]) < 65) or (ord(plaintext[i]) > 90) ):
			cipher += plaintext[i]
		else:
		    cipher += chr((a * (ord(plaintext[i]) - 65) + b) % 26 + 65)
	print(cipher)

def Decrypt():
	a = int(input("Choose KEY a"))
	b = int(input("Choose KEY b"))
	a__ = modinv(a, 26)
	cipher = str(input("ENTER ENCRYPTED: "))
	cipher = cipher.upper()
	plaintext = ""
	for i in range (len(cipher)):
		if ( (ord(cipher[i]) < 65) or (ord(cipher[i]) > 90) ):
			plaintext += cipher[i]
		else:
		    plaintext += chr(a__ * (ord(cipher[i]) - 65 - b) % 26 + 65)
	print(plaintext)

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
    #Key    : a = 17, b = 20
    #Message: AFFINE CIPHER
    #Cipher : UBBAHK CAPJKX
#Decrypt
    #Key    : a = 17, b = 20
    #Cipher: UBBAHK CAPJKX
    #Message : AFFINE CIPHER
	

