pref = ["", "fun", "great", "good", "cheap", "child", "kid", "toddler", "young", "preschool",
        "son", "daughter", "sister", "brother", "cousin", "nephew", "grandson", "granddaughter",
        "friend", "solid", "nice", "cool", "top"] #
what = ["", "toy", "gift", "binoculars", "binocs", "present", "birthday"]
usage = ["", "road", "trip", "travel", "beach", "backyard", "party", "favor",
         "yard", "action", "recreation", "outdoor", "indoor", "park",
         "journey", "vacation", "exploring", "spotting", "surveillance",
         "lookout", "spy", "roleplay", "party", "zoo", "circus", "learning"]

for a in pref:
    for b in what:
        for c in usage:
            print("{} {} {}".format(a,b,c))