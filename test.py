# Import the required libraries
import tkinter
import pystray
from PIL import Image, ImageTk
import threading

g_icon = None
g_window_hidden = False

# Create an instance of tkinter frame or window
g_app=tkinter.Tk()
g_app.title("System Tray Application")

# Set the size of the window
g_app.geometry("700x350")

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
      image=Image.open("image.ico")
      quit_window_item = pystray.MenuItem('Quit', quit_window)
      show_window_item = pystray.MenuItem('Show', show_window, default=True)
      menu=(show_window_item, quit_window_item)
      g_icon=pystray.Icon("name", image, "title", menu)
      g_icon.run()


def hide_window2(event):
   hide_window()

g_app.protocol('WM_DELETE_WINDOW', hide_window)
g_app.bind('<Unmap>', hide_window2)

#win.attributes('-toolwindow', 1)

g_app.mainloop()

print("waiting for input")
input("...")