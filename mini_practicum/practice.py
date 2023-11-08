import re

def make_letter_frequency(filename):
    """
    This function opens a file and counts how many alphabet letters were used in a file.
    """
    dict_alphabet = dict()
    with open(filename) as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                # word = re.findall("[a-z]+", word.lower()) <- tried to do something like this to filter out punctuations..
                for ch in word:
                    if ch not in dict_alphabet:
                        dict_alphabet[ch] = 1
                    else:
                        dict_alphabet[ch] += 1
    return dict_alphabet

def print_letter_frequency(dict_of_count):
    """
    This function prints each letter and its frequency on seperate line
    """
    highest_count = 0
    for key in dict_of_count:            
        print(key, dict_of_count[key])

def main():
    filename = 'data/rit_mission.txt'
    freq_dict = make_letter_frequency(filename)
    print_letter_frequency(freq_dict)

main()