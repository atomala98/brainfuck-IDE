import tkinter as tk
from tkinter import filedialog
from interpreter import interpret_program

INPUTS = 0
LABELS = 1
BUTTONS = 2

def save_to_file():
    filename = filedialog.asksaveasfilename(defaultextension=".txt", initialdir = ".",title = "Select file",filetypes = ((".txt","*.txt"),("all files","*.*")))
    print(filename)
    if filename != '':
        with open(filename, 'w') as text_file:
            for line in code.get("1.0", tk.END).splitlines():
                text_file.write(line + "\n")

def load_from_file():
    filename = filedialog.askopenfilename(initialdir = ".",title = "Select file",filetypes = ((".txt","*.txt"),("all files","*.*")))
    if filename != '':    
        with open(filename, 'r') as text_file:
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


for row in range(3):
    root.grid_rowconfigure(row, minsize=100)

for col in range(3):
    root.grid_columnconfigure(col, minsize=300)

# input

code = tk.Text(root, width=36)
code.grid(row = INPUTS, column=0)

get_input = tk.Text(root, width=36)
get_input.grid(row = INPUTS, column=1)

output = tk.Label(root, font="Montserrat")
output.place(relx=0, rely=0)
output.grid(row = INPUTS, column=2)

# code higlights config

colormap = {'[': 'blue', 
            ']': 'blue',
            '+': 'green',
            '-': 'green',
            '<': 'red',
            '>': 'red',
            ',': 'grey',
            '.': 'grey'}

def on_key(event):
    text_str = code.get("1.0", "end-1c")
    lines = text_str.splitlines(True)
    for line_index, line in enumerate(lines, start=1):
        for char_index, char in enumerate(line):
            if char in colormap:
                code.tag_add(char, f"{line_index}.{char_index}")
                
            
code.bind('<KeyRelease>', on_key)
for c in colormap:
    code.tag_config(c, foreground=colormap[c])

# instructions

instruction1 = tk.Label(root, text='Put the code here', font="Montserrat", padx=20, pady=20)
instruction1.grid(column=0, row=LABELS)

instruction2 = tk.Label(root, text='Put inputs here', font="Montserrat", padx=20, pady=20)
instruction2.grid(column=1, row=LABELS)

instruction3 = tk.Label(root, text='Output', font="Montserrat", padx=20, pady=20)
instruction3.grid(column=2, row=LABELS)

#save button

save_text = tk.StringVar()
save_btn = tk.Button(root, textvariable=save_text, font="Montserrat", bg="#20bebe", fg="white", height=2, width=15, command=save_to_file)
save_text.set('Save to file')
save_btn.grid(column=0, row=BUTTONS)

# load button

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
