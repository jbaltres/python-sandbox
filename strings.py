name = "Baltrescu"

text = "Manche Funktionen funktionieren nur mit einem Text"

print(len(name))

letter = name[-2]

print (letter)

letter_range = name[1:4]

print (letter_range)

#String-Methods

upper_name = name.upper()

print (upper_name)

lower_name = name.lower()

print(lower_name)

find_text = text.find("funktionieren")

print(find_text)

find_text2 = text.capitalize()
find_text6 = text.isalnum()

print(find_text2)
print(find_text6)

replace_text = text.replace("einem Text", "einer Fotze")

print(replace_text)