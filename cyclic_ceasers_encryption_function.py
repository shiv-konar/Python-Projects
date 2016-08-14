plain_text = raw_input("Enter plain text: ")
shift = int(raw_input("Enter shift (1-26): "))


def ceasersencryptiondecryption(text, shift, convert):
    converted_text = ""

    if convert.lower() == "decrypt":
        shift = -shift

    for each in text:
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

            converted_text += chr(char_code)
        else:
            converted_text += each
    return converted_text

encrypted_text = ceasersencryptiondecryption(text=plain_text, shift=shift, convert="encrypt")
print "Plain text: " + plain_text
print "Encrypted text: " + encrypted_text

decrypted_text = ceasersencryptiondecryption(text=encrypted_text, shift=shift, convert="decrypt")
print "Decrypted text: " +  decrypted_text