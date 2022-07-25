
try:
    enc_or_dec = int(input("enter what you want to do : ( encrypt / decrypt )\n 1 if encrypt, 2 if decrypt" ))
    path = input('Enter path of img : ')
        
    # taking decryption key as input
    key = int(input('Enter Key for encryption of img : '))
    if enc_or_dec == 1:
        # print path of img file and encryption key that
        # we are using
        print('The path of file : ', path)
        print('Key for encryption : ', key)
        
        # open file for reading purpose
        fn = open(path, 'rb')
        
        # storing img data in variable "img"
        img = fn.read()
        fn.close()
        
        # converting img into byte array to
        # perform encryption easily on numeric data
        img = bytearray(img)

        # performing XOR operation on each value of bytearray
        for index, values in enumerate(img):
            img[index] = values ^ key

        # opening file for writing purpose
        fn = open(path, 'wb')
        
        # writing encrypted data in img
        fn.write(img)
        fn.close()
    elif enc_or_dec == 2:
            # take path of img as a input

        
        # print path of img file and decryption key that we are using
        print('The path of file : ', path)
        print('Note : Encryption key and Decryption key must be same.')
        print('Key for Decryption : ', key)
        
        # open file for reading purpose
        fn = open(path, 'rb')
        
        # storing img data in variable "img"
        img = fn.read()
        fn.close()
        
        # converting img into byte array to perform decryption easily on numeric data
        img = bytearray(img)

        # performing XOR operation on each value of bytearray
        for index, values in enumerate(img):
            img[index] = values ^ key

        # opening file for writing purpose
        fn = open(path, 'wb')
        
        # writing decryption data in img
        fn.write(img)
        fn.close()
        print('Decryption Done...')

except Exception:
	print('Error caught : ', Exception.__name__)