from menubar_methods import line_number
from variables import textArea
from variables import selected_chars
# from matching_keywords import keyword_matching
def select(event=None):
    line_number()
    # keyword_matching()
    try:
        chars = textArea.count("sel.first", "sel.last")
        line_breaks = textArea.count("sel.first", "sel.last", "lines")
        if line_breaks:
            if line_breaks[0] == 1:
                selected_chars.config(text=f"{chars[0]} chars, {line_breaks[0]} line break")
            elif line_breaks[0] > 1:
                selected_chars.config(text=f"{chars[0]} chars, {line_breaks[0]} line breaks")
        else:
            if chars[0] == 1:
                selected_chars.config(text=f"{chars[0]} char selected")
            else:
                selected_chars.config(text=f"{chars[0]} chars selected")
    except:
        selected_chars.config(text="--------------")
