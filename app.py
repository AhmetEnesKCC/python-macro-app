
import keyboard
import pythoncom
from PyHook3 import cpyHook,HookConstants
from tkinter import *
from macro import mouse_macro

# Functions

macro = ''
result = ''
result_name = ''
selected_button = ''
XBUTTON1 = 0x0001
XBUTTON2 = 0x0002
times = 0


def selected_1():
    global selected_button
    selected_button = XBUTTON1
    macro_variable.set('Side Button 1')

def selected_2():
    global selected_button
    selected_button = XBUTTON2
    macro_variable.set('Side Button 2')


def set_macro():
    pass


def get_result():
    global result_variable
    global result
    print(keyboard.read_key())
    result = keyboard.read_key()
    result_variable.set(f'{result}')


def run():
    global times
    times = times_input.get()
    times = int(times)
    mouse_macro(selected_button, times, result)

def stop():
    sys.exit()

# Components

root = Tk()
root.geometry('800x600')

container = Frame(root, bg='white', width=800, height=100)
container.pack()
main_title = Label(container, text="Macro App", bg='white', width=800, height=1, font='Calibri 40', pady=10)

main_title.pack()

# Content

content_container = Frame(root, width=300, height=500, bg='white')
content_container.pack(side='left', padx=50)

macro_input_text = Label(content_container, text='Enter Macro: ', bg='white', padx=10)
macro_input_text.place(relwidth=1, relheight=0.1)

macro_select_button_1 = Button(content_container, text="Mouse Side Button 1", command=selected_1)
macro_select_button_1.place(relwidth=0.6, relheight=0.1, rely=0.1, relx=0.20)
macro_select_button_2 = Button(content_container, text="Mouse Side Button 2", command=selected_2)
macro_select_button_2.place(relwidth=0.6, relheight=0.1, rely=0.3, relx=0.20)
macro_variable = StringVar()
macro_variable.set('Your Macro')

result_variable = StringVar()
result_variable.set('Your Result')

macro_show_text = Label(content_container, textvariable=macro_variable)
macro_show_text.place(relwidth=0.5, rely=0.5, relheight=0.1, relx=0.25)

macro_input_text = Label(content_container, text='Enter Macro: ', bg='white', padx=10)
macro_input_text.place(relwidth=1, relheight=0.1)

macro_output_text = Label(content_container, text='Enter Result: ', bg='white', padx=10)
macro_output_text.place(relwidth=1, relheight=0.1, rely=0.6)

macro_output_button = Button(content_container, text="ADD RESULT", command=get_result)
macro_output_button.place(relwidth=0.3, relheight=0.1, rely=0.7, relx=0.35)

macro_show_result = Label(content_container, textvariable=result_variable)
macro_show_result.place(relwidth=0.5, rely=0.85, relheight=0.1, relx=0.25)

# RUN
run_container = Frame(root, width=300, height=500, bg='white')
run_container.pack(side='right', padx=50)

run_button = Button(run_container, text="RUN", command=run)
run_button.place(relwidth=0.5, relheight=0.2, relx=0.25, rely=0.30)



times_text = Label(run_container, text='How Many Times (Number): ', bg='white', padx=10)
times_text.place(relwidth=1, relheight=0.1)

times_input = Entry(run_container, selectborderwidth=10, justify='center')

times_input.place(relwidth=0.4, relx=0.3, relheight=0.05, rely=0.1)

root.title('Macro Master Pro --Beta--')

root.mainloop()
