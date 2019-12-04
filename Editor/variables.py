from tkinter import *
import tkinter.font as tkFont
win = Tk()
top_frame = Frame(win)
bottom_frame = Frame(win, bd=0, relief=SUNKEN, bg='#212121')
tools_frame = Frame(win, bd=2, relief=FLAT, bg='#212121')
textArea = Text(top_frame, bg='#212121', fg='white')

selected_chars = Label(bottom_frame, bg='#212121', fg='white')



font_style = "Consolas"
font_size = 15

customFont = tkFont.Font(family=font_style, size=font_size)

file = None

line_num_panel = Frame(win, bd=0, borderwidth=0, highlightthickness=0)


# -------------------------------
font_win = None
win2 = None
win3 = None
win2_state = "nothing"
win3_state = "nothing"
font_win_state = "nothing"
# -------------------------------

wrap1 = IntVar()
wrap1.set(0)

checked = IntVar()
checked.set(1)

location_of_cursor = StringVar()

main_menu = Menu(win, background='#212121', foreground='white')
win.config(menu=main_menu)
File = Menu(main_menu, tearoff=0, background='#212121', foreground='white', bd=0, borderwidth=0)
Edit = Menu(main_menu, tearoff=0)
Toolbars = Menu(main_menu, tearoff=0)
Format = Menu(main_menu, tearoff=0)
View = Menu(main_menu, tearoff=0)
Help = Menu(main_menu, tearoff=0)

canvas = Canvas(line_num_panel, width=48, bg='#212121', bd=0, borderwidth=0, highlightthickness=0)
canvas.pack(fill='both', expand=True, padx=(0, 0.5))


