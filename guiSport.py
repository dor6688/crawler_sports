from tkinter import *

from PIL import ImageTk, Image

from handle_databases import *
import webbrowser
# from main import *


def search_titles_database(web, category, subject):
    if not category == "":
        titles = search_titles(web, category, subject)
        insert_titles(titles)
    else:
        print("need to choose category !")


def insert_titles(new_titles):
    listbox.delete(0, END)
    # need here to rank the titles
    for title in new_titles:
        str = ''.join(title)
        listbox.insert(END, str)
        listbox.insert(END, "")


def open_url(event):
    webbrowser.open_new(event.widget.cget("text"))


def choose_title(evt):
    global title_click
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    title_click = w.get(index)
    if not title_click == "":
        information_about_title = search_article(title_click)
        title_selected['text'] = title_click
        description_select['text'] = information_about_title[0][0]
        url_selected['text'] = information_about_title[0][1]
        # write_article_textarea(information_about_title[0][2])


def refresh():
    print(5)
    #update_articles()


subject_click = ""


def change_clicked(name):
    global subject_click
    if subject1['text'] == name:
        subject1.select()
        subject_click = 'israeli_football'
    else:
        subject1.deselect()

    if subject2['text'] == name:
        subject2.select()
        subject_click = 'world_football'
    else:
        subject2.deselect()

    if subject3['text'] == name:
        subject3.select()
        subject_click = 'israeli_basketball'
    else:
        subject3.deselect()

    if subject4['text'] == name:
        subject4.select()
        subject_click = 'nba'
    else:
        subject4.deselect()


# open the text in a new window
def window_article():
    text_window = Toplevel(root)
    window_width = 200
    window_height = 300
    position_right = int(text_window.winfo_screenwidth() / 2 - window_width / 2)
    position_down = int(text_window.winfo_screenheight() / 2 - window_height / 2)
    text_window.geometry("400x400+{}+{}".format(position_right, position_down))
    close_button = Button(text_window, text="Close", width="8", command=lambda: text_window.destroy())
    close_button.pack()
    scroll = Scrollbar(text_window, orient="vertical")
    scroll.pack(side=RIGHT, fill=Y)
    text_entry = Text(text_window, yscrollcommand=scroll.set)
    scroll.config(command=text_entry.yview)
    text_entry.tag_configure('tag-right', justify='right')
    text_entry.pack()
    if title_click is not None:
        information_about_title = search_article(title_click)
        article = information_about_title[0][2]
        text_entry.config(state=NORMAL)
        text_entry.delete(0.0, END)
        text_entry.insert(END, article, 'tag-right')
        text_entry.config(state=DISABLED)

root = Tk()
window_width = 900
window_height = 500
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.title("crawler_sport")
root.resizable(position_right, 0)
title_label = Label(root, text="חיפוש כתבות ספורט")
text_subject = Label(root, text=" :נושא ")
text_category = Label(root, text=" :תחום ")
text_web = Label(root, text=" :אתר ")
text_titles = Label(root, text=" :כותרות ")
text_titles_select = Label(root, text=" :נבחר ")
text_description_select = Label(root, text=" :תאור ")
text_url_select = Label(root, text=" :url ")

data_subject = StringVar()
subject_search = Entry(root, textvariable=data_subject)


subject1 = Checkbutton(root, text="כדורגל ישראלי", command=lambda: change_clicked("כדורגל ישראלי"))
subject2 = Checkbutton(root, text="כדורגל עולמי", command=lambda: change_clicked("כדורגל עולמי"))
subject3 = Checkbutton(root, text="כדורסל ישראלי", command=lambda: change_clicked("כדורסל ישראלי"))
subject4 = Checkbutton(root, text="NBA", command=lambda: change_clicked("NBA"))

listbox = Listbox(root, width=80, height=10)
width = 50
height = 50
img_sport1 = Image.open('sport1.jpeg')
img_sport5 = Image.open('sport5.jpeg')
img_one = Image.open('one.jpeg')
img_sport1 = img_sport1.resize((width, height), Image.ANTIALIAS)
img_sport5 = img_sport5.resize((width, height), Image.ANTIALIAS)
img_one = img_one.resize((width, height), Image.ANTIALIAS)
photo_sport1 = ImageTk.PhotoImage(img_sport1)
photo_sport5 = ImageTk.PhotoImage(img_sport5)
photo_one = ImageTk.PhotoImage(img_one)

listbox.bind('<<ListboxSelect>>', choose_title)
web1 = Button(root, text="Sport5", fg='black', command=lambda: search_titles_database('sport5', subject_click, subject_search.get()))
web2 = Button(root, text="Sport1", fg='black', command=lambda: search_titles_database('sport1', subject_click, subject_search.get()))
web3 = Button(root, text="ONE", fg='black', command=lambda: search_titles_database('one', subject_click, subject_search.get()))

web1.config(image=photo_sport5)
web2.config(image=photo_sport1)
web3.config(image=photo_one)


refresh_button = Button(root, text="Refresh", fg='black', command=lambda: refresh())
title_selected = Label(root)
description_select = Label(root, wraplength=400)
url_selected = Label(root, fg="blue", cursor="hand2")
url_selected.bind("<Button-1>", open_url)
text_area = Text()
text_button = Button(root, text="article", fg='black', command=lambda: window_article())


# grid
title_label.grid(columnspan=5)
text_subject.grid(row=1, column=5)
refresh_button.grid(row=1, column=0)
text_category.grid(row=2, column=5)
text_web.grid(row=3, column=5)
text_titles.grid(row=4, column=5)
text_url_select.grid(row=10, column=5)
subject_search.grid(row=1, column=4)
subject1.grid(row=2, column=4)
subject2.grid(row=2, column=3)
subject3.grid(row=2, column=2)
subject4.grid(row=2, column=1)
web1.grid(row=3, column=4)
web2.grid(row=3, column=3)
web3.grid(row=3, column=2)
listbox.grid(row=4, column=2, columnspan=3, rowspan=4, sticky=E)
text_titles_select.grid(row=8, column=5)
text_description_select.grid(row=9, column=5)
title_selected.grid(row=8, column=3, columnspan=2, sticky=E)
description_select.grid(row=9, column=3, columnspan=2, sticky=E)
url_selected.grid(row=10, column=3, columnspan=2, sticky=E)
text_button.grid(row=15, column=2, columnspan=2)


root.mainloop()
