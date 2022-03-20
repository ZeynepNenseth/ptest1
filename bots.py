import random

good_actionList = ["study", "train", "cook", "work", "read", "self-esteem", "walk"]
bad_actionList = ["fight", "steal", "swear", "stalk", "shout", "gossip", "bomb"]
extra_actionList = ["jogg", "day-dream", "ski", "picnick", "bird-watch", "knitt", "draw"]
all_actionList = good_actionList + bad_actionList


def alice(a, b=None):
    if b is None and a in good_actionList:
        result = "Alice: {} sounds like a good idea".format(a + "ing")
    elif b is not None and a in bad_actionList:
        result = "Alice: Hmmm, I am not sure about {}. Can we not {} instead?".format(a + "ing", random.choice(b))
    else:
        result = "Alice: I will join you for whatever you are planning."
    return result


def bob(a, b=None):
    if b is None:
        result = "Bob: I guess I could hang out with you for {}.".format(a + "ing")
    else:
        result = "Bob: Yeah, {} is possible. But could we also consider {}?".format(a + "ing", b + "ing")
    return result


def musti(a, b=None):
    if b is None and a in bad_actionList:
        result = "Musti: I agree with Alice. {} is not a good idea.".format(a + "ing")
    elif b is not None & b in bad_actionList:
        result = "Musti: I would choose {} or {} in the forest rather than {}.".format(a + "ing", random.choice(extra_actionList), b + "ing")
    return result


def hellokitty(a, b=None):
    if b is None:
        result = "Hellokitty: {} might be fun!".format(a + "ing")
    elif a & b is all_actionList:
        result = "Hellokitty: We did {} last time as well;-( We could try {} or {} this time.".format(a, b, random.choice(extra_actionList))
    else:
        result = "Hellokitty: {} is fine for me! Let's move then!".format(a + "ing")
    return result

