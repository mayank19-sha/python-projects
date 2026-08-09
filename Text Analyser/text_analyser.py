sentence=input("enter a  sentence: ").strip()

print(sentence.upper())
print(sentence.lower())
print(len(sentence.split()))
print(sentence.replace(" ", "_"))
print(sentence.lower().startswith("the"))
if len(sentence)>10:
    print(sentence[:10])
else:
    print("sentence is too short")