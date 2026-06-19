sentence = input("Enter a sentence: ")

print("Words:", len(sentence.split()))
print("Characters:", len(sentence))
print("Lowercase:", sentence.lower())
print("Uppercase:", sentence.upper())
print("With underscores:", sentence.replace(" ", "_"))
