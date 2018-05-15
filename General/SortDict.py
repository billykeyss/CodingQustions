def sort_dict(dictionaryInput):
    return sorted(dictionaryInput, key=lambda x:x[1])

print sort_dict({"a":7, "b":1, "c":5, "d":3})
