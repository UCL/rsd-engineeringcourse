def greet(personal, family, title="", polite=False):
    greeting= "How do you do, " if polite else "Hey, "
    if title:
        greeting+=title+" "

    greeting+= personal + " " + family +"."
    return greeting
