def generate():

    """
    pref = ["", "educational", "cheap", "best", "most interesting", "creative", "durable",
            "wonderful", "gift", "montessori", "jigsaw", "chunky", "learning", "play",
            "wooden", "cool", "organic", "zigsaw", "large", "round", "big", "colorful",
            "art", "animals", "sorting", "learn", "shapes", "color recognition", "rainbow",
            "match", "good", "fun", "new", "teaching", "top", "tops", "unique", "unusual", "preschool"]

    what = ["toy", "toys", "puzzle", "puzzles", "gift", "gifts", "cats", "board",
            "game", "games", "set", "figures", "animals", "2018" ]

    usage = ["", "for kids", "for toddlers", "for boys", "for girls", "for children",
             "for kid", "for toddler", "for boy", "for girl", "for babies", "for baby",
             "for age", "for 3", "for 4", "for 5", "for 6", "for 7",
             "for year", "for birthday", "for year old", "for preschoolers", "for brain",
             "sale", "2018"]
    """

    pref = ["", "educational", "cheap", "best", "most interesting", "creative", "durable", "hobby", "blue"
            "wonderful", "gift", "learning", "play", "backyard", "activity", "birding", "bird watching",
             "cool",  "colorful", "party", "travel", "outdoor", "outside", "indoor", "small", "light", "stem",
            "art", "learn", "good", "fun", "new", "teaching", "top", "tops", "unique", "unusual", "preschool"]

    what = ["", "toy", "toys", "gift", "gifts", "binocular", "binoculars", "activity",
            "game", "games", "set", "accessory", "stuff", "things", "party", "gadget"]

    usage = ["", "for kids", "for toddlers", "for boys", "for girls", "for children",
             "for kid", "for toddler", "for boy", "for girl", "for babies", "for baby",
             "for age", "for 3", "for 4", "for 5", "for 6", "for car trip",
             "for year", "for birthday", "for year old", "for preschoolers", "for brain",
             "sale", "2018", "for grandson", "for granddaughter"]

    res = []
    for a in pref:
        for b in what:
            for c in usage:
                phrase = "{} {} {}".format(a,b,c).replace("  ", " ").replace("  ", " ").strip()
                #print(phrase)
                res.append(phrase)
    return res