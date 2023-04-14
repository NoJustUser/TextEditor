from cgitb import text
from tkinter import *

# This is a simple text editor. Input in the single-line field file name (1.txt) 
# Put open for watching file contents, write something in the multiline field below
# Then put save for saving your content.

def open_file():

    fail_content.delete(1.0, END)
    f = open(var.get(), 'r')
    content = f.readlines()
    for i in range(len(content)-1, -1, -1):  # Бежим по списку с конца, с шагом -1
        fail_content.insert(1.0, content[i])
    f.close()
    return content


def save_file():

    f = open(var.get(), 'w')
    content = fail_content.get(1.0, END)
    f.write(content)
    f.close()
    fail_content.delete(1.0, END)
    info_message = 'Текст успешно сохранен в файле : ' + var.get()
    fail_content.insert(1.0, info_message)


root = Tk()

frame = Frame()
frame.pack()

var=StringVar()
_file_name = Entry(frame, textvariable = var, width=41).pack(side = LEFT)
btn_open = Button(frame, text = 'Открыть', command = open_file).pack(side = LEFT)
btn_save = Button(frame, text = 'Сохранить', command = save_file).pack(side = LEFT)


fail_content = Text(root, width = 45, height = 25)
scroll = Scrollbar(command=fail_content.yview)
scroll.pack(side = RIGHT, fill = Y)
fail_content.config(yscrollcommand=scroll.set)

fail_content.pack()

root.mainloop()

