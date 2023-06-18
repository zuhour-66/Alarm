from tkinter.ttk import *
from tkinter import *
import datetime
import threading
from playsound import playsound
from PIL import ImageTk, Image
import time
from tkinter import messagebox

def alarm():
    global is_alarm_active
    while is_alarm_active:
        control = activate_var.get()
        print(control)

        alarm_hour = hour1.get()
        alarm_minute = minutes1.get()
        alarm_sec = seconds1.get()

        now = datetime.datetime.now()

        hour = now.strftime("%I")
        minute = now.strftime("%M")
        second = now.strftime("%S")

        if control == 1:
            if alarm_hour == hour and alarm_minute == minute and alarm_sec == second:
                messagebox.showinfo("Alarm", "Time is now")
                playsound('C:\\Users\\alwas\\OneDrive\\المستندات\\a\\JAVA\\aa.mp3')
                print('playing sound using playsound')

        time.sleep(1)

def stop_alarm():
    global is_alarm_active
    is_alarm_active = False

def activate():
    global is_alarm_active
    set_alarm_timer = f"{hour1.get()}:{minutes1.get()}:{seconds1.get()}"
    if activate_var.get() == 1:
        is_alarm_active = True
        t = threading.Thread(target=alarm)
        t.start()
    else:
        is_alarm_active = False

bg_color = '#cbd2d4'
rr_color = '#d8eaf0'

window = Tk()
window.title("ALARM")
window.geometry('420x600')
icon = PhotoImage(file='ra.png')
window.iconphoto(True, icon)

frame_line = Frame(window, width=400, height=5, bg=rr_color)
frame_line.grid(row=0, column=0)

body1 = Frame(window, width=400, height=400, bg='#668894')
body1.grid(row=1, column=0)

img = Image.open(r'ra.png')
img = img.resize((100, 100))
img = ImageTk.PhotoImage(img)
label1 = Label(
    body1,
    text='MY Alarm',
    font=('Ivy 18 bold', 10, 'bold'),
    fg='#101517',
    bg='#4e7885',
    relief=GROOVE,
    bd=5,
    padx=2,
    pady=2,
    image=img,
    compound='right'
)
label1.place(x=10, y=15)

hour = Label(
    body1,
    text='HOUR',
    height=1,
    font=(('Arial', 10, 'bold')),
    bg='#668894',
    fg='#101517',
    relief=GROOVE,
    bd=5,
    padx=2,
    pady=2,
)
hour.place(x=130, y=120)

hour1 = Combobox(body1, width=2, font=('arial 17'))
hour1['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23')
hour1.current(0)
hour1.place(x=133, y=150)

minutes = Label(
    body1,
    text='MINUTE',
    height=1,
    font=(('Arial', 10, 'bold')),
    bg='#668894',
    fg='#101517',
    relief=GROOVE,
    bd=5,
    padx=2,
    pady=2,
)
minutes.place(x=177, y=120)

minutes1 = Combobox(body1, width=2, font=('arial 17'))
minutes1['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
minutes1.current(0)
minutes1.place(x=184, y=150)

seconds = Label(
    body1,
    text='SECOND',
    height=1,
    font=('Arial', 10, 'bold'),
    bg='#668894',
    fg='#101517',
    relief=GROOVE,
    bd=5,
    padx=2,
    pady=2,
)
seconds.place(x=227, y=120)

seconds1 = Combobox(body1, width=2, font=('arial 17'))
seconds1['values'] = ('00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60')
seconds1.current(0)
seconds1.place(x=235, y=150)

activate_var = IntVar()
activate_check = Checkbutton(
    body1,
    text="Activate",
    variable=activate_var,
    font=('arial 10 bold'),
    bg='#FFFFFF',
    relief=GROOVE,
    bd=5,
    padx=2,
    pady=2,
    command=activate
)
activate_check.place(x=125, y=222)

stop_button = Button(
    body1,
    text="Stop Alarm",
    font=('arial 10 bold'),
    bg='#FF0000',
    fg='#FFFFFF',
    relief=GROOVE,
    bd=5,
    padx=2,
    pady=2,
    command=stop_alarm
)
stop_button.place(x=210, y=222)

frame_line.configure(bg=rr_color)
window.mainloop()
