from sys import argv

script, filename= argv

txt = open(filename) # opens the file that you entered after the script(ex15.py) name to have access

print(f"Here's your file {filename}") # printing the filename of the file
print(txt.read()) # printing the opened file you entered before
print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
