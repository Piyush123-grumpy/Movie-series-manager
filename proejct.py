from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import sqlite3

conn = sqlite3.connect('dataa.db')

#create a server
# Cursor class is an instance which using which you can invoke methods that
#execute SQlite statements, fetch data from the result set of the queries
c = conn.cursor()
'''
#create a table
c.execute("""CREATE TABLE names(
          first_name text,
          last_name text,
          age integer,
          Username text,
          Password text 
)
""")
print("Table created suceessfully")

'''
#CODE FOR MOVIE MANAGER BELOW:

#creates registers the informations in the data base
def registerbutton():
    conn = sqlite3.connect('dataa.db')
    c = conn.cursor()

    # import into table
    c.execute("INSERT INTO names VALUES(:First_name,:Last_name, :age, :Username, :Password)", {
        'First_name':name_entry.get(),
        'Last_name':name_entry2.get(),
        'age':age_entry.get(),
        'Username':entry.get(),
        'Password':entry2.get()
    })
    print('Address inserted sucessfully')
    conn.commit()

    conn.close()

    #delete the boxxes
    name_entry.delete(0,END)
    name_entry2.delete(0,END)
    age_entry.delete(0,END)
    entry.delete(0,END)
    entry2.delete(0,END)
    messagebox.showinfo('Movie/series manager', 'Account has been registered')
    registerscren.destroy()
    select()
#To create a option screen to know whether the user wants to login or register
def select():
    global selectscreen
    selectscreen = Tk()
    selectscreen.title("Movie/Series Management system")
    selectscreen.geometry("500x350")
    selectscreen.iconbitmap("moveee.ico")
    selectscreen.resizable(0, 0)
    global bg
    global butn
    bg = ImageTk.PhotoImage(Image.open("space2.jpg"))
    butn = ImageTk.PhotoImage(Image.open("button_login.png"))
    butn2 = ImageTk.PhotoImage(Image.open("button_register (1).png"))
    my_canvas = Canvas(selectscreen, width=500, height=350)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0, 0, image=bg)
    my_canvas.create_text((250, 50), text="Welcome to Movies/Series", font=("vladimir script", 30), fill="misty rose")
    my_canvas.create_text((250, 100), text="Manager", font=("vladimir script", 30), fill="misty rose")
    my_canvas.create_text((250, 150), text="Would you like to", font=("Cambria", 16), fill="misty rose")
    my_canvas.create_text((250, 200), text="OR", font=("Helvetica", 10), fill="misty rose")
    buton1 = Button(selectscreen, image=butn, border=0,command=login)
    buton2 = Button(selectscreen, image=butn2, border=0,command=register)
    buton1_window = my_canvas.create_window(150, 205, window=buton1)
    buton2_window = my_canvas.create_window(350, 205, window=buton2)
    selectscreen.mainloop()
#shows the register window
def register():
    selectscreen.destroy()
    global registerscren
    registerscren=Tk()
    registerscren.title("Register")
    registerscren.geometry("300x300")
    registerscren.iconbitmap("moveee.ico")
    registerscren['bg']='lightsteelblue4'
    registerscren.resizable(0, 0)
    Firstname=StringVar()
    lastname=StringVar()
    agebeta=StringVar()
    Username=StringVar()
    Password=StringVar()
    global name_entry
    global name_entry2
    global age_entry
    global entry
    global entry2

    name=Label(registerscren,text="First Name:",font=('helvetica',8,'bold'),bg="lightsteelblue4",fg="white")
    name.place(x=30,y=55)
    name_entry=Entry(registerscren,text=Firstname)
    name_entry.place(x=100,y=55)
    lastname_label=Label(registerscren,text="Last name:",font=('helvetica',8,'bold'),bg="lightsteelblue4",fg="white")
    lastname_label.place(x=30,y=80)
    name_entry2 = Entry(registerscren,text=lastname)
    name_entry2.place(x=100, y=80)
    age=Label(registerscren,text="age:",font=('helvetica',8,'bold'),bg="lightsteelblue4",fg="white")
    age.place(x=30,y=105)
    age_entry = Entry(registerscren,text=agebeta)
    age_entry.place(x=100, y=105)
    label_1=Label(registerscren,text="User name:",font=('helvetica',8,'bold'),bg="lightsteelblue4",fg="white")
    label_1.place(x=30,y=130)
    entry=Entry(registerscren,text=Username)
    entry.place(x=100,y=130)
    label_2=Label(registerscren,text="Password:",font=('helvetica',8,'bold'),bg="lightsteelblue4",fg="white")
    label_2.place(x=30,y=155)
    entry2 = Entry(registerscren, text=Password)
    entry2.place(x=100, y=155)
    register_button=Button(registerscren,text="Register",font=('helvetica',8,'bold'),command=registerbutton,bg="grey4",fg="white",padx=15)
    register_button.place(x=105,y=190)
    registerscren.mainloop()
