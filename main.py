import win32gui
import pyautogui

import tkinter

def winEnumHandler( hwnd, ctx ):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        print (hex(hwnd), win32gui.GetWindowText(hwnd))
        x = input()
        win32gui.ShowWindow(hwnd, 5)
        win32gui.SetForegroundWindow(hwnd)
        pyautogui.press("alt")

def callback(event):
    print("You pressed Enter")
    print(event)

def main():
    app = tkinter.Tk()
    app.bind('<Return>', callback)


    Lb1 = tkinter.Listbox(app)
    Lb1.insert(1, "Python")
    Lb1.insert(2, "Perl")
    Lb1.insert(3, "C")
    Lb1.insert(4, "PHP")
    Lb1.insert(5, "JSP")
    Lb1.insert(6, "Ruby")

    Lb1.pack()
    app.mainloop()
    
    #win32gui.EnumWindows( winEnumHandler, None )


if __name__ == "__main__":
    main()