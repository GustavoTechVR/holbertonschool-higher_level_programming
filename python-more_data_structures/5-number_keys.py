#!/usr/bin/python3

def number_keys(a_dictionary):
    count_keys = 0
    for key in a_dictionary:
        count_keys += 1
    return count_keys


if __name__ == "__main__":
    a_dictionary = {'language': "C", 'number': 13, 'track': "Low level"}
    nb_keys = number_keys(a_dictionary)
    print("Número de claves: {:d}".format(nb_keys))
