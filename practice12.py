from tkinter import E


letter = '''Dear <|NAME|>
You are selected!
<|DATE|>'''
name = input("Enter your name\n")
date = input("Enter date\n")
letter = letter.replace("<|NAME|", name)
letter = letter.replace("<|DATE|", date)            
print(letter)            