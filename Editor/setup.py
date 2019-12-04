from find_replace import confirm_on_win_close, change_font
from selected_characters import select
from all_shortcut_keys import *
from toolbar_top_frame import *
# import menubar_methods as mm


win.title("Untitled  -Notepad")
win.geometry("1100x510")
# win.configure(background="#212121")
win.minsize(500, 300)


def proxy(*args):
    # let the actual widget perform the requested action
    try:
        cmd = (textArea._orig,) + args
        result = textArea.tk.call(cmd)
    except:
        return

    if (args[0] in ("insert", "replace", "delete") or
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
    ):
        textArea.event_generate("<<Change>>", when="tail")
    # print(result)

    # return what the actual widget returned
    return result

textArea._orig = textArea._w + "_orig"
textArea.tk.call("rename", textArea._w, textArea._orig)
textArea.tk.createcommand(textArea._w, proxy)

def line_counters(event=None):
    canvas.delete('all')
    i = textArea.index("@0,0")

    # def findXCenter(canvas, item):
    #     coords = canvas.bbox(item)
    #     print(win.cget('width'))
    #     xOffset = (win.cget('width') / 2) - ((coords[2] - coords[0]) / 2)
    #     return xOffset
    while True:
        dline = textArea.dlineinfo(i)
        if dline is None: break
        y = dline[1]
        linenum = str(i).split(".")[0]
        canvas.create_text(20, y, font=customFont, anchor="nw", text=linenum, fill='white')
        text_length = canvas.bbox('all') # returns a tuple like (x1, y1, x2, y2)
        # print(text_length)
        if text_length is not None:
            width = text_length[2] - text_length[0]
            canvas.config(width=width+35)
            # print(width+35)
        i = textArea.index("%s+1line" % i)

win.bind('<KeyPress>', line_counters)
textArea.bind("<<Change>>", line_counters)
win.bind('<Configure>', line_counters)


tools_frame.pack(fill=X, pady=(0, 1))



textArea.config(padx=3, pady=0, blockcursor=False, relief=FLAT, #bd=0
                insertwidth=2.2, insertbackground="white", height=19, borderwidth=0, highlightthickness=0,
                    font=(font_style, font_size), undo=True, wrap=NONE, spacing1=0.5)

# Coloring for active line for first time
# textArea.tag_add("highlight", f"{1}.0", f"{1}.end+1c")
textArea.tag_config("highlight", background='blue')

y_scrollbar = Scrollbar(top_frame, orient=VERTICAL, command=textArea.yview, bg='#424242', width=16,
                        highlightcolor='#424242')
textArea.config(yscrollcommand=y_scrollbar.set)
# y_scrollbar.config(command=textArea.yview)

y_scrollbar.pack(side=RIGHT, fill=Y)

x_scrollbar = Scrollbar(top_frame, orient=HORIZONTAL)
textArea.config(xscrollcommand=x_scrollbar.set)
x_scrollbar.config(command=textArea.xview)
x_scrollbar.pack(side=BOTTOM, fill=X)




row, col = textArea.index(INSERT).split(".")
line, column = int(row), int(col)+1
location_of_cursor.set(f"Ln {line}, Col {column}\t\t")

selected_chars.config(text="--------------", relief=FLAT)
status_bar = Label(bottom_frame, textvariable=location_of_cursor, relief=FLAT, bg='#212121', fg='white')
status_bar.pack(side=RIGHT)
selected_chars.pack(side=RIGHT, padx=50)

textArea.pack(expand=1, fill=BOTH)
textArea.focus()

bottom_frame.pack(side=BOTTOM, fill=X)
line_num_panel.pack(side=LEFT, fill=BOTH)
# canvas.pack(fill=Y)
# line_num_panel.config(yscrollcommand=y_scrollbar.set)
top_frame.pack(side=TOP, expand=1, fill=BOTH)

# -----------------
# Menus
# -----------------
main_menu.add_cascade(label=" File", menu=File)
File.add_command(label="       New         Ctrl+N       ", command=new_file)
File.add_command(label="       Open        Ctrl+O       ", command=open_file)
File.add_separator()
File.add_command(label="       Save        Ctrl+S       ", command=save_file)
File.add_command(label="       Save as       ", command=save_as_file)
File.add_separator()
File.add_command(label="       Exit       ", command=exit)

# # Edit Menu
main_menu.add_cascade(label="  Edit", menu=Edit)
Edit.add_command(label="       Cut              Ctrl+X        ", command=cut)
Edit.add_command(label="       Copy           Ctrl+C        ", command=copy)
Edit.add_command(label="       Paste           Ctrl+V        ", command=paste)
Edit.add_separator()
Edit.add_command(label="       Undo           Ctrl+Z        ", command=undo)
Edit.add_command(label="       Redo           Ctrl+Y        ", command=redo)
Edit.add_command(label="       Find..          Ctrl+F        ", command=searching)
Edit.add_command(label="       Replace..     Ctrl+R        ", command=replace)
Edit.add_command(label="       Select All    Ctrl+A        ", command=select_all)
Edit.add_separator()
Edit.add_command(label="       Go To..        Ctrl+G        ", command=go_to)

# Toolbar Menu
main_menu.add_cascade(label=" Toolbar", menu=Toolbars)
Toolbars.add_command(label="       Hide toolbar                ", command=show_toolbar)

# Format Menu
main_menu.add_cascade(label="  Format", menu=Format)
Format.add_command(label="       Font..       ", command=change_font)
Format.add_command(label="       Font color       ", command=font_color)
Format.add_command(label="       Set dark theme       ", command=theme_color)
Format.add_command(label="       Set default theme       ", command=default_theme)
# wrap1 = IntVar()
# wrap1.set(0)
Format.add_checkbutton(label="       Word Wrap       ", onvalue=1, offvalue=0, command=word_wrap, variable=wrap1)
Format.add_separator()
Format.add_command(label="       Date/Time       ", command=date_time)
# # View Menu
zoom_menu = Menu(tearoff=0)
zoom_menu.add_command(label="     Zoom In               Control+Plus", command=increase_font)
zoom_menu.add_command(label="     Zoom Out            Control+Minus", command=decrease_font)

zoom_menu.add_command(label="     Zoom Reset         Control+Shift+R", command=font_reset)
main_menu.add_cascade(label="  View", menu=View)
View.add_cascade(label="  Zoom   ", menu=zoom_menu)

View.add_checkbutton(label="       Status Bar       ",  onvalue=1, offvalue=0, command=hide_statusbar, variable=checked)

# Help Menu
main_menu.add_cascade(label="  Help", menu=Help)
Help.add_command(label="       About       ", command=about)


win.protocol("WM_DELETE_WINDOW", confirm_on_win_close)
win.mainloop()
