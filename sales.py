from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import ttkbootstrap as tb
import sqlite3

class Windows(tb.Window):
    def __init__(self):
        super().__init__()
        self.Windows_login()
    
    def Windows_login(self):
        self.grid_columnconfigure(0, weight=1)

        self.frame_login = Frame(master=self)
        self.frame_login.grid(row=0, column=0, sticky=NSEW)

        Iblframe_login = tb.LabelFrame(master=self.frame_login, text="Log In")
        Iblframe_login.pack(padx=10, pady=35)

        Ibltitle = tb.Label(master=Iblframe_login, text="Log In")
        Ibltitle.pack(padx=10, pady=10)

        ent_user = tb.Entry(master=Iblframe_login, width=40, justify=CENTER)
        ent_user.pack(padx=10, pady=10)

        ent_password = tb.Entry(master=Iblframe_login, width=40, justify=CENTER)
        ent_password.pack(padx=10, pady=10)
        ent_password.config(show='*')

        btn_enter = tb.Button(master=Iblframe_login, width=38, text='Log in', bootstyle='success')
        btn_enter.pack(padx=10, pady=10)
        btn_enter.config(command=lambda: self.check_login(ent_user.get(), ent_password.get()))

    def check_login(self, username, password):
        conn = sqlite3.connect('user_login_liquor.db')
        cursor = conn.cursor()

        # Example query to check if username and password match
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        conn.close()

        if user:
            messagebox.showinfo("Liquor System", "Welcome back")
            self.startsession()
        else:
            #The login failed
            messagebox.showerror("Login Failed", "Invalid username or password")

    def window_menu(self):
        self.frame_left = Frame(self, width=200)
        self.frame_left.grid(row=0, column=0, sticky=NS)

        self.frame_center = Frame(self)
        self.frame_center.grid(row=0, column=1, sticky=NSEW)

        self.frame_right = Frame(self, width=400)
        self.frame_right.grid(row=0, column=2, sticky=NSEW)

        lbl1 = Label(self.frame_left, text="Button1")
        lbl1.grid(row=0, column=0, padx=10, pady=10)

        lbl2 = Label(self.frame_center, text="Button2")
        lbl2.grid(row=0, column=0, padx=10, pady=10)

        lbl3 = Label(self.frame_right, text="Button3")
        lbl3.grid(row=0, column=0, padx=10, pady=10)

    def startsession(self):
        self.frame_login.pack_forget()
        self.window_menu()


def main():
    app = Windows()
    app.title('Liquor system sales')
    app.state('zoomed')
    app.mainloop()


if __name__ == '__main__':
    main()

