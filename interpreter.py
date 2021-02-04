import time

def interpret_program(program, p=0, arr=[x for x in range(3000)], inputs=[]):
    a = 0
    s = ''
    i = 0
    while i < len(program):
        if program[i] == "<":
            p -= 1
        elif program[i] == ">":
            p += 1
        elif program[i] == '.':
            s += chr(arr[p])
        elif program[i] == ',': 
            arr[p] = inputs[a]
            a += 1
        elif program[i] == '+':
            arr[p] += 1
        elif program[i] == '-':
            arr[p] -= 1
        elif program[i] == "[":
            loop = program[i+1:i + program[i:].find(']')]
            i += program[i:].find(']')
            while arr[p] != 0:
                s += interpret_program(loop, p, arr)
        else:
            pass
        if arr[p] == 256:
            arr[p] = 0
        if arr[p] == -1:
            arr[p] = 255
        i += 1
    return s

if __name__ == '__main__':
    print(interpret_program('+++>+++++<[>+<-]++++++[>++++++++<-]>.'))