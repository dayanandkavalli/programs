def transform_string(s):
    ascii_values = []
    transformed_string = list(s)
    length = len(s)
    for i in range(length):
        ascii_val = ord(s[i])

        if ascii_val % 2 == 0:
            if i < length - 1 and not transformed_string[i + 1].isdigit():
                next_ascii_val = (ascii_val % 7) + ord(s[i + 1])
                if next_ascii_val > 127:
                    next_ascii_val = 83
                transformed_string[i + 1] = chr(next_ascii_val)
        else:
            if i > 0 and not transformed_string[i - 1].isdigit():
                prev_ascii_val = ord(transformed_string[i - 1]) - (ascii_val % 5)
                if prev_ascii_val < 0:
                    prev_ascii_val = 83
                transformed_string[i - 1] = chr(prev_ascii_val)

        ascii_values.append(str(ascii_val))
    transformed_string = "".join(transformed_string)
    return transformed_string, "-".join(ascii_values)

s = input("Enter a string: ")
transformed_string, ascii_values = transform_string(s)
print("Input string:", s)
print("ASCII values:", ascii_values)
print("Final Answer:", transformed_string)
