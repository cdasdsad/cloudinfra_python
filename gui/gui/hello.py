# gui/hello.py

# tkinter 를 tk로 쓰겠다.
import tkinter as tk

if __name__ == "__main__" :
    root = tk.Tk() # Tk 객체 생성해서 참조값을 root에 담기

    root.geometry("300x100")

    label = tk.Label(root, text = "Hello, tkinter!", font = ("Arial", 14))
    label.pack(pady=30)

    root.mainloop()
