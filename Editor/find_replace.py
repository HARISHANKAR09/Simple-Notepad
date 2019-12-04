from variables import *
from tkinter import messagebox as mb
from menubar_methods import save_file
import variables as v

# -------------------------------
font_win = None
win2 = None
win3 = None
win2_state = "nothing"
win3_state = "nothing"
font_win_state = "nothing"
go_to_window = None
go_to_window_state = "nothing"
# -------------------------------


words = None
match = None
def search_words():
    textArea.tag_delete('highlight', "1.0", END)
    global words, match
    start_index = "1.0"
    match = 0
    while True:
        countVar = IntVar()
        start_index = textArea.search(words, start_index, END, count=countVar)
        if start_index:
            end_index = textArea.index('%s+%dc' % (start_index, countVar.get()))
            textArea.tag_add('highlight', start_index, '%s+%dc' % (start_index, countVar.get()))  # add tag to k
            textArea.tag_config('highlight', background='yellow', foreground='red')  # and color it with v
            if countVar.get() == 0:
                break
            else:
                start_index = end_index
                textArea.see('%s+%dc' % (start_index, countVar.get()))
                match += 1
        else:
            break

def searching(event=None):
    from tkinter import ttk
    global win2, win2_state
    if win2_state == "nothing":
        win2 = Tk()
        win2_state = "active"
        win2.title("Find")
        win2.geometry("300x200")
        win2.resizable(0, 0)
        win2.pack_propagate(0)
        # win2.focus_force()
        find = Label(win2, text="Find:", font=(None, 10))
        find.pack(anchor="w", padx=45)
        entry = ttk.Entry(win2, font=(None, 12))
        entry.pack(ipadx=10)
        entry.focus_force()
        matches = Label(win2, text="Matches Found: -")
        matches.pack()

        def search_text(event=None):
            global words, match
            words = entry.get()
            search_words()
            # textArea.tag_delete('highlight', "1.0", END)
            # words = entry.get()
            # start_index = "1.0"
            # match = 0
            # while True:
            #     countVar = IntVar()
            #     start_index = textArea.search(words, start_index, END, count=countVar)
            #     if start_index:
            #         end_index = textArea.index('%s+%dc' % (start_index, countVar.get()))
            #         textArea.tag_add('highlight', start_index, '%s+%dc' % (start_index, countVar.get()))  # add tag to k
            #         textArea.tag_config('highlight', background='yellow', foreground='red')  # and color it with v
            #         if countVar.get() == 0:
            #             break
            #         else:
            #             start_index = end_index
            #             textArea.see('%s+%dc' % (start_index, countVar.get()))
            #             match += 1
            #     else:
            #         break
            if match > 0:
                matches.config(text=f"Matches Found: {match}")
            else:
                matches.config(text="No Matches Found")

        def remove_tag():
            global win2_state
            textArea.tag_delete('highlight')
            win2_state = "nothing"
            win2.destroy()

        win2.protocol("WM_DELETE_WINDOW", remove_tag)
        win2.bind('<KeyPress>', search_text)
        win2.mainloop()
    else:
        win2.focus_force()
        print("already created")




def replace(event=None):
    from tkinter import ttk
    global win3, win3_state
    if win3_state == "nothing":
        win3 = Tk()
        # win3.iconbitmap("icon.ico")
        win3_state = "active"
        win3.title("Replace")
        win3.geometry("600x200")
        win3.resizable(0, 0)
        win3.pack_propagate(0)
        # win3.focus_force()
        label1 = Label(win3, text='Find:', font=(None, 12))
        label1.grid(row=0, column=3, ipadx=5)
        find = ttk.Entry(win3, font=(None, 12))
        find.grid(row=0, column=4, ipadx=20)
        matches = Label(win3, text="Matches Found: -")
        matches.grid(row=0, column=5, ipadx=20)
        label2 = Label(win3, text='Replace:', font=(None, 12))
        find.focus_force()
        label2.grid(row=1, column=3, ipadx=20)
        replace = ttk.Entry(win3, font=(None, 12))
        replace.grid(row=1, column=4, ipadx=20)
        def search_only(event=None):
            global words, match
            words = find.get()
            search_words()
            # textArea.tag_delete('highlight', "1.0", END)
            #
            # global match
            # start_index = "1.0"
            # match = 0
            # while True:
            #     countVar = IntVar()
            #     start_index = textArea.search(words, start_index, END, count=countVar)
            #     if start_index:
            #         end_index = textArea.index('%s+%dc' % (start_index, countVar.get()))
            #         textArea.tag_add('highlight', start_index, '%s+%dc' % (start_index, countVar.get()))  # add tag to k
            #         textArea.tag_config('highlight', background='yellow', foreground='red')  # and color it with v
            #         if countVar.get() == 0:
            #             break
            #         else:
            #             start_index = end_index
            #             textArea.see('%s+%dc' % (start_index, countVar.get()))
            #             match += 1
            #     else:
            #         break
            if match > 0:
                matches.config(text=f"Matches Found: {match}")
            else:
                matches.config(text="No Matches Found")


        def search_with_replace(event=None):
            global match
            textArea.tag_delete('highlight', "1.0", END)
            words_find = find.get()
            words_replace = replace.get()
            start_index = "1.0"
            while True:
                countVar = IntVar()
                start_index = textArea.search(words_find, start_index, END, count=countVar)
                if start_index:
                    end_index = textArea.index('%s+%dc' % (start_index, countVar.get()))
                    # and color it with v
                    if countVar.get() == 0:
                        # mb.showinfo("No Matches", "No matches found")
                        break
                    else:
                        textArea.delete(start_index, end_index)
                        textArea.insert(start_index, words_replace)
                        # textArea.replace(start_index, end_index, words_replace)
                        matches.config(text=f"{match} Matches are Replaced")
                        textArea.tag_add('highlight', start_index,
                                         '%s+%dc' % (start_index, len(words_replace)))
                        textArea.tag_config('highlight', background='yellow', foreground='black')
                        textArea.see('%s+%dc' % (start_index, countVar.get()))
                        start_index = end_index
                        # break
                else:
                    if match == 0:
                        matches.config(text="No Matches Found")
                        mb.showinfo("No Matches", "No matches found")
                        win3.focus_force()
                    break
            match = 0
        def remove_tag():
            global win3_state
            textArea.tag_delete('highlight')
            win3_state = "nothing"
            win3.destroy()

        win3.protocol("WM_DELETE_WINDOW", remove_tag)
        find.bind("<KeyRelease>", search_only)
        btn = ttk.Button(win3, text="Replace", command=search_with_replace)
        btn.grid(row=2, column=4, ipadx=10, ipady=3)
        win3.grid_columnconfigure(3, minsize=100)
        win3.mainloop()
    else:
        win3.focus_force()
        print("already created")


