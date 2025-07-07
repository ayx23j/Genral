Ram = []
Registers = []
L_one = []
Programs = []
ProgramListIdx = 0
def reset():
    for i in  1000000:
        Ram.append()
        Registers.append()
        L_one.append()
def start():
    reset()
    answer = ""
    while not answer == "none":
        answer = int(input("Enter a program"))
        Programs.append(answer)
        ProgramListIdx = ProgramListIdx+1
    TimerCPU = 0
    ProgramListIdx = 1
    for i in len(Programs):
        
def Qx_64_CPU(code, codei):
    codes = code
    codeIdx = codei
    for i in len(codes):
        deal1 = 0
        deal2 = 0
        deal3 = 0
        register = 0
        rv = 0
        if code[codeIdx] == 0:
            if codeIdx % 8 == 0:
                Programs.pop()
