import threading
from tkinter import *
from tkinter import messagebox

from PIL import ImageTk, Image

from handle_databases import *
import webbrowser
from main_sport import update_all

global all_new_article
all_new_article = 0


def search_titles_database(web, category, subject):
    """
    This method search titles from the database
    :param web: The selected web site
    :param category: The selected category
    :param subject: The selected subject
    """
    if not category == "":
        titles = search_titles(web, category, subject)
        insert_titles(titles)
    else:
        print("need to choose category !")


def insert_titles(new_titles):
    """
    This method insert titles to the list box
    :param new_titles: The titles that adding
    """
    listbox.delete(0, END)
    # need here to rank the titles
    for title in new_titles:
        str = ''.join(title)
        listbox.insert(END, str)
        listbox.insert(END, "")


def open_url(event):
    """
    This method open the url web site
    :param event: Click on the selected url
    """
    webbrowser.open_new(event.widget.cget("text"))


def choose_title(evt):
    """
    This method control of showing the data of a selected title
    :param evt: Click on the selected title
    """
    global title_click
    # Note here that Tkinter passes an event object to onselect()
    w = evt.widget
    try:
        index = int(w.curselection()[0])
        title_click = w.get(index)
        if not title_click == "":
            information_about_title = search_article(title_click)
            title_selected['text'] = title_click
            description_select['text'] = information_about_title[0][0]
            url_selected['text'] = information_about_title[0][1]
    except:
        pass


def refresh():
    """
    This method control of updating titles
    """
    global all_new_article
    if all_new_article > 0:
        messagebox.showinfo("New Article", "Found " + str(all_new_article) + " new articles :\nSport5 : " +
                            str(notification_sport5) + "\n" + "Sport1 : " + str(notification_sport1) + "\n" +
                            "ONE : " + str(notification_one))
    all_new_article = 0
    update_btn_text()


subject_click = ""


def change_clicked(name):
    """
    This method control of chosen category
    :param name:The chosen category
    """
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
def window_article(event):
    """
    This method control of the text window
    :param event: Click twice on the selected title
    """
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
    try:
        if title_click is not None:
            information_about_title = search_article(title_click)
            article = information_about_title[0][2]
            text_entry.config(state=NORMAL)
            text_entry.delete(0.0, END)
            text_entry.insert(END, article, 'tag-right')
            text_entry.config(state=DISABLED)
    except:
        pass


root = Tk()


window_width = 900
window_height = 700
position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
root.geometry("450x580+{}+{}".format(position_right, position_down))
root.title("crawler_sport")

top_frame = Frame(root)
top_frame.pack(side=TOP, pady=20)

title_label = Label(top_frame, text="חיפוש כתבות ספורט", font=("Helvetica", 18))
title_label.pack(side=TOP)

second_top_frame = Frame(root)
second_top_frame.pack(side=TOP)

text_category = Label(second_top_frame, text=" :תחום ", font=("Ariel", 14))
text_category.grid(row=0, column=4, pady=10)

subject1 = Checkbutton(second_top_frame, text="כדורגל ישראלי", command=lambda: change_clicked("כדורגל ישראלי"))
subject2 = Checkbutton(second_top_frame, text="כדורגל עולמי", command=lambda: change_clicked("כדורגל עולמי"))
subject3 = Checkbutton(second_top_frame, text="כדורסל ישראלי", command=lambda: change_clicked("כדורסל ישראלי"))
subject4 = Checkbutton(second_top_frame, text="NBA", command=lambda: change_clicked("NBA"))

subject1.grid(row=0, column=3)
subject2.grid(row=0, column=2)
subject3.grid(row=0, column=1)
subject4.grid(row=0, column=0)


# image on the button
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

text_web = Label(second_top_frame, text=" :אתר ", font=("Ariel", 14))

web1 = Button(second_top_frame, text="Sport5", fg='black', command=lambda: search_titles_database('sport5', subject_click, subject_search.get()))
web2 = Button(second_top_frame, text="Sport1", fg='black', command=lambda: search_titles_database('sport1', subject_click, subject_search.get()))
web3 = Button(second_top_frame, text="ONE", fg='black', command=lambda: search_titles_database('one', subject_click, subject_search.get()))

web1.config(image=photo_sport5)
web2.config(image=photo_sport1)
web3.config(image=photo_one)

text_web.grid(row=1, column=4)
web1.grid(row=1, column=3)
web2.grid(row=1, column=2)
web3.grid(row=1, column=1)

third_top_frame = Frame(root)
third_top_frame.pack(side=TOP)

text_subject = Label(second_top_frame, text=" :נושא ", font=("Ariel", 14))
text_subject.grid(row=2, column=4, pady=10)
data_subject = StringVar()
subject_search = Entry(second_top_frame, textvariable=data_subject, width=50)
subject_search.grid(row=2, column=0, columnspan=5)

center_frame = Frame(root)
center_frame.pack(side=TOP)

listbox = Listbox(center_frame, width=60, height=10)
listbox.bind('<<ListboxSelect>>', choose_title)
listbox.bind('<Double-1>', window_article)
listbox.pack()

bottom_frame = Frame(root)
bottom_frame.pack(side=TOP)


text_titles_select = Label(bottom_frame, text=" :נבחר ")
text_titles_select.pack()

title_selected = Label(bottom_frame, font='Helvetica 12 bold')
title_selected.pack()

bottom_second_frame = Frame(root)
bottom_second_frame.pack(side=TOP)

text_description_select = Label(bottom_second_frame, text=" :תאור ")
text_description_select.pack()

description_select = Label(bottom_second_frame, wraplength=420)
description_select.pack()

bottom_third_frame = Frame(root)
bottom_third_frame.pack(side=TOP)

text_url_select = Label(bottom_third_frame, text=" :url ")
text_url_select.pack()

url_selected = Label(bottom_third_frame, fg="blue", cursor="hand2")
url_selected.bind("<Button-1>", open_url)
url_selected.pack()


def update_btn_text(num=0):
    """
    This method write on the update button the number of the new articles that added
    :param num: Number of added articles
    """
    btn_text.set("New article : " + str(num))


btn_text = StringVar()
refresh_button = Button(root, text="Refresh", textvariable=btn_text, fg='black', command=lambda: refresh())
refresh_button.pack(side=BOTTOM)


def notification_article():
    """
    This method control the crawler timer
    """
    global all_new_article
    global notification_sport5
    global notification_sport1
    global notification_one
    threading.Timer(120.0, notification_article).start()
    count = update_all()
    notification_sport5 = count[0]
    notification_sport1 = count[1]
    notification_one = count[2]
    all_new_article += notification_sport5 + notification_sport1 + notification_one
    update_btn_text(all_new_article)
    print(count[0])
    print(count[1])
    print(count[2])


notification_article()
root.resizable(0, 0)
root.mainloop()
