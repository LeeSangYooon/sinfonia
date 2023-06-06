import tkinter as tk
from tkinter import filedialog
import subprocess
import os

# Get the path of the 'compiler.py' file relative to 'gui.py'
compiler_path = os.path.join(os.path.dirname(__file__), '..', '..', 'compiler.py')
virtual_machine_path = os.path.join(os.path.dirname(__file__), '..', '..', 'virtualmachine.py')

saved = False
filename = "new_sinfonia_program.sfn"
filepath = ""
def compile_code():
    file_path = file_entry.get()
    if not file_path:
        result_text.configure(state="normal")
        result_text.insert(tk.END, "ERROR: Please select a file. \n")
        result_text.configure(state="disabled")
        highlight_text("error", "ERROR:")
        return -1

    if os.path.splitext(filepath)[1] != '.sfn':
        result_text.configure(state="normal")
        result_text.insert(tk.END, "ERROR: Please select a Sinfonia code (.sfn). \n")
        result_text.configure(state="disabled")
        highlight_text("error", "ERROR:")
        return -1
    
    if not saved:
        result_text.configure(state="normal")
        result_text.insert(tk.END, "ERROR: Please save your code before running it \n")
        result_text.configure(state="disabled")
        highlight_text("error", "ERROR:")
        return -1
    

    try:
        # Run the compiler program using the relative path
        result_text.configure(state="normal")
        result_text.delete(1.0, tk.END)  # Clear previous contents
        result_text.insert(tk.END, "Compiling... \n")
        result_text.update_idletasks()
        result_text.configure(state="disabled")
        result = subprocess.run(["python", compiler_path, file_path], capture_output=True, text=True)
        
        result_text.configure(state="normal")
        if result.returncode == 0:
            # Compiler executed successfully
            output = result.stdout.strip()
            
            result_text.insert(tk.END, output + '\n\n')
            highlight_text("success", "Compiled Successfully")
        else:
            # Compiler returned an error
            error_message = result.stderr.strip()
            result_text.insert(tk.END, error_message)
        result_text.configure(state="disabled")
        return 1

    except Exception as e:
        result_text.configure(state="normal")
        result_text.delete(1.0, tk.END)  # Clear previous contents
        result_text.insert(tk.END, f"ERROR: {str(e)}")
        result_text.configure(state="disabled")
        highlight_text("error", "ERROR:")
        return -1

def run_code():
    virtual_machine_file = file_entry.get()
    if not virtual_machine_file:
        result_text.configure(state="normal")
        result_text.insert(tk.END, "ERROR: Please select a file. \n")
        result_text.configure(state="disabled")
        highlight_text("error", "ERROR:")
        return
    if os.path.splitext(filepath)[1] != '.svmc':
        result_text.configure(state="normal")
        result_text.insert(tk.END, "ERROR: Please select a virtual machine code (.svmc). \n")
        result_text.configure(state="disabled")
        highlight_text("error", "ERROR:")
        return
    

    try:
        # Launch the VirtualMachine program in a new console window
        # Open the command prompt
        input_command = f'python "{os.path.abspath(virtual_machine_path)}" "{os.path.abspath(virtual_machine_file)}"'
        
        result_text.configure(state="normal")  # Enable editing
        result_text.delete(1.0, tk.END)  # Clear previous contents
        result_text.insert(tk.END, f"Virtual Machine is Running {os.path.abspath(virtual_machine_file)} on CMD Console \n")
        result_text.configure(state="disabled")  # Disable editing
        highlight_text("success", "Virtual Machine is Running")
        result_text.update_idletasks()

        os.system(f"start cmd /k {input_command}")

        result_text.update()



    except Exception as e:
        result_text.configure(state="normal")  # Enable editing
        result_text.delete(1.0, tk.END)  # Clear previous contents
        result_text.insert(tk.END, f"ERROR: {str(e)}")
        result_text.configure(state="disabled")  # Disable editing
        highlight_text("error", "ERROR:")

