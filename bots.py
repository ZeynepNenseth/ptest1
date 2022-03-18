import random

good_actionList = ["study", "train", "cook", "work", "read", "self-esteem", "walk"]
bad_actionList = ["fight", "steal", "swear", "stalk", "shout", "gossip", "bomb"]
extra_actionList = ["jogg", "day-dream", "ski", "picnick"]
all_actionList = good_actionList + bad_actionList

def alice(a, b = None):
    if b is None & a is good_actionList:
        return "{} sounds like a good idea".format(a + "ing")
    elif b is not None & a is bad_actionList:
        return "Hmmm, I am not sure about {}. Can we not {} instead?".format(a + "ing", random.choice(b))
    else:
        return "I will join you for whatever you are planning."

def bob(a, b = None):
    if b is None:
        return "I guess I could hang out with you for {}.".format(a + "ing")
    else:
        return "Yeah, {} is possible. But could we also consider {}?".format(a + "ing", b + "ing")

def musti(a, b = None):
    if b is None & a is bad_actionList:
        return "I agree with Alice. {} is not a good idea.".format(a + "ing")
    elif b is not None & b is bad_actionList:
        return "I would choose {} or {} in the forest rather than {}.".format(a + "ing", random.choice(extra_actionList), b + "ing")

def hellokitty(a, b = None):
    if b is None:
        return "{} might be fun!".format(a + "ing")
    elif a & b is all_actionList:
        return "We did {} last time as well;-( We could try {} or {} this time.".format(a, b, random.choice(extra_actionList))
    else:
        return "{} is fine for me! Let's move then!".format(a + "ing")


