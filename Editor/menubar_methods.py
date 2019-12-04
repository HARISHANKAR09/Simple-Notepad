from tkinter import filedialog as fd, messagebox as mb
from tkinter import colorchooser as cc
from datetime import datetime
from variables import *
import variables as v
from highlighting import highlight_keyword

# mylist = ["1"]
# var = StringVar(value=mylist)
# listbox.config(listvariable=var)



def line_number(event=None):
    # string_finder()
    modified() # global location_of_cursor
    textArea.tag_remove("highlight", '1.0', "end")
    row, col = textArea.index(INSERT).split(".")
    line , column = str(int(row)), str(int(col)+1)
    v.location_of_cursor.set(f"Ln {line}, Col {column}\t\t")
    return None


def increase_font(event=None):
    # global font_style, font_size
    if v.font_size <= 60:
        v.font_size += 1
        customFont.config(size=v.font_size)
        line_num_panel.update_idletasks()
        textArea.config(font=(v.font_style, v.font_size))



def decrease_font(event=None):
    if v.font_size >= 10:
        v.font_size -= 1
        customFont.config(size=v.font_size)
        line_num_panel.update_idletasks()
        textArea.config(font=(v.font_style, v.font_size))



def font_reset(event=None):
    v.font_size = 20
    customFont.configure(size=v.font_size)
    textArea.config(font=(v.font_style, v.font_size))

# Check for v.file is saved or not set * on window title
def modified(event=None):
    if v.file == None:
        if textArea.edit_modified() == 1:
            win.title("Untitled  -Notepad*")
    else:
        if textArea.edit_modified() == 1:
            win.title(str(v.file.name) + "   -Notepad*")
        else:
            win.title(str(v.file.name) + "   -Notepad")


def new_file(event=None):
    # global v.file
    if v.file == None:
        confirm_on_new_file()
        line_number()
        modified()
        return
    else:
        confirm_on_new_file()
        line_number()
        modified()
        return


def open_file(event=None):
    # global v.file
    confirm_on_new_file()
    v.file = fd.askopenfile(title="Choose file to open", filetypes=[("Text(default)", "*.txt"), ("Python", "*.py"),
                                                                  ("Java", "*.java"), ("JavaScript", "*.js"),
                                                                  ("HTML", "*.html"), ("CSS", "*.css"),
                                                                  ("All files", "*.*")])
    if v.file is None:
        return
    else:
        # global v.file_name
        # textArea.edit_modified(arg=False)
        textArea.delete("1.0", END)
        textArea.insert("1.0", v.file.read())
        win.title(str(v.file.name) + " -Notepad")
        textArea.mark_set(INSERT, 1.0)  # Set caret(cursor) position at 1.0
        print("Opened")
        # v.file_name = v.file.name
        v.file.close()
        line_number()
        textArea.edit('reset')
        textArea.edit_modified(arg=False)
        # modified()
        highlight_keyword()
        return True


def save_file(event=None):
    # global v.file
    if v.file == None:
        v.file = fd.asksaveasfile(title="Save v.file", defaultextension=".txt",
                                filetypes=[("Text(default)", "*.txt"), ("Python", "*.py"),
                                           ("Java", "*.java"), ("JavaScript", "*.js"),
                                           ("HTML", "*.html"), ("CSS", "*.css"),
                                           ("All files", "*.*")])
        if v.file == None:
            return None
        else:
            v.file.write(textArea.get("1.0", "end-1c"))
            win.title(str(v.file.name) + " -Notepad")
            # v.file_name = v.file.name
            v.file.close()
            print("Saved..")
            textArea.edit_modified(arg=False)
            # print(v.file)
            modified()
            highlight_keyword()
            return True
    else:
        v.file = open(v.file.name, "w+")
        v.file.write(textArea.get("1.0", "end-1c"))
        win.title(str(v.file.name) + "  -Notpad")
        # v.file_name = v.file.name
        v.file.close()
        print("Saved..")
        textArea.edit_modified(arg=False)
        modified()
        highlight_keyword()
        return True


