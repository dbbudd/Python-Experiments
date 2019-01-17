def simpleMatcher(pattern, text):
    i=0
    j=0
    match = False
    stop = False
    while not match and not stop:
        if text[i] == pattern[j]:
            i=i+1
            j=j+1
        else:
            i=i+1
            j=0

        if j == len(pattern):
            match = True
        else:
            if i == len(text):
                stop = True

    if match:
        return i-j
    else:
        return -1
