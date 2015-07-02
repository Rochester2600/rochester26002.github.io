# 2600 monthly page content generator
# Generates a mad libs style random content based
# on user input. Used in part of rochester2600.com 
# site generator

import random

with open('nouns.list') as f:
    NOUNS = f.readlines()

def main():
    subject = raw_input("Subject for the meeting: [Choose N to randomize] ")
    examples = ["","",""]
    print("Enter examples of things related to %s." % subject)
    examples[0] = raw_input("Enter first thing: [N to randomize] ")
    examples[1] = raw_input("Enter second thing: [N to randomize] ")
    examples[2] = raw_input("Enter last thing: [N to randomize] ")
    for index, example in enumerate(examples):
        if example.lower() == "n":
            examples[index] = random_subject()

    #randexamples = [random_examples() for x in examples if x.lower() == "n"]


    if subject.lower() == "n":
        subject = random_subject()
    
    invite = random.choice([
        "Join us for",
        "You're invited to",
        "This month will be",
        "Come on down for"
    ])
    title = "Rochester 2600: %s Edition." % subject.title()
    night_desc = random.choice([
        "This meeting",
        "The evening",
        "The Friday night"
    ])
    do_desc = random.choice([
        "will focus on",
        "will pay tribute to",
        "is an homage to",
        "be a celebration of",
    ])
    subject_desc = "all things %s related including" % subject
    example_desc = "%s, %s, and %s." % (examples[0], examples[1], examples[2])
    talk_desc = "This month's talks include:"
    page = [invite, title, night_desc, do_desc, subject_desc, example_desc, talk_desc]
    #print(page)
    page = " ".join(page)
    print page


def random_subject():
    return random.choice(NOUNS).strip()


if __name__ == '__main__':
    main()