def compile_and_run_code():
    if compile_code() == -1:
        return
    virtual_machine_file = os.path.splitext(file_entry.get())[0] + '.svmc'
    try:
        # Launch the VirtualMachine program in a new console window
        # Open the command prompt
        input_command = f'python "{os.path.abspath(virtual_machine_path)}" "{os.path.abspath(virtual_machine_file)}"'
        
        result_text.configure(state="normal")  # Enable editing
        result_text.insert(tk.END, f"Virtual Machine is Running {os.path.abspath(virtual_machine_file)} on CMD Console \n")
        result_text.configure(state="disabled")  # Disable editing
        highlight_text("success", "Virtual Machine is Running")
        result_text.update_idletasks()

        os.system(f"start cmd /k {input_command}")

        result_text.update()

    except Exception as e:
        result_text.configure(state="normal")  # Enable editing
        result_text.delete(1.0, tk.END)  # Clear previous contents
        result_text.insert(tk.END, f"ERROR:  {str(e)}")
        result_text.configure(state="disabled")  # Disable editing


def on_text_modified(event):
    global saved
    
    # Handle the event here
    if saved:
        saved = False
        filename_label.configure(text=f"{filename} (not saved)")

def select_file():
    global saved, filename, filepath
    file_path = filedialog.askopenfilename(filetypes=[("Sinfonia Files", "*.sfn *.svmc")])
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

    with open(file_path, mode='r') as f:
        code_text.delete(1.0, tk.END) 
        code_text.insert(tk.END, f.read())
        code_text.update()
    
    filename_label.configure(text=os.path.basename(file_path))
    saved = True
    filename = os.path.basename(file_path)
    filepath = file_path
    if os.path.splitext(file_path)[1] == '.svmc':
        code_text.configure(state='disabled') 
    else:
        code_text.configure(state='normal') 
    print(filename)

def save_file():
    global saved, filename, filepath

    if filepath == "":
        filepath = filedialog.asksaveasfilename(filetypes=[("Sinfonia Files", "*.sfn *.svmc")])

    file_entry.delete(0, tk.END)
    file_entry.insert(0, filepath)

    with open(filepath, mode='w') as f:
        f.write(code_text.get("1.0", tk.END))
    
    filename_label.configure(text=os.path.basename(filepath))
    saved = True
    filename = os.path.basename(filepath)


# Function to highlight specific text
def highlight_text(tag, text):
    if tag == 'error': bg = 'red'
    elif tag == 'success': bg = 'yellow'
    else: bg = 'blue'
    start = "1.0"
    end = tk.END
    result_text.tag_configure(tag, background=bg)
    while True:
        pos = result_text.search(text, start, end, count=tk.END)
        if not pos:
            break
        result_text.tag_add(tag, pos, f"{pos}+{len(text)}c")
        start = f"{pos}+1c"



# Create the main Tkinter window
window = tk.Tk()
window.title("Compiler GUI")

# Create a label and entry field for selecting the file
file_label = tk.Label(window, text="Select File:")
file_label.pack()
file_entry = tk.Entry(window, width=200)
file_entry.pack()
browse_button = tk.Button(window, text="Browse", command=select_file)
browse_button.pack()

# Create a button to compile the code
compile_button = tk.Button(window, text="Compile", command=compile_code)
compile_button.pack()

# Create a button to run the code
run_button = tk.Button(window, text="Run", command=run_code)
run_button.pack()

# Create a button to compile and run the code
compile_and_run_button = tk.Button(window, text="Compile and Run", command=compile_and_run_code)
compile_and_run_button.pack()

# Create a button to compile and run the code
save_button = tk.Button(window, text="Save File", command=save_file)
save_button.pack()




result_text = tk.Text(window, height=40, width=90, state='disabled', font=("Consolas", 15))
result_text.pack(side=tk.RIGHT)

# Create a filename label
filename_label = tk.Label(window, text="File: *", font=("Arial", 15), )
filename_label.pack(anchor='w')

code_text = tk.Text(window, height=40, width=100, state='normal', font=("Consolas", 15))
code_text.pack(side=tk.LEFT)
code_text.bind("<Key>", on_text_modified)


start_text = """// Sinfonia 언어 에디터
// sample codes 파일에 샘플 코드가 있습니다.
// 언어에 대한 내용은 레퍼런스 문서를 참조하세요.
// 먼저 빈 .sfn 파일을 만들고 Browse버튼을 눌러 그걸 여세요

// Browse 버튼으로 파일 선택
// Run 버튼으로 기계어 실행
// Compile and Run 버튼으로 Sinfonia 코드를 컴파일하고 실행
// Compile 버튼으로 Sinfonia 코드를 컴파일

"""
code_text.delete(1.0, tk.END) 
code_text.insert(tk.END, start_text)
code_text.update()

def run_gui():
    # Start the Tkinter event loop
    window.mainloop()
    
