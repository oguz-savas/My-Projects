import string

list_of_word = list(string.ascii_letters)

def caesar(start_text, shift_amount, chiper_direction):
    new_word = ""
    for i in start_text:
        index = list_of_word.index(i)
        if chiper_direction == "encode":
            new_index = index + shift_amount
        elif chiper_direction == "decode":
            new_index = index - shift_amount
        new_letter = list_of_word[new_index % len(list_of_word)]
        new_word  += new_letter
    print(new_word)


while True:
    direction = input("Select the operation type (encode/decode): ")
    text = input("Write Your Word: ")
    shift = int(input("Enter Shift Amount: "))

    caesar(text, shift, direction)

    con = input("Do you want to continue(Yes/No: ").lower()
    if con == "no":
        break




