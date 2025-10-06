#10/3/25 Test prep




# Language determiner
""" def language(x):
    t_count = 0
    s_count = 0

    for _ in range(x):
        line = input("WRITE A SENTENCE FOR THIS LINE.")
        t_count += line.lower().count('t')
        s_count += line.lower().count('s')

    if t_count > s_count:
        print("English")
    elif t_count < s_count:
        print("French")
    else:
        print("French")


n = int(input("WRITE A NUMBER OF LINES."))
language(n)  """




# Parking space

""" n = int(input("WRITE A NUMBER OF PARKING SPACES."))

# Read parking space states
yesterday = input("WRITE THE PARKING SPACES FROM YESTERDAY.")
today = input("WRITE THE PARKING SPACES FROM TODAY.")

# Count spaces occupied both yesterday and today
count = 0
for i in range(n):
    if yesterday[i] == 'C' and today[i] == 'C':
        count += 1

# Output the result
print(f"THE NUMBER OF PARKING SPACES OCCUPIED ON BOTH DAYS ARE {count}.") """