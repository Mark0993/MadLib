print("Welcome to the the ridiculous world of Mab Lib where you create some crazy stories")
print("You will need to enter some words below to build they story")

user_words = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": "", "9": "", "10": "",
               "11": "", "12": "", "13": "", "14": "", "15": "", "16": "", "17": "", "18": "", "19": "", "20": ""}



user_words["1"] = input("Please enter a Proper Noun (A persons name): ")
user_words["2"] = input("Please enter an Noun: ")
user_words["3"] = input("Please enter Adjective: ")
user_words["4"] = input("Please enter a Verb: ")
user_words["5"] = input("Please enter an Adjective: ")
user_words["6"] = input("Please enter an Animal: ")
user_words["7"] = input("Please enter a Verb: ")
user_words["8"] = input("Please enter a Colour: ")
user_words["9"] = input("Please enter a Verb ending in 'ing': ")
user_words["10"] = input("Please enter an Adverb ending in 'ly: ")
user_words["11"] = input("Please enter a Number: ")
user_words["12"] = input("Please enter a Measure of Time: ")
user_words["13"] = input("Please enter a Colour: ")
user_words["14"] = input("Please enter an Animal: ")
user_words["15"] = input("Please enter a Number: ")
user_words["16"] = input("Please enter a Silly Word: ")
user_words["17"] = input("Please enter a Noun: ")

[print(f"{key}: {value}") for key, value in user_words.items()] # - testing

print("You have created a crazy madlib: ")

print(f"""This weekend I am going camping with {user_words['1']}. I packed my lantern, sleeping bag, and,
{user_words['2']}. I am so {user_words['3']} to {user_words['4']} in a tent. I am {user_words['5']} we
might see a {user_words['6']}, they are kind of dangerous. We are going to hike, fish, and {user_words['7']}.
I have heard that the {user_words['8']} lake is great for {user_words['9']}. Then we will
{user_words['10']} through the forest for {user_words['11']} {user_words['12']}. If I see a
{user_words['13']} {user_words['14']} while hiking, I am going to bring it home as a pet! At night we will tell
{user_words['15']} {user_words['16']} stories and roast {user_words['17']} around the campfire!!""")

print("That certinaly is a crazy story")
