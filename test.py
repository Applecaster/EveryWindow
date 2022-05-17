# Import the required libraries
import tkinter
import pystray
from PIL import Image, ImageTk
import threading

g_dostuff = True
g_icon = None
g_should_quit = False
g_window_hidden = False
#g_exit_event = threading.Event()

# Create an instance of tkinter frame or window
win=tkinter.Tk()
win.title("System Tray Application")

# Set the size of the window
win.geometry("700x350")

# Define a function for quit the window
def quit_window(icon, item):
   print("quit window")
   global g_dostuff, win, g_icon, g_should_quit
   g_dostuff = False
   g_icon.stop()
   #win.after(0,win.deiconify())
   win.destroy()

# Define a function to show the window again
def show_window(icon, item):
   print("show window")
   global win, g_icon, g_window_hidden
   g_window_hidden = False
   g_icon.stop()
   win.after(0,win.deiconify())
      
      
# Hide the window and show on the system taskbar
def hide_window():
   print("hide window")
   global win, g_icon
   win.withdraw()
   print("hiii")
   image=Image.open("image.ico")
   quit_window_item = pystray.MenuItem('Quit', quit_window)
   show_window_item = pystray.MenuItem('Show', show_window, default=True)
   menu=(show_window_item, quit_window_item)
   g_icon=pystray.Icon("name", image, "title", menu)
   g_icon.run()


def hide_window2(event):
   print("hide window 2")
   global g_window_hidden
   if not g_window_hidden:
      g_window_hidden = True
      hide_window()
   #threading.Thread(target=hide_window,args=()).start()

win.protocol('WM_DELETE_WINDOW', hide_window)
win.bind('<Unmap>', hide_window2)

#win.attributes('-toolwindow', 1)

win.mainloop()

print("waiting for input")
input("...")