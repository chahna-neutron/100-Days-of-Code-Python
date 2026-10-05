from art import logo

print(logo)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift *= -1

    for letter in text:
        if letter not in alphabet:
          output_text += letter
        else:
          shifted_position = alphabet.index(letter) + shift
          shifted_position %= len(alphabet)
          output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")


should_start=True
while should_start:

 direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
 text = input("Type your message:\n").lower()
 shift = int(input("Type the shift number:\n"))

 caesar(text=text, shift=shift, encode_or_decode=direction)


 input_text=input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
 if input_text == "no":
     should_start=False
     print("Goodbye!")

