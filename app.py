# dataannotation

in_file = "coding_qual_input.txt"
# in_file = "small.txt"


def read_encoder(file_path):
    encoded_words = {}

    with open(file_path, "r") as file:
        for line in file:
            items = line.split(" ")
            encoded_words[items[0]] = items[1]

    return encoded_words


def read_pyramid(file_path):
    keys = []
    with open(file_path, "r") as file:
        for line in file:
            items = line.split(" ")
            keys.append(items[-1].rstrip())
    return keys


encoded_pairs = read_encoder(in_file)
keys_to_read = read_pyramid("pyramid_01.txt")

for key in keys_to_read:
    print(f"{key}: {encoded_pairs[key].rstrip()}")
