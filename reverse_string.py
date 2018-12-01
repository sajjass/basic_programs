def reverse_a_string(string_value):
    new_string = []
    index = len(string_value)
    while index:
        index -= 1
        new_string.append(string_value[index])
    return ''.join(new_string)

print reverse_a_string("sudhakar")