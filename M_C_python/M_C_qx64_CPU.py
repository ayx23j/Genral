Ram = []
Registers = []
L_one = []
Programs = []
coderidx = []
ProgramListIdx = 0
TimerCPU = 0
CodeIdx = 0
ProgramListIdx = 0
def reset():
    for i in  range(1000000):
        Ram.append("")
        Registers.append("")
        L_one.append("")
def start():
    ProgramListIdx = 0
    reset()
    answer = ""
    while not answer == "none":
        answer = input("Enter a program")
        Programs.append(answer)
        ProgramListIdx = ProgramListIdx+1
    TimerCPU = 0
    ProgramListIdx = 1
    Qx_64_CPU()
    for i in range(len(Programs)):
        coderidx.append(0)
        while True:
            TimerCPU = TimerCPU + .001
            if TimerCPU == .003:
                TimerCPU = 0
                switch()
            if len(Programs) == 1:
                M_C_CODE = Programs[0]
                M_C_CODEIDX = 1
                Qx_64_CPU(M_C_CODE,M_C_CODEIDX)       
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
                Programs.pop(ProgramListIdx)
                quit()
        elif code[codeidx] == 1:
            codeidx = codeidx + 4
            deal1 = deal1 + code[code.index]
            code.index = code.index+1
def switch():
    ProgramListIdx = ProgramListIdx + 1
    TimerCPU = 0
    coderidx[ProgramListIdx] = CodeIdx
    if Programs[ProgramListIdx] == "none":
        ProgramListIdx = 0
        switch() 
        # ???
    M_C_CODE = Programs[ProgramListIdx]
    M_C_CODEIDX = coderidx[ProgramListIdx]
    Qx_64_CPU(M_C_CODE,M_C_CODEIDX)
def startup():
    start()
    quit()