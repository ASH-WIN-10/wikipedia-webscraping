import urllib.request
from bs4 import BeautifulSoup

def search_and_write(user_Input):
    if userInput == "exit()":
        return "Thank you!!"
    
    #opening the file
    out = open('output.txt', 'a', encoding='utf-8')

    page = urllib.request.urlopen('https://en.wikipedia.org/wiki/' + user_Input)
    content = page.read().decode("utf-8")

    start_index = content.find("<p>") + 3
    last_index = content.find("</p><")
    paragraph = content[start_index:last_index]

    final_output = BeautifulSoup(paragraph, "html.parser")
    out.write(final_output.get_text())
    out.write("\n\n")
    #closing the file
    out.close()

userInput = '1'
print("Enter 0 to exit!!")
while userInput!='exit()':
    userInput = input("What do you want to search about? ")
    search_and_write(userInput)
