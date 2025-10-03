#10/3/25 prep for assessment

def language(x):
    if x.count("t") + x.count("T") > x.count("s") + x.count("S"):
        print("THE TEXT IS ENGLISH.")
    elif x.count("t") + x.count("T") < x.count("s") + x.count("S"):
        print("THE TEXT IS FRENCH.")

language()