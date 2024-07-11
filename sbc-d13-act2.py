characters = ["!", "\"", "#", "$", "%", "&", "'", "(", ")", "*", "+", ",", "-", ".", "/", ":", ";", "<", "=", ">", "?", "@", "[", "\\", "]", "^", "_", "`", "{", "|", "}", "~"]

words = "Hai hello how are you? hello! hai huhayyy!"

value = []
sys = []
tmp = ""

for i in words:
    if i in characters:
        if tmp:
            value.append(tmp.strip())
            sys.append(tmp.strip() + i)
            tmp = ""
        else:
            if sys:
                sys[-1] += i
    else:
        tmp += i
if tmp:
    value.append(tmp.strip())
    sys.append(tmp.strip())

print(value)
print(sys)


