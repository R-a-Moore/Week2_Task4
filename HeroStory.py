
text = "There once was a hero. He went to work. The end." # the text used for the story
Hero_name = input("Please enter your name: ") # the hero in the story

def make_story(): # creates the story dictionary
    Story = {
        "start" : "",
        "middle" : "",
        "end" : ""
    }
    set_Story(Story)

def set_Story(Story): # adds the text to the story
    Story["start"] = text[0:22]
    Story["middle"] = text[22:39]
    Story["end"] = text[39:48]
    print_Story(Story)
    set_Story_Hero(Story)

def print_Story(Story): # prints out the story and its attributes
    print(Story)
    print(type(Story))
    print(Story.keys())
    print(Story.values())
    print(Story["start"])
    print(Story["middle"])
    print(Story["end"])

def set_Story_Hero(Story): # adds the hero to the story
    Story["Hero"] = Hero_name
    print("And our brave her was called...", Story["Hero"])

def starter(): # starts off the code
    make_story()

starter()



