from typing import List, AnyStr


class DictEntry:
    def __init__(self, substring=""):
        self.substring = substring
        self.uses = 0

    def increment_uses(self):
        self.uses += 1

    def new_with(self, character: AnyStr):
        return DictEntry(self.substring + character)

    def __repr__(self):
        return "\"" + self.substring + "\""


def find_in_dict(string: AnyStr, dictionary: List[DictEntry]):
    number = 0
    tmp_size = 0
    for i in range(number, len(dictionary)):
        from_dict = dictionary[i]
        size = len(from_dict.substring)

        if from_dict.substring == string[:size] and size > tmp_size:
            tmp_size = size
            number = i

    return number


def compress(message, dictionary_size=12):
    if dictionary_size <= 1:
        raise ValueError("dictionary size should be 2 or greater")

    dictionary = [DictEntry()]

    output = []
    while len(message) > 0:
        number = find_in_dict(message, dictionary)
        matching_entry = dictionary[number]
        matching_entry.increment_uses()

        message = message[len(matching_entry.substring):]

        character = message[:1]
        message = message[1:]

        dictionary.append(matching_entry.new_with(character))

        output.append((number, character))
        if len(dictionary) >= dictionary_size:
            remove_entry = sorted(dictionary, key=lambda entry: (entry.uses, len(entry.substring)))[0]
            dictionary.remove(remove_entry)

    return output


def decompress(compressed_message, dictionary_size=12):
    if dictionary_size <= 1:
        raise ValueError("dictionary size should be 2 or greater")

    message = ""
    dictionary = [DictEntry()]
    for part in compressed_message:
        number, character = part
        current_entry = dictionary[number]
        current_entry.increment_uses()

        new_entry = current_entry.new_with(character)
        dictionary.append(new_entry)
        message += new_entry.substring

        if len(dictionary) >= dictionary_size:
            remove_entry = sorted(dictionary, key=lambda entry: (entry.uses, len(entry.substring)))[0]
            dictionary.remove(remove_entry)

    return message
