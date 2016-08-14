text = raw_input("Enter text: ")

encrypt_text = ""
decrypt_text = ""

for char in text:
    if char == " ":
        encrypt_text += str(ord(char))
    else:
        encrypt_text += str(ord(char) - 23)

print "Plain Text: " + text
print "Encrypted Text: " + encrypt_text

for i in range(0, len(encrypt_text) - 1, 2):
    if int(encrypt_text[i] + encrypt_text[i+1]) == 32:
        decrypt_text += chr(int(encrypt_text[i] + encrypt_text[i + 1]))
    else:
        decrypt_text += chr(int(encrypt_text[i] + encrypt_text[i+1]) + 23)

print "Decrypted Text: " + decrypt_text
