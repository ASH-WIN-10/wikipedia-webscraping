import urllib.request
from bs4 import BeautifulSoup

def search_and_write(user_Input):
    page = urllib.request.urlopen('https://en.wikipedia.org/wiki/' + user_Input)
    content = page.read().decode("utf-8")

    start_index = content.find("<p>") + 3
    last_index = content.find("</p><")
    paragraph = content[start_index:last_index]

    final_output = BeautifulSoup(paragraph, "html.parser")

    with open("output.txt", "a", encoding="utf-8") as output_file:
        output_file.write(final_output.get_text())
        output_file.write("\n\n")
    print("Done!!\n")

userInput = None
print("Enter 'exit()' to exit!!")
while userInput != "exit()":
    userInput = input("What do you want to search about? ")
    if userInput == "exit()":
        print("Thank you!!")
        break
    else:
        print("Your output is being printed in the file. Please wait...")
    search_and_write(userInput)