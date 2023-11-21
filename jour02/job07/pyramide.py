# Programme pour afficher une suite pyramidale

def pyramid(s):
    length = len(s)
    for i in range(length):
        print(s[:i+1])

s = "abcdefghijklmnopqrstuvwxyz" * 10
pyramid(s)