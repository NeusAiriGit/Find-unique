InputString = "A"
InputString = list(InputString)
firstLetter = False

if len(InputString) == 1:
    UniqueString = InputString
    UniqueString = "".join(UniqueString)
else:
    for i in range(0,len(InputString),2):
        if i <= len(InputString)-3:

            if InputString[i] == InputString[i+1]:
                
                pass
            else:
                UniqueString = list(InputString[i] + InputString[i+1])
                if InputString[i+1] ==InputString[i+2]:
                    UniqueString.pop(-1)
                    UniqueString = "".join(UniqueString)
                    break
        else:
            UniqueString = InputString[-1]

print(UniqueString)