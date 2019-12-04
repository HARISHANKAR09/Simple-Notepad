from tkinter import *
from keyword import kwlist
from variables import win, textArea


def highlight_keyword(event):
    textArea.tag_delete('keyword', "1.0", END)
    keywords = kwlist
    count_var = IntVar()
    for k in keywords:
        start_index = '1.0'
        while True:  # search for occurence of k
            start_index = textArea.search(rf'\y{k}\y', start_index, END, count=count_var, regexp=True)
            if start_index:
                end_index = textArea.index('%s+%dc' % (start_index, count_var.get()))  # find end of k
                # print(end_index)
                textArea.tag_add('keyword', start_index, '%s+%dc' % (start_index, count_var.get()))
                # add tag to k
                textArea.tag_config('keyword', foreground='red')  # and color it with v
                textArea.tag_add("keyword", start_index, "%s+%dc" % (start_index, len(k)))
                start_index = end_index  # reset start_index to continue searching
            else:
                # textArea.tag_delete('coloring')
                break
