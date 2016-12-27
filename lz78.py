def find_in_dict(string, dictionary):
    number = 0
    for i in range(number, len(dictionary)):
        from_dict = dictionary[i]
        size = len(from_dict)

        if from_dict == string[:size]:
            number = i

    return number


def compress(message, dictionary_size=12):
    dictionary = [""]

    test = ""
    output = []
    while len(message) > 0:
        number = find_in_dict(message, dictionary)
        size = len(dictionary[number])

        message = message[size:]

        character = message[:1]
        message = message[1:]

        dictionary.append(dictionary[number] + character)
        test += dictionary[number] + character
        output.append((number, character))

    return output


def decompress(compressed_message):
    message = ""

    dictionary = [""]
    for part in compressed_message:
        number, character = part

        substring = dictionary[number] + character
        dictionary.append(substring)
        message += substring
    return message
