pref = ["handpicked", "top 10", "best", "most interesting", "creative", "wonderful"] #
what = ["toys", "amazon toys", "baby toys", "wooden toys", "toys for toddlers"]
usage = [""]

for a in pref:
    for b in what:
        for c in usage:
            print("{} {} {}".format(a,b,c))