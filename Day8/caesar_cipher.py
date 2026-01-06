import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        
# def encrypt(original_text, shift_amount):
#             cipher_text = ""

#             for char in original_text:
#                 shifted_position = alphabet.index(char) + shift_amount

#                 shifted_position = shifted_position % len(alphabet)

#                 cipher_text += alphabet[shifted_position]
            
#             print(f"Here is the encoded result: {cipher_text}") 
# encrypt(text,shift)

# def decrpyt(original_text, shift_amount):
#             output_text = ""

#             for char in original_text:
#                 shifted_position = alphabet.index(char) - shift_amount

#                 shifted_position = shifted_position % len(alphabet)

#                 cipher_text += alphabet[shifted_position]
            
#             print(f"Here is the decoded result: {output_text}") 
        
# decrpyt(text,shift)  

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
                    shift_amount *= -1

    for letter in original_text:

            if letter not in alphabet:
               output_text += letter

            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position = shifted_position % len(alphabet)
                output_text += alphabet[shifted_position]
        
    print(f"Here is the {encode_or_decode}d result: {output_text}")

should_contine = True
while should_contine:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text,shift_amount=shift,encode_or_decode=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()

    if restart == 'no':
         should_contine = False
         print("Goodbye...")

