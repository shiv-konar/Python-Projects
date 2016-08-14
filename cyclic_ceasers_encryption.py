plain_text = raw_input("Enter plain text: ")
shift = int(raw_input("Enter shift (1-26): "))

encrypted_text = ""
decrypted_text = ""

for each in plain_text:
    if each.isalpha():
        char_code = ord(each)
        char_code += shift

        if each.isupper():
            if char_code > ord('Z'):
                char_code -= 26

            elif char_code < ord('A'):
                char_code += 26

        if each.islower():
            if char_code > ord('z'):
                char_code -= 26

            elif char_code < ord('a'):
                char_code += 26

        encrypted_text += chr(char_code)
    else:
        encrypted_text += each

print "Encrypted text: " + encrypted_text

shift = -shift

for each in encrypted_text:
    if each.isalpha():
        char_code = ord(each)
        char_code += shift

        if each.isupper():
            if char_code > ord('Z'):
                char_code -= 26

            elif char_code < ord('A'):
                char_code += 26

        if each.islower():
            if char_code > ord('z'):
                char_code -= 26

            elif char_code < ord('a'):
                char_code += 26

        decrypted_text += chr(char_code)
    else:
        decrypted_text += each

print "Decrypted text: " + decrypted_text