def find_shortest_substrings(s, x):
    substrings = []
    for i in range(len(s)):
        for j in range(i + x, len(s) + 1):
            substring = s[i:j]
            if len(substring) == x and substring[0] == substring[-1]:
                substrings.append(substring)
    return substrings

def print_shortest_substrings(s, x):
    substrings = find_shortest_substrings(s, x)
    if not substrings:
        print("Answer: not-found")
    else:
        print("Answer:", " ".join(substrings))

s = input("Enter the string: ")
x = int(input("Enter the number x: "))

print_shortest_substrings(s,x)