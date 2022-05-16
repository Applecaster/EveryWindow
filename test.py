# Import the required libraries
import tkinter
import pystray
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win=tkinter.Tk()
win.title("System Tray Application")

# Set the size of the window
win.geometry("700x350")

# Define a function for quit the window
def quit_window(icon, item):
   icon.stop()
   win.destroy()

# Define a function to show the window again
def show_window(icon, item):
   icon.stop()
   win.after(0,win.deiconify())

# Hide the window and show on the system taskbar
def hide_window():
   win.withdraw()
   print("hiii")
   image=Image.open("image.ico")
   menu=(pystray.MenuItem('Quit', quit_window), pystray.MenuItem('Show', show_window))
   icon=pystray.Icon("name", image, "title", menu)
   icon.run()

win.protocol('WM_DELETE_WINDOW', hide_window)

win.mainloop()