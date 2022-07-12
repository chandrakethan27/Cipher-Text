alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
            'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

if shift > 26:
    shift = shift % 26


def caesar(the_text, shift_amount, direction_2):
    if (direction == 'encode'):
        cipher_text = ""
        for char in the_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position + shift_amount
                cipher_text += alphabet[new_position]
            else:
                cipher_text += char
        print(f"The encrypted code is {cipher_text}")

    elif (direction == 'decode'):
        plain_text = ""

        for char in the_text:
            if char in alphabet:
                position = alphabet.index(char)
                new_position = position - shift_amount
                plain_text += alphabet[new_position]
        else:
            plain_text += char
        print(f"The decrpted code is {plain_text}")


caesar(the_text=text, shift_amount=shift, direction_2=direction)






