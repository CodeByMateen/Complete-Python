'''
# REMOVE CURSE WORDS FROM FILE
'''
curse_patterns = ["f**", "s***", "b**", "a**", "p****", "dumbf***", "m***********"]

updated_text = ""
with open("gamma.txt", encoding="utf-8") as file:
    updated_text = file.read()

    for curse in curse_patterns:
        updated_text = updated_text.replace(curse, "")

print(updated_text)

with open("gamma.txt", "w", encoding="utf-8") as file:
    file.write(updated_text)
