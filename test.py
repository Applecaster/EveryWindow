from tkinter import *
 
def cb_search(event):
     
    sstr=search_str.get()
    listbox.delete(0,END)
    #If filter removed show all data
    if sstr=="":
        fill_listbox(main_data) 
        return
 
    filtered_data=list()
    for item in main_data:
        if item.find(sstr)>=0:
            filtered_data.append(item)
  
    fill_listbox(filtered_data)   
 
def fill_listbox(ld):
    for item in ld:
        listbox.insert(END, item)
 
 
main_data= ["one","two", "three","twenty two"]
 
#GUI
master = Tk()


search_str = StringVar()
search = Entry(master, textvariable=search_str, width=10)
search.pack()
search.bind('<Return>', cb_search)


listbox = Listbox(master)
listbox.pack()
fill_listbox(main_data)

mainloop()