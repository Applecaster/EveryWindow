import win32gui
import pyautogui
import tkinter


g_hwnd_title_list = []
g_filtered_data = []
g_search_str = None
g_listbox = None


def winEnumHandler( hwnd, ctx ):
    global g_hwnd_title_list
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        g_hwnd_title_list.append((hwnd, win32gui.GetWindowText(hwnd)))
        g_filtered_data.append((hwnd, win32gui.GetWindowText(hwnd)))
        # x = input()

def enter_callback(event):
    global g_listbox, g_filtered_data, g_hwnd_title_list
    win32gui.ShowWindow(g_filtered_data[g_listbox.curselection()[0]][0], 5)
    pyautogui.press("alt")
    win32gui.SetForegroundWindow(g_filtered_data[g_listbox.curselection()[0]][0])
    exit()

def cb_searchx(*args):
    global g_listbox, g_search_str, g_filtered_data
    
    sstr=g_search_str.get()
    g_listbox.delete(0,tkinter.END)
    #If filter removed show all data
    if sstr=="":
        fill_listbox(g_hwnd_title_list) 
        if g_listbox.size():
            g_listbox.select_set(0)
        return
 
    g_filtered_data=list()
    for item in g_hwnd_title_list:
        print(f"hi search {item}")
        if item[1].lower().find(sstr.lower())>=0:
            g_filtered_data.append(item)
  
    fill_listbox(g_filtered_data)
    
    if g_listbox.size():
            g_listbox.select_set(0)


def fill_listbox(hwnd_title_list):
    global g_listbox
    for hwnd_title_tuple_item in hwnd_title_list:
        g_listbox.insert(tkinter.END, hwnd_title_tuple_item[1])


def on_entry_up_down(event):
    selection = g_listbox.curselection()[0]
    
    if event.keysym == 'Up':
        selection += -1

    if event.keysym == 'Down':
        selection += 1

    if 0 <= selection < g_listbox.size():
        g_listbox.selection_clear(0, tkinter.END)
        g_listbox.select_set(selection)


def entry_ctrl_bs(event):
    ent = event.widget
    end_idx = ent.index(tkinter.INSERT)
    start_idx = ent.get().rfind(" ", None, end_idx)
    ent.selection_range(start_idx, end_idx)
    

def main():
    global g_listbox, g_search_str, g_hwnd_title_list, g_filtered_data
    
    app = tkinter.Tk()
    app.bind('<Return>', enter_callback)

    g_search_str = tkinter.StringVar()
    g_search_str.trace("w", cb_searchx)
    
    search_entry = tkinter.Entry(app, textvariable=g_search_str, width=10)
    search_entry.pack()
    search_entry.bind('<Control-BackSpace>', entry_ctrl_bs)
    search_entry.focus_set()

    g_listbox = tkinter.Listbox(app)
    win32gui.EnumWindows( winEnumHandler, g_hwnd_title_list )
    fill_listbox(g_hwnd_title_list)
    g_listbox.pack()
    if g_hwnd_title_list:
        g_listbox.select_set(0)
    app.bind("<Down>", on_entry_up_down)
    app.bind("<Up>", on_entry_up_down)
    
    app.mainloop()


if __name__ == "__main__":
    main()