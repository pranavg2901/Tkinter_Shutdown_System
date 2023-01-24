from tkinter import *
import os


def Restart():
    os.system("shutdown /r /t 1")


def restart_time():
    os.system("shutdown /r /t 20")


def logout():
    os.system("shutdown -1")


def shutdown():
    os.system("shutdown /s /t 1")


st = Tk()
st.title("ShutDown")
st.geometry("500x500")
st.config(bg="Black")

restart = Button(st, text="Restart", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="plus",
                 command=Restart)
restart.place(x=160, y=60, height=70, width=160)

restart_time = Button(st, text="Restart Time", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="plus",
                      command=restart_time)
restart_time.place(x=160, y=150, height=70, width=160)

logout = Button(st, text="Log Out", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="plus", command=logout)
logout.place(x=160, y=240, height=70, width=160)

shutdown = Button(st, text="ShutDown", font=("Times New Roman", 20, "bold"), relief=RAISED, cursor="plus",
                  command=shutdown)
shutdown.place(x=160, y=330, height=70, width=160)

st.mainloop()
