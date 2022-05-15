import win32gui
import pyautogui
import tkinter


g_list = []
g_search_str = None
g_listbox = None


def winEnumHandler( hwnd, ctx ):
    global g_list
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        g_list.append(win32gui.GetWindowText(hwnd))
        # x = input()
        # win32gui.ShowWindow(hwnd, 5)
        # win32gui.SetForegroundWindow(hwnd)
        # pyautogui.press("alt")

def callback(event):
    print("You pressed Enter")
    print(event)

def cb_searchx(*args):
    global g_listbox
    global g_search_str
    
    sstr=g_search_str.get()
    g_listbox.delete(0,tkinter.END)
    #If filter removed show all data
    if sstr=="":
        fill_listbox(g_list) 
        if g_listbox.size():
            g_listbox.select_set(0)
        return
 
    filtered_data=list()
    print("hi")
    print(g_listbox)
    for item in g_list:
        print(f"hi search {item}")
        if item.lower().find(sstr.lower())>=0:
            filtered_data.append(item)
  
    fill_listbox(filtered_data)
    
    if g_listbox.size():
            g_listbox.select_set(0)


def fill_listbox(ld):
    global g_listbox
    for item in ld:
        g_listbox.insert(tkinter.END, item)


def on_entry_up_down(event):
    selection = g_listbox.curselection()[0]
    
    if event.keysym == 'Up':
        selection += -1

    if event.keysym == 'Down':
        selection += 1

    if 0 <= selection < g_listbox.size():
        g_listbox.selection_clear(0, tkinter.END)
        g_listbox.select_set(selection)


def main():
    global g_listbox, g_search_str
    
    app = tkinter.Tk()
    #app.bind('<Return>', callback)

    g_search_str = tkinter.StringVar()
    g_search_str.trace("w", cb_searchx)
    
    search_entry = tkinter.Entry(app, textvariable=g_search_str, width=10)
    search_entry.pack()
    search_entry.focus_set()

    g_listbox = tkinter.Listbox(app)
    win32gui.EnumWindows( winEnumHandler, g_list )
    fill_listbox(g_list)
    g_listbox.pack()
    if g_list:
        g_listbox.select_set(0)
    app.bind("<Down>", on_entry_up_down)
    app.bind("<Up>", on_entry_up_down)
    
    app.mainloop()


if __name__ == "__main__":
    main()