def go_to(event=None):
    from tkinter import ttk
    global go_to_window, go_to_window_state
    if go_to_window_state == "nothing":
        go_to_window = Tk()
        go_to_window_state = "active"
        go_to_window.geometry("300x100")
        go_to_window.title("Go to Line")
        # go_to_window.
        # go_to_window.iconbitmap("icon.ico")
        go_to_window.resizable(0, 0)
        entry = ttk.Entry(go_to_window, font=(None, 14))
        entry.pack(ipadx=10)
        entry.focus_force()

        def go_to_line():
            global go_to_window_state
            line = entry.get()
            if (line.isdigit()):
                textArea.mark_set(INSERT, float(line + ".0"))
                go_to_window.destroy()
                go_to_window_state = "nothing"
                textArea.focus()
                textArea.see(float(line + ".0"))
            else:
                mb.showinfo("Input Handling", "This text box takes only integer input!!")
                entry.focus_force()

        def exit():
            global go_to_window_state
            go_to_window.destroy()
            go_to_window_state = "nothing"

        btn = ttk.Button(go_to_window, text="Go", command=go_to_line)
        btn.pack(ipadx=20)
        btn2 = ttk.Button(go_to_window, text="Cancel", command=exit)
        btn2.pack(ipadx=20)
        go_to_window.protocol("WM_DELETE_WINDOW", exit)
        go_to_window.mainloop()
    else:
        go_to_window.focus_force()
        print("already created")


def change_font():
    global font_win, font_win_state
    if font_win_state == 'nothing':
        from tkinter import ttk
        font_win = Tk()
        font_win_state = 'active'
        font_win.title("Choose font styles")
        # font_win.iconbitmap("icon.ico")
        font_win.geometry("400x500")
        font_win.resizable(0, 0)
        frame = LabelFrame(font_win, text="Choose font style")
        frame.pack()
        listbox = Listbox(frame, font=("Arial Unicode MS", 10), width=30)
        listbox.pack(side=LEFT, fill=Y)
        items = ["ALGERIAN", "Arial Black", "Agency FB", "Bahnschrift Condensed", "Arial Rounded MT Bold",
                 "Arial Unicode MS",
                 "Copperplate Gothic Bold", "Bahnschrift SemiLight", "Bahnschrift Light SemiCondensed",
                 "Bahnschrift SemiBold",
                 "Baskerville Old Face", "Broadway", "Copperplate Gothic Bold", "Elephant", "Baskerville Old Face",
                 "Castellar"]
        for i in items:
            listbox.insert(END, i)
            # listbox.itemconfig(0, {'':''})
        listbox.select_set(0)
        y_scrollbar = Scrollbar(frame, orient=VERTICAL)
        y_scrollbar.config(command=listbox.yview)
        y_scrollbar.pack(side=RIGHT, fill=Y)
        listbox.config(yscrollcommand=y_scrollbar.set)

        def chooseFont():
            global font_win_state
            v.font_style = listbox.get(ACTIVE)
            textArea.config(font=(v.font_style, v.font_size))
            font_win_state = "nothing"
            font_win.destroy()

        btn = ttk.Button(font_win, text="OK", command=chooseFont)
        btn.pack(ipadx=80)

        def delete():
            global font_win_state
            font_win.destroy()
            font_win_state = "nothing"

        font_win.protocol("WM_DELETE_WINDOW", delete)
        font_win.mainloop()
    else:
        font_win.focus_force()
        print('already created')


def confirm_box():
    ans = mb.askyesnocancel("Save file", "Do you want to save this file ?")
    if ans == True:
        saved = save_file()
        if saved:
            win.destroy()
        else:
            return
    elif ans == False:
        win.destroy()
    else:
        return


def confirm_on_win_close(event=None):

    #  For child windows destroy
    global win2_state
    if win2_state == "active":
        win2.destroy()
        win2_state = "nothing"

    global win3_state
    if win3_state == "active":
        win3.destroy()
        win3_state = "nothing"

    global font_win_state
    if font_win_state == "active":
        font_win.destroy()
        font_win_state = "nothing"

    global go_to_window_state
    if go_to_window_state == "active":
        go_to_window.destroy()
        go_to_window_state = "nothing"

    # -----------------------------

    # global file
    if textArea.edit_modified() == 1:
        if file == None:
            text_length = len(textArea.get("1.0", "end-1c"))
            if text_length == 0:
                win.destroy()
            else:
                confirm_box()
        else:
            confirm_box()
    else:
        win.destroy()