#pops up the log in window
def login():
    selectscreen.destroy()
    global entry1
    global entry2
    global log
    log=Tk()
    log.title("Log in")
    log.geometry("400x250")
    log.iconbitmap("moveee.ico")
    log.resizable(0, 0)
    global entry1
    global entry2
    img= ImageTk.PhotoImage(Image.open("space2.jpg"))
    buton2 = ImageTk.PhotoImage(Image.open("button_login.png"))
    goback =ImageTk.PhotoImage(Image.open("button_go-back (1).png"))
    my_canvas=Canvas(log,width=300,height=200)
    my_canvas.pack(fill="both",expand=True)
    my_canvas.create_image(0,0,image=img)
    my_canvas.create_text(100,70,text="Username:",font=("helvetica",15),fill="MistyRose")
    entry1 = Entry(log)
    my_canvas.create_window(230,70,window=entry1,width=150)
    my_canvas.create_text(100, 100, text="Password:", font=("helvetica", 15), fill="MistyRose")
    entry2 = Entry(log)
    my_canvas.create_window(230, 100, window=entry2,width=150)
    login_button = Button(log, image=buton2, border=0,command=loginbuttion)
    login_button_window = my_canvas.create_window(220, 150, window=login_button)
    goback_button = Button(log, image=goback, border=0, command=prevscreen)
    goback_button_window = my_canvas.create_window(220, 200, window=goback_button)
    log.mainloop()
def prevscreen():
    log.destroy()
    select()
#verifies the info in the login window
def loginbuttion():
    global a
    a=entry1.get()
    b=entry2.get()
    conn = sqlite3.connect('dataa.db')
    c.execute("SELECT *, oid FROM names")
    records = c.fetchall()
    for i in records:
        if a in i and a !="":
            if b in i and b !="":
                log.destroy()
                moviemanager()
                break
    else:
        messagebox.showerror('Movie/series manager', 'The username or password is invalid')
