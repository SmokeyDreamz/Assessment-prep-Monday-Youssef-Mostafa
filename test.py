#10/3/25 Test prep

""" You would like to do some experiments in natural language processing. Natural language processing (NLP) involves
using machines to recognize human languages.
Your first idea is to write a program that can distinguish English text from French text.
After some analysis, you have concluded that a very reasonable way of distinguishing these two languages is to
compare the occurrences of the letters t and T to the occurrences of the letters s and S . Specifically:
if the given text has more t and T characters than s and S characters, we will say that it is (probably)
English text;
if the given text has more s and S characters than t and T characters, we will say that it is (probably)
French text;
if the number of t and T characters is the same as the number of s and S characters, we will say that it is
(probably) French text.
Input Specification
The input will contain the number followed by lines of text, where each line has at least one
character and no more than characters.
Output Specification
Your output will be one line. This line will either consist of the word English (indicating the text is probably English) or
French (indicating the text is probably French). """

# English or French

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
language(n) """








""" You supervise a small parking lot which has parking spaces.
Yesterday, you recorded which parking spaces were occupied by cars and which were empty.
Today, you recorded the same information.
How many of the parking spaces were occupied both yesterday and today?
Input Specification
The first line of input contains the integer . The second and third lines of input contain characters
each. The second line of input records the information about yesterday's parking spaces, and the third line of input
records the information about today's parking spaces. Each of these characters will either be C to indicate an
occupied space or . to indicate it was an empty parking space.
Output Specification
Output the number of parking spaces which were occupied yesterday and today. """

""" # Occupy Parking

n = int(input("HOW MANY PARKING SPACES ARE THERE IN TOTAL."))

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








""" Magnus lost a game of chess to Kile so he found comfort in competitive programming. Very soon, he heard of the
iconic COCI competition and decided to try his luck there.
He wrote a mail to Kile: "Dear Kile, please, prepare me for COCI. Magnus".
Kile replied: "You want to participate in COCI? All right, here's your warm-up task. A series of four consecutive letters of
some word that make up the subword HONI (Croatian acronym for COCI) is called the HONI-block. I will send you the
word of length and you will throw out as many letters as you want (it might be none as well) so that in the end there
are as many HONI-blocks as possible in the word. Kile".
Magnus was very worried and asked you, COCI competitive scene, for help. Help him determine the maximum number
of HONI-blocks he can get in the final word.
Input
The first line contains a word of length , consisting of uppercase letters of the English alphabet.
Output
In the first and only line, print out the required number of HONI-blocks. """

# Contest 3 #1 Magnus



#doesnt work
""" def honifinder(honi):
    HONI = 0
    H = 0
    O = 0
    N = 0
    I = 0
    for i in honi:
        if honi[i] == "H":
            H += 1
            i += 1
            if honi[i] == "O":
                O += 1
                i += 1
                if honi[i] == "N":
                    N += 1
                    i += 1
                    if honi[i] == "I":
                        I += 1
                        i += 1
                        if honi[i] == "H" and honi[i] == "O" and honi[i] == "N" and honi[i] == "I":
                            HONI += 1
    print(HONI)
honifinder("HJJJOOONNNKKKII") """