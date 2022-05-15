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
        print (hex(hwnd), win32gui.GetWindowText(hwnd))
        # x = input()
        # win32gui.ShowWindow(hwnd, 5)
        # win32gui.SetForegroundWindow(hwnd)
        # pyautogui.press("alt")

def callback(event):
    print("You pressed Enter")
    print(event)

def cb_search(event):
    global g_listbox
    global g_search_str
    
    sstr=g_search_str.get()
    g_listbox.delete(0,tkinter.END)
    #If filter removed show all data
    if sstr=="":
        fill_listbox(g_listbox) 
        return
 
    filtered_data=list()
    for item in g_listbox:
        if item.find(sstr)>=0:
            filtered_data.append(item)
  
    fill_listbox(filtered_data)   


def fill_listbox(ld):
    print("hi")
    print(ld)
    global g_listbox
    for item in ld:
        print(item)
        g_listbox.insert(tkinter.END, item)


def main():
    global g_listbox, g_search_str
    
    app = tkinter.Tk()
    app.bind('<Return>', callback)

    g_search_str = tkinter.StringVar()
    
    search = tkinter.Entry(app, textvariable=g_search_str, width=10)
    search.pack()
    search.bind('<Return>', cb_search)

    g_listbox = tkinter.Listbox(app)
    win32gui.EnumWindows( winEnumHandler, g_list )
    #print("hi")
    #print(g_list)
    fill_listbox(g_list)
    g_listbox.pack()
    
    app.mainloop()


if __name__ == "__main__":
    main()