#movie manager user interface
def moviemanager():
    global add
    global my_canvas
    global add2
    global favbutn
    global movie
    global search
    movie=Tk()
    movie.title("Movie/Series manager")
    movie.geometry("400x500")
    movie.iconbitmap("moveee.ico")
    movie.resizable(0,0)
    background=ImageTk.PhotoImage(Image.open("nasa-rTZW4f02zY8-unsplash2.jpg"))
    add = ImageTk.PhotoImage(Image.open("button_add-a-movie (6).png"))
    removebtn= ImageTk.PhotoImage(Image.open("button_clear-the-list (2).png"))
    search=ImageTk.PhotoImage(Image.open("button_search (5).png"))
    favbutn=ImageTk.PhotoImage(Image.open("button_favourites (2).png"))
    add2=ImageTk.PhotoImage(Image.open("button_add-as-series (1).png"))
    showmoviebutn=ImageTk.PhotoImage(Image.open("button_show-movie-list (1).png"))
    showseriesebutn=ImageTk.PhotoImage(Image.open("button_show-series-list (1).png"))
    showfavutn=ImageTk.PhotoImage(Image.open("button_show-favourites.png"))
    quitbutn=ImageTk.PhotoImage(Image.open("button_quit.png"))
    my_canvas = Canvas(movie, width=500, height=350)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0, 0, image=background)
    addmovie = Button(movie, image=add, borderwidth=0,command=addmoviename)
    addmovie_window = my_canvas.create_window(70, 50, window=addmovie)
    removebutton = Button(movie, image=removebtn, borderwidth=0,command=delete)
    removebutton_window = my_canvas.create_window(70, 450, window=removebutton)
    searchbutton = Button(movie, image=search, borderwidth=0,command=searchbox)
    searchbutton_window = my_canvas.create_window(70, 150, window=searchbutton)
    favourite = Button(movie, image=favbutn, borderwidth=0,command=favourites)
    favourite_window = my_canvas.create_window(70, 200, window=favourite)
    showbutn=ImageTk.PhotoImage(Image.open("button_all-movie-series (2).png"))
    showbutton = Button(movie, image=showbutn, borderwidth=0,command=showquery)
    showbutton_window = my_canvas.create_window(70, 250, window=showbutton)
    addseries = Button(movie, image=add2, borderwidth=0,command=addseriesname)
    addmovie_series= my_canvas.create_window(70, 100, window=addseries)
    showmovie = Button(movie, image=showmoviebutn, borderwidth=0,command=querymovie)
    showmovie_window = my_canvas.create_window(70, 300, window=showmovie)
    showseries = Button(movie, image=showseriesebutn, borderwidth=0,command=queryseries )
    showseries_window = my_canvas.create_window(70, 350, window=showseries)
    showfav = Button(movie, image=showfavutn, borderwidth=0, command=queryfav)
    showfav_window = my_canvas.create_window(70, 400, window=showfav)
    quit = Button(movie, image=quitbutn, borderwidth=0,command=exit)
    quit_window = my_canvas.create_window(340, 460, window=quit)
    my_canvas.create_text((250, 150), text="Movies/Series", font=("vladimir script", 30),fill="misty rose")
    my_canvas.create_text((250, 200), text="Manager", font=("vladimir script", 30), fill="misty rose")
    my_canvas.create_text((250, 250), text="How much movie have ", font=("Helvetica", 12), fill="misty rose")
    my_canvas.create_text((250, 280), text="you seen?", font=("Helvetica", 12), fill="misty rose")
    movie.mainloop()
#Checks whether the name of the movie exists or not
def showquery():
    query = Toplevel()
    query.title("query")
    query.geometry("200x300")
    query.iconbitmap("moveee.ico")
    query.resizable(0,0)
    f = open(f'{a}.txt', 'r')
    list = f.readlines()
    scrollbar = Scrollbar(query)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(query, yscrollcommand=scrollbar.set,height=300,fg="black",bg="mistyrose")
    count=0
    for i in list:
        listbox.insert(END,f'{str(count)}. {str(i)}')
        count=count+1
    listbox.pack(side=TOP,fill=BOTH)
    scrollbar.config(command=listbox.yview)
    f.close()
#pops up the add name window
def addmoviename():
    movie.destroy()
    global blankspace_for_name
    global addmovie
    addmovie=Tk()
    addmovie.title("Add a movie to your list")
    addmovie.iconbitmap("moveee.ico")
    addmovie.geometry("300x200")
    addmovie.resizable(0,0)
    addmovimg= ImageTk.PhotoImage(Image.open("nasa-rTZW4f02zY8-unsplash2.jpg"))
    addmovbutn = ImageTk.PhotoImage(Image.open("button_add-a-movie (6).png"))
    my_canvas = Canvas(addmovie, width=300, height=200)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0, 0, image=addmovimg)
    blankspace= StringVar
    blankspace_for_name = Entry(addmovie)
    my_canvas.create_window(150, 70, window=blankspace_for_name, width=150)
    addbutn2 = Button(addmovie, image=addmovbutn, border=0,command=addmov)
    addbutn2_window = my_canvas.create_window(150, 110, window=addbutn2)
    addmovie.mainloop()
