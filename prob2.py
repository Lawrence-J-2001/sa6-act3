strings = ["dog", "dolphin", "cat", "mouse", "tiger", "cow"]
strings.sort(key=lambda x: len(x))
strings.sort(key=lambda x: x)

print(strings)