from tkinter import *
from handle_databases import *
import webbrowser
from main import *


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
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    index = int(w.curselection()[0])
    title = w.get(index)
    if not title == "":
        information_about_title = search_article(title)
        title_selected['text'] = title
        description_select['text'] = information_about_title[0][0]
        url_selected['text'] = information_about_title[0][1]
        write_article_textarea(information_about_title[0][2])


def write_article_textarea(article):
    text_area.config(state=NORMAL)
    text_area.delete(0.0, END)
    text_area.insert(END, article,'tag-right')
    text_area.config(state=DISABLED)


def refresh():
    update_articles()


subject_click=""


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


root = Tk()

window_width = 900
window_height = 500
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.title("crawler_sport")
#root.geometry("600x480+{}+{}".format(position_right, position_down))
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

listbox = Listbox(root, width=45, height=10)
listbox.bind('<<ListboxSelect>>', choose_title)
web1 = Button(root, text="Sport5", fg='black', command=lambda: search_titles_database('sport5', subject_click, subject_search.get()))
web2 = Button(root, text="Sport1", fg='black', command=lambda: search_titles_database('Sport1', "israeli_football"))
web3 = Button(root, text="ONE", fg='black')
refresh_button = Button(root, text="Refresh", fg='black', command=lambda: refresh())
title_selected = Label(root)
description_select = Label(root)
url_selected = Label(root, fg="blue", cursor="hand2")
url_selected.bind("<Button-1>", open_url)
text_area = Text(root)
text_area.tag_configure('tag-right', justify='right')


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
listbox.grid(row=4, column=3, columnspan=2, rowspan=4, sticky=E)
text_titles_select.grid(row=8, column=5)
text_description_select.grid(row=9, column=5)
title_selected.grid(row=8, column=3, columnspan=2, sticky=E)
description_select.grid(row=9, column=3, columnspan=2, sticky=E)
url_selected.grid(row=10, column=3, columnspan=2, sticky=E)
text_area.grid(row=11, columnspan=5)

#listbox.grid(row=4, column=2, columnspan=2)











root.mainloop()
