from customtkinter import *
from tkinter import *
import webbrowser
import imdb
from PIL import Image, ImageTk
import time

imdbq = imdb.IMDb()

def msearch(movie):
    searchq = imdbq.search_movie(movie)
    rendname = searchq[0]
    baseURL = 'https://vidsrc.xyz/embed/movie/tt' + searchq[0].getID()
    outline = imdbq.get_movie(searchq[0].getID()).data['plot outline']
    year = imdbq.get_movie(searchq[0].getID()).data['year']
    result = []
    result.append(f'{rendname}')
    result.append(baseURL)
    result.append(outline)
    result.append(year)
    return result

def tsearch(series):
    searchq = imdbq.search_movie(series)
    rendname = searchq[0]
    baseURL = 'https://vidsrc.xyz/embed/tv/tt' + searchq[0].getID()
    outline = imdbq.get_movie(searchq[0].getID()).data['plot outline']
    year = imdbq.get_movie(searchq[0].getID()).data['year']
    result = []
    result.append(f'{rendname}')
    result.append(baseURL)
    result.append(outline)
    result.append(year)
    return result

def loadingtxt():
    label.configure(text='Searching...')

def searchd():
    selected_content_type = content_type.get()
    if selected_content_type == "Movies":
        ret = msearch(entry.get())
    elif selected_content_type == "TV Series":
        ret = tsearch(entry.get())
    else:
        ret = ["", "", "", ""]

    label.configure(text=ret[0])
    outlinel.configure(text=ret[2])
    year.configure(text=ret[3])

    # Enable the button and bind the command to open the URL in a web browser
    if ret[0]:
        PlayURLButton.configure(state=NORMAL, command=lambda: webbrowser.open(ret[1]))
        PlayURL.configure(text=ret[1])
        PlayURLButton.place(relx=0.8, rely=0.4, anchor='center')  # Show the button
    else:
        PlayURLButton.pack_forget()

def searchbtn():
    loadingtxt()
    app.after(1000, searchd)  # Schedule searchd to be called after 1000 milliseconds (1 second)


app = CTk()
app.geometry('900x600')
app.title("Vidsrc")

button_image = CTkImage(Image.open("assets/banner.png"), size=(600, 120))
lblimg = CTkLabel(master=app, text="", image=button_image)
lblimg.pack(pady=10)

entry = CTkEntry(master=app, placeholder_text='Enter Name...', width=500, text_color='#FFCC70')
entry.place(relx=0.5, rely=0.3, anchor='center')

modex = ["Movies", "TV Series"]
content_type = StringVar(app)
content_type.set("Movies")  # default value

option_menu = CTkOptionMenu(master=app, values=modex, variable=content_type)
option_menu.place(relx=0.1, rely=0.3, anchor='center')

btn = CTkButton(master=app, text='Search', corner_radius=32, command=searchbtn)
btn.place(relx=0.9, rely=0.3, anchor='center')

label = CTkLabel(master=app, text=" ", font=('Times', 24))
label.place(relx=0.3, rely=0.4, anchor='center')

year = CTkLabel(master=app, text=" ", font=('Times', 14))
year.place(relx=0.3, rely=0.45, anchor='center')

outlinel = CTkLabel(master=app, text=" ", font=('Times', 14), wraplength=600)
outlinel.place(relx=0.5, rely=0.7, anchor='center')

PlayURL = CTkLabel(master=app, text=" ")
PlayURLButton = CTkButton(master=app, text="Play in Browser", state=DISABLED)  # Button is initially disabled

Cppry = CTkLabel(master=app, text="© Copyright 2024 Sapan Gajjar. All rights reserved.", font=('Times', 10))
Cppry.place(relx=0.5, rely=0.95, anchor='center')

app.mainloop()
