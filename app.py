import tkinter as tk
from interpreter import interpret_program

INPUTS = 0
LABELS = 2
BUTTONS = 3

def save_to_file():
    with open(load_input.get() + '.txt', "w") as text_file:
        for line in code.get("1.0", tk.END).splitlines():
            text_file.write(line + "\n")

def load_from_file():
    with open(load_input.get() + '.txt', "r") as text_file:
        code.delete(1.0, "end")
        code.insert(1.0, text_file.read())

def interpret():
    inputs = read_inputs()
    run_program(inputs)

def read_inputs():
    inputs = []
    text = get_input.get('1.0', tk.END).splitlines()
    for line in text:
        if line:
            inputs.append(int(line))
    return inputs

def run_program(inputs):
    program_code = code.get("1.0", tk.END)
    output["text"] = interpret_program(program_code, 0, [0 for i in range(3000)], inputs)
    print('')

# start
root = tk.Tk()

canvas = tk.Canvas(root, width=800, height=400)
canvas.grid(columns=3)


for row in range(4):
    root.grid_rowconfigure(row, minsize=100)

for col in range(3):
    root.grid_columnconfigure(col, minsize=300)

code = tk.Text(root, width=36, height=30.4)
code.grid(row = INPUTS, rowspan=2, column=0)

get_input = tk.Text(root, width=36)
get_input.grid(row = INPUTS, column=1)

output = tk.Label(root, font="Montserrat")
output.place(relx=0, rely=0)
output.grid(row = INPUTS, column=2)

load_label = tk.Label(root, font="Montserrat", text="File name              ->")
load_label.grid(column=1, row=1)

load_input = tk.Entry(root, font="Montserrat")
load_input.grid(column=2, row=1)

# bottom text
instruction1 = tk.Label(root, text='Put the code here', font="Montserrat", padx=20, pady=20)
instruction1.grid(column=0, row=LABELS)

instruction2 = tk.Label(root, text='Put inputs here', font="Montserrat", padx=20, pady=20)
instruction2.grid(column=1, row=LABELS)

instruction3 = tk.Label(root, text='Output', font="Montserrat", padx=20, pady=20)
instruction3.grid(column=2, row=LABELS)

save_text = tk.StringVar()
save_btn = tk.Button(root, textvariable=save_text, font="Montserrat", bg="#20bebe", fg="white", height=2, width=15, command=save_to_file)
save_text.set('Save to file')
save_btn.grid(column=0, row=BUTTONS)

load_text = tk.StringVar()
load_btn = tk.Button(root, textvariable=load_text, font="Montserrat", bg="#20bebe", fg="white", height=2, width=15, command=load_from_file)
load_text.set('Load file')
load_btn.grid(column=1, row=BUTTONS)

# run button
run_text = tk.StringVar()
run_btn = tk.Button(root, textvariable=run_text, font="Montserrat", bg="#20bebe", fg="white", height=2, width=15, command=interpret)
run_text.set('Run')
run_btn.grid(column=2, row=BUTTONS)

root.mainloop()
