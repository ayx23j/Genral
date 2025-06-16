def createCode(x) :
    codeIdx = 0
    while len(x) > codeIdx :
        if x[codeIdx] == 1 :
            codeIdx = codeIdx + 1
        if x[codeIdx] == 2 :
            codeIdx = codeIdx + 1
        if x[codeIdx] == 2 :
            codeIdx = codeIdx + 1
        if x[codeIdx] == 3 :
            codeIdx = codeIdx + 1
        if x[codeIdx] == 4 :
            codeIdx = codeIdx + 1
        if x[codeIdx] == 5 :
            codeIdx = codeIdx + 1
        if x[codeIdx] == 6 :
            codeIdx = codeIdx + 1
        if x[codeIdx] == 7 :
            codeIdx = codeIdx + 1
        codeIdx = codeIdx + 1
        code = ""
        return(code)

def main():
    while True:
        h = input("Give me the code :   ")
        return(createCode(h))
main()


    



