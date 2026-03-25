from googletrans import Translator
x = Translator()
text1 = input("Enter any sentence: ")
text2 = input("Enter thelanguage: ")
result = x.translate(text1, dest=text2)
print("Original :", text1)
print("Translated :", result)