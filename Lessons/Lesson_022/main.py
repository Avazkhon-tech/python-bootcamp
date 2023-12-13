# slicing
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
print(piano_keys[2:])
print(piano_keys[:5])
print(piano_keys[2:5:2]) # third one is step
print(piano_keys[::2]) # go from the beginning to the end and skip every second one


piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_tuple[2:4:-1])  # reveres the tuple