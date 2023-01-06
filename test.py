total_length = 0
count = 0
while True:
    word = input("Enter a word: ")
    if word.lower() == "q" or word.lower() == "quit":
        if count == 0:
            break
        else:
            average_length = total_length / count
            print(f"The average word length is: {average_length}.")
            break
    else:
        total_length += len(word)
        count += 1

