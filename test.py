#10/3/25 Test prep


def language(x):
    t_count = 0
    s_count = 0

    for _ in range(x):
        line = input()
        t_count += line.lower().count('t')
        s_count += line.lower().count('s')

    if t_count > s_count:
        print("English")
    else:
        print("French")


n = int(input())
language(n)