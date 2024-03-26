while True:
    sentence_input = input("Input sentence here: ").upper()

    frequency = {}
    
    for char in sentence_input: 

        if char == ' ':

            continue

        if char in frequency:

            frequency[char] += 1

        else:
            
            frequency[char] = 1
        

    print(str(frequency))