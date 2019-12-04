from menubar_methods import *
from variables import win
from find_replace import searching, replace

close_icon = PhotoImage(file='images/close_icon2.png')
close_button = Button(master=tools_frame, text='x', font=(None, 10), bd=0, command=show_toolbar, bg='#212121', fg='white')
close_button.pack(side=RIGHT, padx=0)

# close_button.config(master=win)

new_file_icon = PhotoImage(file='images/new_file_icon2.png')
new_file_button = Button(tools_frame, bg='#212121', image=new_file_icon, bd=0, command=new_file)
new_file_button.pack(side=LEFT, padx=2)

open_file_icon = PhotoImage(file='images/open_file_icon2.png')
open_file_button = Button(tools_frame, bg='#212121', image=open_file_icon, bd=0, command=open_file)
open_file_button.pack(side=LEFT, padx=2)

save_icon = PhotoImage(file='images/save_file_icon2.png')
save_button = Button(tools_frame, bg='#212121', image=save_icon, bd=0, command=save_file)
save_button.pack(side=LEFT, padx=2)

cut_icon = PhotoImage(file='images/cut_icon.png')
cut_button = Button(tools_frame, bg='#212121', image=cut_icon, bd=0, command=cut)
cut_button.pack(side=LEFT, padx=2)

paste_icon = PhotoImage(file='images/paste_icon.png')
paste_button = Button(tools_frame, bg='#212121', image=paste_icon, bd=0, command=paste)
paste_button.pack(side=LEFT, padx=2)

copy_icon = PhotoImage(file='images/copy_icon.png')

copy_button = Button(tools_frame, bg='#212121', image=copy_icon, bd=0, command=copy)
copy_button.pack(side=LEFT, padx=2)

undo_icon = PhotoImage(file='images/undo_icon.png')
undo_button = Button(tools_frame, bg='#212121', image=undo_icon, bd=0, command=undo)
undo_button.pack(side=LEFT, padx=2)

redo_icon = PhotoImage(file='images/redo_icon.png')
redo_button = Button(tools_frame, bg='#212121', image=redo_icon, bd=0, command=redo)
redo_button.pack(side=LEFT, padx=2)

select_all_icon = PhotoImage(file='images/select_all_icon.png')
select_all_button = Button(tools_frame, bg='#212121', image=select_all_icon, bd=0, command=select_all)
select_all_button.pack(side=LEFT, padx=2)

search_icon = PhotoImage(file='images/search_icon.png')
search_button = Button(tools_frame, bg='#212121', image=search_icon, bd=0, command=searching)
search_button.pack(side=LEFT, padx=2)

replace_icon = PhotoImage(file='images/replace_icon2.png')
replace_button = Button(tools_frame, bg='#212121', image=replace_icon, bd=0, command=replace)
replace_button.pack(side=LEFT, padx=2)
font_decrease_icon = PhotoImage(file='images/font_decrease.png')
font_decrease_button = Button(tools_frame, bg='#212121', image=font_decrease_icon, bd=0, command=decrease_font)
font_decrease_button.pack(side=LEFT, padx=2)

font_increase_icon = PhotoImage(file='images/font_increase.png')
font_increase_button = Button(tools_frame, bg='#212121', image=font_increase_icon, bd=0, command=increase_font)
font_increase_button.pack(side=LEFT, padx=2)
