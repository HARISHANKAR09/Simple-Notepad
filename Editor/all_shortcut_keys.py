from menubar_methods import *
from variables import win, textArea
from highlighting import highlight_keyword
from selected_characters import select
from find_replace import searching, replace, go_to


# All events and key binding

win.bind('<Control-n>', new_file)
win.bind('<Control-N>', new_file)
win.bind('<Control-o>', open_file)
win.bind('<Control-O>', open_file)
win.bind('<Control-s>', save_file)
win.bind('<Control-S>', save_file)
win.bind('<Control-g>', go_to)
win.bind('<Control-G>', go_to)
textArea.bind('<Control-z>', undo)
textArea.bind('<Control-Z>', undo)
textArea.bind('<Control-y>', redo)
textArea.bind('<Control-Y>', redo)
textArea.bind('<Control-a>', select_all)
textArea.bind('<Control-A>', select_all)

# textArea.bind("<FocusIn>", line_number)
textArea.bind("<ButtonRelease>", line_number)
textArea.bind('<Control - +>', increase_font)
textArea.bind('<Control - =>', increase_font)
textArea.bind('<Control-minus>', decrease_font)


textArea.bind("<KeyPress>", line_number)
textArea.bind("<KeyRelease>", highlight_keyword)
textArea.bind("<Control-f>", searching)
textArea.bind("<Control-F>", searching)
textArea.bind("<Control-r>", replace)
textArea.bind("<Control-R>", replace)
textArea.bind("<Control-Shift-r>", font_reset)
textArea.bind("<Control-Shift-R>", font_reset)

textArea.bind("<<Selection>>", select)
win.bind("<KeyPress>", select)
def br(event):
    textArea.insert('insert+1c', '"')
    textArea.mark_set('insert', 'insert-1c')

textArea.bind('<">', br)