def save_as_file(event=None):
    # global v.file
    v.file = fd.asksaveasfile(title="Save as", defaultextension=".txt",
                            filetypes=[("Text(default)", "*.txt"), ("Python", "*.py"), ("Java", "*.java"),
                                       ("All files", "*.*")])
    if v.file == None:
        return
    else:
        v.file.write(textArea.get("1.0", "end-1c"))
        # v.file_name = v.file.name
        v.file.close()
        win.title(str(v.file.name) + " -Notepad")
        textArea.edit_modified(arg=False)
        print("Saved As...")
        highlight_keyword()


def exit():
    win.destroy()


def cut():
    textArea.event_generate('<<Cut>>')


def copy():
    textArea.event_generate('<<Copy>>')


def paste():
    # keywordss()
    textArea.event_generate('<<Paste>>')
    highlight_keyword()


def font_color():
    color = cc.askcolor()
    textArea.config(fg=color[1])


# --------------------------------
hide = 1

def hide_statusbar():
    global hide
    if hide == 1:  # hiding
        bottom_frame.pack_forget()
        hide = 0
    elif hide == 0:  # displaying
        top_frame.pack_forget()
        bottom_frame.pack(side=BOTTOM, fill=X)
        top_frame.pack(side=TOP, expand=1, fill=BOTH)
        hide = 1


# ---------------------------------

clicked = 1

def show_toolbar():
    global clicked, hide
    if clicked == 0:      # displaying
        top_frame.pack_forget()
        bottom_frame.pack_forget()
        line_num_panel.pack_forget()
        tools_frame.pack(fill=X, pady=(0, 1))
        if hide == 1:     # displaying status bar
            bottom_frame.pack(side=BOTTOM, fill=X)
        line_num_panel.pack(side=LEFT, fill=BOTH)
        top_frame.pack(side=TOP, fill=BOTH, expand=1)
        Toolbars.entryconfigure(1, label="       Hide toolbar                ")
        clicked = 1
    elif clicked == 1:    # hiding
        tools_frame.pack_forget()
        Toolbars.entryconfigure(1, label="       Show toolbar                ")
        clicked = 0


def about():
    mb.showinfo("About", "Notepad Version : 1.0\nDeveloped by HARISH JANGID")


def undo(event=None):
    textArea.event_generate('<<Undo>>')


def redo(event=None):
    textArea.event_generate('<<Redo>>')
    highlight_keyword()


def select_all(event=None):
    textArea.tag_add("sel", "1.0", "end-1c")
    return "break"  # Deleting default Control + a select event

# ------------
def theme_color():
    textArea.config(bg="#2b2727", insertbackground="white", fg="white")


def default_theme():
    textArea.config(bg="white", insertbackground="black", fg="black")


def date_time():
    now = datetime.now()
    textArea.insert(INSERT, str(now.strftime("%I:%M %p  %d-%m-%Y")))





def word_wrap():
    if wrap1.get() == 0:
        textArea.config(wrap=NONE)
    elif wrap1.get() == 1:
        textArea.config(wrap=WORD)




def confirm_on_new_file(event=None):
    # global v.file
    if textArea.edit_modified() == 1:
        if v.file == None:
            text_length = len(textArea.get("1.0", "end-1c"))
            if text_length == 0:
                textArea.delete("1.0", END)
                line_number()
                win.title("Untitled  -Notepad")
                textArea.edit('reset')
                textArea.edit_modified(arg=False)
            else:
                confirm_box_on_new_file()
        else:
            confirm_box_on_new_file()
    else:
        textArea.delete("1.0", END)
        line_number()
        win.title("Untitled  -Notepad")
        textArea.edit('reset')
        textArea.edit_modified(arg=False)
        v.file = None
# ---------------

def confirm_box_on_new_file():
    # global v.file
    ans = mb.askyesnocancel("Save file", "Do you want to save this v.file ?")
    print(ans)
    if ans is True:
        print("True")
        saved = save_file
        if saved is True:
            textArea.delete("1.0", END)
            line_number()
            textArea.edit('reset')
            textArea.edit_modified(arg=False)
            v.file = None
            win.title("Untitled  -Notepad")
        else:
            return
    elif ans is False:
        v.file = None
        textArea.delete("1.0", END)
        line_number()
        win.title("Untitled  -Notepad")
        textArea.edit('reset')
        textArea.edit_modified(arg=False)
    elif ans is None:
        print("Nott")
        return





