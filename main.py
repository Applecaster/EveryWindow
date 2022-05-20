import win32gui
import pyautogui
import tkinter
import pystray
import PIL


g_hwnd_title_list = []
g_filtered_data = []
g_search_str = None
g_listbox = None
g_app = None
g_icon = None
g_window_hidden = False

def winEnumHandler( hwnd, ctx ):
    global g_hwnd_title_list
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        g_hwnd_title_list.append((hwnd, win32gui.GetWindowText(hwnd)))
        g_filtered_data.append((hwnd, win32gui.GetWindowText(hwnd)))
        # x = input()

def enter_callback(event):
    global g_listbox, g_filtered_data, g_hwnd_title_list, g_app
    pyautogui.press("alt")
    win32gui.ShowWindow(g_filtered_data[g_listbox.curselection()[0]][0], 5)
    win32gui.SetForegroundWindow(g_filtered_data[g_listbox.curselection()[0]][0])
    g_app.destroy()

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
    
# Define a function for quit the window
def quit_window(icon, item):
   global g_app, g_icon
   g_icon.stop()
   g_app.destroy()

# Define a function to show the window again
def show_window(icon, item):
   global g_app, g_icon, g_window_hidden
   g_window_hidden = False
   g_icon.stop()
   g_app.after(0,g_app.deiconify())
      
# Hide the window and show on the system taskbar
def hide_window():
   global g_app, g_icon, g_window_hidden
   if not g_window_hidden:
      g_window_hidden = True
      g_app.withdraw()
      image=PIL.Image.open("image.ico")
      quit_window_item = pystray.MenuItem('Quit', quit_window)
      show_window_item = pystray.MenuItem('Show', show_window, default=True)
      menu=(show_window_item, quit_window_item)
      g_icon=pystray.Icon("name", image, "title", menu)
      g_icon.run()


def hide_window2(event):
   hide_window()


def main():
    global g_listbox, g_search_str, g_hwnd_title_list, g_filtered_data, g_app, g_icon, g_window_hidden
    
    while True:
        g_hwnd_title_list = []
        g_filtered_data = []
        g_search_str = None
        g_listbox = None
        g_app = None
        
        g_app = tkinter.Tk()
        g_app.bind('<Return>', enter_callback)

        g_search_str = tkinter.StringVar()
        g_search_str.trace("w", cb_searchx)
        
        search_entry = tkinter.Entry(g_app, textvariable=g_search_str, width=10)
        search_entry.pack()
        search_entry.bind('<Control-BackSpace>', entry_ctrl_bs)
        search_entry.focus_set()

        g_listbox = tkinter.Listbox(g_app)
        win32gui.EnumWindows( winEnumHandler, g_hwnd_title_list )
        fill_listbox(g_hwnd_title_list)
        g_listbox.pack()
        if g_hwnd_title_list:
            g_listbox.select_set(0)
        g_app.bind("<Down>", on_entry_up_down)
        g_app.bind("<Up>", on_entry_up_down)
        
        g_app.protocol('WM_DELETE_WINDOW', hide_window)
        g_app.bind('<Unmap>', hide_window2)
        
        g_app.mainloop()
        
        print("exited cleanly :)")
        input("Press enter to run again")


if __name__ == "__main__":
    main()