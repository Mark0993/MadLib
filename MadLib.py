print("Welcome to the the ridiculous world of Mab Lib where you create some crazy stories")
print("You will need to enter some words below to build they story")

user_words = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "",
               "11": "", "12": "", "13": "", "14": "", "15": "", "16": "", "17": "", "18": "", "19": "", "20": ""}



user_words["1"] = input("Please enter a Proper Noun (A persons name): ")
user_words["2"] = input("Please enter an Noun: ")
user_words["3"] = input("Please enter Adjective ")
user_words["4"] = input("Please enter a Verb")
user_words["5"] = input("Please enter an Adjective")
user_words["6"] = input("Please enter an Animal")
user_words["7"] = input("Please enter a Verb")
user_words["8"] = input("Please enter a Colour")
user_words["9"] = input("Please enter a Verb ending in 'ing'")
user_words["10"] = input("Please enter an Adverb ending in 'ly")
user_words["11"] = input("Please enter a Number")
user_words["12"] = input("Please enter a Measure of Time")
user_words["13"] = input("Please enter a Colour")
user_words["14"] = input("Please enter an Animal")
user_words["15"] = input("Please enter a Number")
user_words["16"] = input("Please enter a Silly Word")
user_words["17"] = input("Please enter a Noun")

[print(f"{key}: {value}") for key, value in user_words.items()]