#adds the movie into the file
def addmov():

    blank=blankspace_for_name.get()
    f = open(f'{a}movies.txt','a')
    f.write(f'{blank}')
    f.write("\n")
    f.close()
    f = open(f'{a}.txt', 'a')
    f.write(f'{blank}')
    f.write("\n")
    f.close()
    blankspace_for_name.delete(0,END)
    messagebox.showinfo('Movies', 'Movie name has been added')
    addmovie.destroy()
    moviemanager()
#pops up the addseries name window
def addseriesname():
    movie.destroy()
    global blankspace_for_series
    global addseries
    addseries=Tk()
    addseries.title("Add a movie to your list")
    addseries.iconbitmap("moveee.ico")
    addseries.geometry("300x200")
    addseries.resizable(0,0)
    addseriesbg= ImageTk.PhotoImage(Image.open("nasa-rTZW4f02zY8-unsplash2.jpg"))
    addserbutn = ImageTk.PhotoImage(Image.open("button_add-as-series (1).png"))
    my_canvas = Canvas(addseries, width=300, height=200)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0, 0, image=addseriesbg)
    blankspace= StringVar
    blankspace_for_series = Entry(addseries)
    my_canvas.create_window(150, 70, window=blankspace_for_series, width=150)
    addbutn2 = Button(addseries, image=addserbutn, border=0,command=addser)
    addbutn2_window = my_canvas.create_window(150, 110, window=addbutn2)
    addseries.mainloop()
#adds the name of the series into the file
def addser():
    blank=blankspace_for_series.get()
    f = open(f'{a}series.txt','a')
    f.write(f'{blank}')
    f.write("\n")
    f.close()
    f = open(f'{a}.txt', 'a')
    f.write(f'{blank}')
    f.write("\n")
    f.close()
    blankspace_for_series.delete(0,END)
    messagebox.showinfo('Series', 'Seires name has been added')
    addseries.destroy()
    moviemanager()
#pops up the favourites window
def favourites():
    movie.destroy()
    global blankspace_for_fav
    global fav
    fav=Tk()
    fav.title("Add a movie to your list")
    fav.iconbitmap("moveee.ico")
    fav.geometry("300x200")
    fav.resizable(0,0)
    favbackg=ImageTk.PhotoImage(Image.open("nasa-rTZW4f02zY8-unsplash2.jpg"))
    favbuton=ImageTk.PhotoImage(Image.open("button_favourites (2).png"))
    my_canvas = Canvas(fav, width=300, height=200)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0, 0, image=favbackg)
    blankspace= StringVar
    blankspace_for_fav = Entry(fav)
    my_canvas.create_window(150, 70, window=blankspace_for_fav, width=150)
    favourite = Button(fav, image=favbuton, border=0,command=addfav)
    favourite_window = my_canvas.create_window(150, 110, window=favourite)
    fav.mainloop()
#adds the name of the favourite move in the list
def addfav():
    blank=blankspace_for_fav.get()
    f = open(f'{a}fav.txt','a')
    f.write(f'{blank}')
    f.write("\n")
    f.close()
    f = open(f'{a}.txt', 'a')
    f.write(f'{blank}')
    f.write("\n")
    f.close()
    blankspace_for_fav.delete(0,END)
    messagebox.showinfo('Favourites', 'Movie name has been added to favourite')
    fav.destroy()
    moviemanager()
#shows the list of all the movies
def querymovie():
    query = Toplevel()
    query.title("Movies")
    query.geometry("200x300")
    query.iconbitmap("moveee.ico")
    query.resizable(0,0)
    f = open(f'{a}movies.txt', 'r')
    list = f.readlines()
    scrollbar = Scrollbar(query)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(query, yscrollcommand=scrollbar.set,height=300,fg="black",bg="mistyrose")
    count = 0
    for i in list:
        listbox.insert(END,f'{str(count)}. {str(i)}')
        count=count+1
    listbox.pack(side=TOP,fill=BOTH)
    scrollbar.config(command=listbox.yview)
    f.close()
