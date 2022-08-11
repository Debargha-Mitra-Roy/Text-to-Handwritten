import pywhatkit as pw
from PIL import Image
import string
import random

print("INSTRUCTIONS :-")
print("1. Open file.txt")
print("2. Enter the paragraph in file.txt")
print("3. Close it")
print("4. Run the program")
print("5. Enter your text color (Blue / Black / Red / Green)")

# initializing size of string
N = 7

# using random.choices() generating random strings
res = ''.join(random.choices(string.ascii_letters, k=N))

# Convert the string to a .png extention
res = res + ".png"

color = input("Enter your text color (blue / black / red / green) : ")

r, g, b = 0, 0, 0

if color == "blue":
    r, g, b = 0, 0, 138

if color == "black":
    r, g, b = 0, 0, 0

if color == "red":
    r, g, b = 255, 0, 0

if color == "green":
    r, g, b = 0, 177, 64

with open('./file.txt') as txt:
    lines = txt.read()

pw.text_to_handwriting(lines, res, [r, g, b])

print("Thanks for using our service. Your file is ready to use.")

# Open the file in reading mode
demo = Image.open(res, 'r')
demo.show()
