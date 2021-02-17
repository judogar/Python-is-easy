# """ Create a note-taking program. When a user starts it up, it should prompt them for a filename.
# If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file. After they enter the text, it should save the file and exit.
# If they enter a file name that already exists, it should ask the user if they want:
  # A) Read the file
  # B) Delete the file and start over
  # C) Append the file

# If the user wants to read the file it should simply show the contents of the file on the screen. If the user wants to start over then the file should be deleted and another 
# empty one made in its place. If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file. """"

FileList = []
FileName = input("Please enter a file name: ")
FileList.append(FileName)
print("The current files in the list are: ",FileList)
instruction = 0
addedText = 0
import os

if FileName in FileList:
    print("The file already exists, what do you want to do: A) Read the file, B) Delete the file and start over or C) Append the file: ")
    instruction = input("Please enter A, B or C:")
    if instruction == "A":
        open(FileName, "r")
        print(FileName)
    elif instruction == "B":
        os.remove(FileName)
    else:
        addedText= input("Please write what you want to append to the file: ")
        Filename = open(FileName, "a")
        FileName.write(addedText)
else:
    open(FileName, "w")
    input("Enter the text you want to write in the file: ")

# FileName.close()