#shows the list of all the series you have entered
def queryseries():
    query = Toplevel()
    query.title("Series")
    query.geometry("200x300")
    query.iconbitmap("moveee.ico")
    query.resizable(0,0)
    f = open(f'{a}series.txt', 'r')
    list = f.readlines()
    scrollbar = Scrollbar(query)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(query, yscrollcommand=scrollbar.set,height=300,fg="black",bg="mistyrose")
    count=0
    for i in list:
        listbox.insert(END,f'{str(count)}. {str(i)}')
        count=count+1
    listbox.pack(side=TOP,fill=BOTH)
    scrollbar.config(command=listbox.yview)
    f.close()
#shows the list of all the favourite movies
def queryfav():
    query = Toplevel()
    query.title("Favourites")
    query.geometry("200x300")
    query.iconbitmap("moveee.ico")
    query.resizable(0,0)
    f = open(f'{a}fav.txt', 'r')
    list = f.readlines()
    scrollbar = Scrollbar(query)
    scrollbar.pack(side=RIGHT, fill=Y)
    listbox = Listbox(query, yscrollcommand=scrollbar.set,height=300,fg="black",bg="mistyrose")
    count=0
    for i in list:
        listbox.insert(END,f'{str(count)}. {str(i)}')
        count=count+1
    listbox.pack(side=TOP,fill=BOTH)
    scrollbar.config(command=listbox.yview)
    f.close()
#destroys/exits the UI
def exit():
    movie.destroy()
#clears all the name of the movies
def delete():
    global remove
    response = messagebox.askyesno('Deleted', 'Are you sure you want to clear the list?')
    if response == 1:
        f = open(f'{a}series.txt', 'w')
        f.write(f'')
        f.write("\n")
        f.close()
        f = open(f'{a}movies.txt', 'w')
        f.write(f'')
        f.write("\n")
        f.close()
        f = open(f'{a}fav.txt', 'w')
        f.write(f'')
        f.write("\n")
        f.close()
        f = open(f'{a}.txt', 'w')
        f.write(f'')
        f.write("\n")
        f.close()
        messagebox.showinfo('Deleted', 'The movie list has been cleared')
    else:
        pass
#destroys the remove window
def closewin():
    remove.destroy()
#pops up the search window
def searchbox():
    movie.destroy()
    global blankspace_for_finding
    global Find
    Find = Tk()
    Find.title("Add a movie to your list")
    Find.iconbitmap("moveee.ico")
    Find.geometry("300x200")
    Find.resizable(0,0)
    searchbg= ImageTk.PhotoImage(Image.open("nasa-rTZW4f02zY8-unsplash2.jpg"))
    searchbuton=ImageTk.PhotoImage(Image.open("button_search (5).png"))
    my_canvas = Canvas(Find, width=300, height=200)
    my_canvas.pack(fill="both", expand=True)
    my_canvas.create_image(0, 0, image=searchbg)
    blankspace = StringVar
    blankspace_for_finding = Entry(Find)
    my_canvas.create_window(150, 70, window=blankspace_for_finding, width=150)
    Findbutn2 = Button(Find, image=searchbuton, border=0, command=find)
    Findbutn2_window = my_canvas.create_window(150, 110, window=Findbutn2)
    Find.mainloop()
#finds the movie that you have searched
def find():
    f = open(f"{a}.txt", "r")
    b = f.readlines()
    word = blankspace_for_finding.get()
    for i in b:
        if word in i:
            messagebox.showinfo(f'Found', f'The movie {word} exists in the list')
            Find.destroy()
            moviemanager()
            break
    else:
        messagebox.showerror('Not Found', f'The movie {word} was not found. Please try again')
        Find.destroy()
        moviemanager()
select()
