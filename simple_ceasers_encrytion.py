plain_text = raw_input("Enter text to encrypt: ")

move_forward = 5
encrypted_text = ""
decrypted_text = ""

for each in plain_text:
    if each.isalpha():
        encrypted_text += chr(ord(each) + move_forward)
    else:
        encrypted_text += each

for each in encrypted_text:
    if each.isspace():
        decrypted_text += each
    else:
        decrypted_text += chr(ord(each) - move_forward)

print "Encrypted text: " + encrypted_text
print "Decrypted text: " + decrypted_text