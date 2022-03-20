import random

good_actionList = ["study", "train", "cook", "work", "read", "self-esteem", "walk"]
bad_actionList = ["fight", "steal", "swear", "stalk", "shout", "gossip", "bomb"]
extra_actionList = ["jogg", "day-dream", "ski", "picnick", "bird-watch", "knitt", "draw"]
all_actionList = good_actionList + bad_actionList


def alice(a, b=None):
    if b is None and a in good_actionList:
        result = "{} sounds like a good idea".format(a + "ing")
        print("Alice: " + result)
        return result

    elif b is not None and a in bad_actionList:
        result = "Hmmm, I am not sure about {}. Can we not {} instead?".format(a + "ing", random.choice(b))
        print("Alice: " + result)
        return result

    else:
        result = "I will join you for whatever you are planning."
        print("Alice: " + result)
        return result


def bob(a, b=None):
    if b is None:
        result = "I guess I could hang out with you for {}.".format(a + "ing")
    else:
        result = "Yeah, {} is possible. But could we also consider {}?".format(a + "ing", b + "ing")
    return result
    print("Bob: " + result)


def musti(a, b=None):
    if b is None and a in bad_actionList:
        result = "I agree with Alice. {} is not a good idea.".format(a + "ing")
    elif b is not None & b in bad_actionList:
        result = "I would choose {} or {} in the forest rather than {}.".format(a + "ing", random.choice(extra_actionList), b + "ing")
    return result
    print("Musti: " + result)

def hellokitty(a, b = None):
    if b is None:
        result = "{} might be fun!".format(a + "ing")
    elif a & b is all_actionList:
        result = "We did {} last time as well;-( We could try {} or {} this time.".format(a, b, random.choice(extra_actionList))
    else:
        result = "{} is fine for me! Let's move then!".format(a + "ing")
    return result
    print("Hellokitty: " + result)

