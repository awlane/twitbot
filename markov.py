from pathlib import Path
import random

#creates "chain" dictonary
markov = dict()

#reads the file into "memory"
def read2(input_text):
    #create an array from the words
    word_array = str.split(input_text)
    #iterate through the array and create assoications between words
    if len(word_array) > 3:
        for x in range(2, len(word_array) - 3):
            if (word_array[x - 2], word_array[x - 1]) in markov:
                markov[(word_array[x - 2], word_array[x - 1])].append(word_array[x])
            else:
                markov[(word_array[x - 2], word_array[x - 1])] = [word_array[x]]

def speak2(length, tweet):
    #Pick a random key to start the output
    seed = random.choice(list(markov))
    word1 = seed[0]
    word2 = seed[1]
    #Capitalizes the first word as to match English grammar conventions, stores in output string
    babble = str.capitalize(word1) + " " + word2
    for x in range(2, length):
            current = random.choice(markov[(word1, word2)])
            babble += (" " + current)
            if "!" in current or "?" in current:
                break
            if tweet and len(current) >= 130:
                break
            word1 = word2
            word2 = current
    return babble

def read3(input_text):
    input_text = input_text.replace("\n", " ")
    input_text = input_text.replace("\r", " ")
    word_array = str.split(input_text)
    if len(word_array) > 4:
        for x in range(3, len(word_array) - 4):
            if (word_array[x - 3], word_array[x - 2], word_array[x - 1]) in markov:
                markov[(word_array[x - 3], word_array[x - 2], word_array[x - 1])].append(word_array[x])
            else:
                markov[(word_array[x - 3], word_array[x - 2], word_array[x - 1])] = [word_array[x]]

def speak3(length, tweet):
    #Pick a random key to start the output
    seed = random.choice(list(markov))
    word1 = seed[0]
    word2 = seed[1]
    word3 = seed[2]
    #Capitalizes the first word as to match English grammar conventions, stores in output string
    babble = str.capitalize(word1) + " " + word2 + " " + word3
    for x in range(3, length):
            current = random.choice(markov[(word1, word2, word3)])
            babble += (" " + current)
            if "!" in current or "?" in current:
                break
            if tweet and len(babble) >= 130:
                break
            word1 = word2
            word2 = word3
            word3 = current
    return babble