alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(t, s, d):
    end_text = ''
    i = 0
    if d == "encode":
        s *= -1
    while i < len(t):
        if t[i] not in alphabet:
            end_text += t[i]
            i += 1
            continue
        end_text += alphabet[(alphabet.index(t[i])+s)%len(alphabet)]
        i += 1
    print(f"The {d}d text is {end_text}.")

import art
print(art.logo)

while want == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text,shift,direction)
    print("")
    want = input("Do you want to go again? Type yes or no\n").lower()