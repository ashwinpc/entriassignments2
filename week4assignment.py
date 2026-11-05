def has_unique_chars(s):
    k = ""

    for i in s:
        if i in k:
            return False
        else:
            k += i

    return True


s = input("Enter a string: ")

print(has_unique_chars(s))