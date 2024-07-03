# OM GANESHAY NAMAH
# MAIN GUI INTERFACE
import time

import win32com
import winsound

from pandas import DataFrame
import csv
from tkinter import *
# import pyaudio
import speech_recognition as sr
from tkinter import messagebox
import win32com.client
import admin_window
from database_manager import *
speaker = win32com.client.Dispatch('SAPI.SpVoice')


def say(text):
    speaker.Speak(text)


i = 0
score = 0
recursion_permission = True
timer_id = None


def call_enter_score():
    print(userval.get())
    print(type(userval.get()))
    enter_score(userval.get(), score)
    # quit()
    firstrank, secondrank, thirdrank = leaderboardmaker()
    user_rank_window = rank_finder(str(userval.get()))
    leadboard = Tk()
    leadboard.title('JLUG QUIZ INTERFACE')
    leadboard.state('zoomed')
    leadboard.configure(background='#31304D')

    header = Frame(leadboard, background='navy')
    header.pack(fill="x")
    photo = PhotoImage(file="Picture1.png")
    logo = Label(header, image=photo)
    logo.pack(side=LEFT)

    poweredby = Label(header, text="Powered By-\nRK Patel and Company", background='navy',
                      font='Constantia 13 bold italic',
                      fg='#F0ECE5')
    poweredby.pack(side=RIGHT, padx=10)

    welcomelabel = Label(header, text="                        Welcome To JLUG Quiz Interface", background='navy',
                         font='Constantia 20 bold italic',
                         fg='#F0ECE5')
    welcomelabel.pack(pady=10, anchor=CENTER)

    # body

    winnerlabel = Label(leadboard, text='LEADER-BOARD', font='Constantia 20 bold italic underline', bg='#31304D',
                        fg='#F0ECE5')
    winnerlabel.pack(pady=50)

    firstframe = Frame(leadboard, background="#31304D")
    firstframe.pack()

    first = Label(firstframe, text='1st- ', font='Constantia 40 bold italic', bg='#31304D', fg='#F0ECE5')
    first.pack(pady=20, side=LEFT)

    firstname = Label(firstframe, text=f'{firstrank}', font='Constantia 20 bold italic', bg='#31304D', fg='#F0ECE5')
    firstname.pack(pady=10, side=LEFT)

    secondframe = Frame(leadboard, background="#31304D")
    secondframe.pack()

    second = Label(secondframe, text='2nd- ', font='Constantia 40 bold italic', bg='#31304D', fg='#F0ECE5')
    second.pack(pady=10, side=LEFT)

    secondname = Label(secondframe, text=f'{secondrank}', font='Constantia 20 bold italic', bg='#31304D', fg='#F0ECE5')
    secondname.pack(pady=50, side=LEFT)

    thirdframe = Frame(leadboard, background="#31304D")
    thirdframe.pack()

    third = Label(thirdframe, text='3rd- ', font='Constantia 40 bold italic', bg='#31304D', fg='#F0ECE5')
    third.pack(pady=10, side=LEFT)

    thirdname = Label(thirdframe, text=f'{thirdrank}', font='Constantia 20 bold italic', bg='#31304D', fg='#F0ECE5')
    thirdname.pack(pady=50, side=LEFT)

    your_rank_frame = Frame(leadboard, background="#31304D")
    your_rank_frame.pack()

    your_rank = Label(your_rank_frame, text='YOUR RANK- ', font='Constantia 10 bold italic', bg='#31304D', fg='#F0ECE5')
    your_rank.pack(pady=10, side=LEFT)

    your_rank_name = Label(your_rank_frame, text=f'{user_rank_window}', font='Constantia 40 bold italic', bg='#31304D',
                           fg='#F0ECE5')
    your_rank_name.pack(pady=50, side=LEFT)

    footer = Frame(leadboard, background='navy')
    footer.pack(fill="x", side=BOTTOM)

    timelabel = Label(footer, text=f'Welcome', font='Constantia 20 bold italic', fg='#F0ECE5',
                      background='navy')
    timelabel.pack(pady=10, side=RIGHT, padx=10)

    leadboard.mainloop()


def call_check_cred(useless=0):
    winsound.Beep(400, 200)
    r = username.get()
    if check_cred(username.get(), password.get()):
        login.destroy()

        if r == 'admin':
            adwin = Tk()
            quiz_admin_window = admin_window.QuizAdminWindow(adwin)
            adwin.mainloop()
            return
        # To store the ID of the timer

        with open('Book1.csv', 'r', newline='') as csvfile:
            csv_reader = csv.reader(csvfile)
            df = DataFrame(csv_reader, columns=['question', 'A', 'B', 'C', 'D', 'correct'])
            df=retrive_question()

        def say_question(i):
            say(str(df.iloc[i].question))
            say(f'Option A: {df.iloc[i].A}')
            say(f'Option B: {df.iloc[i].B}')
            say(f'Option C: {df.iloc[i].C}')
            say(f'Option D: {df.iloc[i].D}')

        def takecammand():
            r = sr.Recognizer()
            with sr.Microphone() as source:
                r.pause_threshold = 0.6
                audio = r.listen(source)
                print('Recognizing')
                try:
                    query = r.recognize_google(audio, language='en-in')
                    return query
                except Exception as e:
                    print(e)
                    return 'Something went wrong,Sorry for that '

        def mic_commanding():
            winsound.Beep(400, 200)
            infolabel.config(text='Listening')
            infolabel.update()

            query = takecammand()
            infolabel.config(text='')
            if query == 'Something went wrong,Sorry for that ':
                a = messagebox.showerror('ERROR', 'Speak loud and clear')
                print('Error- Could Not Recognised', end=a)
            else:
                # confirm_window = Tk()
                # confirm_window.mainloop()
                # say(query)
                # say(str('confirm?'))
                # ans = takecammand()
                # ans = str(ans)
                # if ans.lower() == "yes":
                #     confirm = True
                #     confirm_window.destroy()
                # else:
                #     confirm = False
                #     confirm_window.destroy()

                confirm = messagebox.askyesno('Confirm', f'{query} ?')
                if confirm:
                    if 'a' in query.lower():
                        query = '1'
                    elif 'b' in query.lower():
                        query = '2'
                    elif 'c' in query.lower():
                        query = '3'
                    elif 'd' in query.lower():
                        query = '4'
                    else:
                        a = messagebox.showerror('Error', 'Speak correct option')
                        query = str(a)
                    if query == 'ok':
                        return
                    else:
                        check(str(query), df)
                return

        def start_quiz():
            winsound.Beep(400, 200)
            quesscrolly.pack(side=RIGHT, fill=Y)
            ques.pack(anchor=W, pady=50, padx=50)
            optA.pack(pady=10, padx=100, anchor=W)
            optB.pack(pady=10, padx=100, anchor=W)
            optC.pack(pady=10, padx=100, anchor=W)
            optD.pack(pady=10, padx=100, anchor=W)
            # infolabel.pack(pady=5, anchor=CENTER)
            # ansfield.pack(anchor=CENTER)
            timelabel.config(text=f'Time Remaining- {20} sec')
            suboptframe.pack(pady=10)
            # submitbutton.pack(anchor=CENTER, pady=10)
            # submitbuttonmic.pack(anchor=CENTER, side=LEFT)
            startbutton.destroy()
            next_ques(0)

        def update_label(remaining_time):
            global i, recursion_permission, timer_id

            timelabel.config(text=f'Time Remaining- {remaining_time} sec')

            if remaining_time > 0 and recursion_permission:
                timer_id = root.after(1000, lambda: update_label(remaining_time - 1))
            else:
                timelabel.config(text=f'Time Remaining- {remaining_time} sec')
                i += 1
                next_ques(i)

        def last_timer(remaining_time):
            global username
            quittime.config(text=f"Window will be closed after {remaining_time} Sec.")

            if remaining_time > 0:
                root.after(1000, lambda: last_timer(remaining_time - 1))
            else:
                root.destroy()
                call_enter_score()

        def next_ques(i):
            winsound.Beep(400, 200)
            global recursion_permission, timer_id

            if i >= len(df):
                quesframe.destroy()
                submitbutton.destroy()
                infolabel.destroy()
                ansfield.destroy()
                startbutton.destroy()
                timelabel.destroy()
                submitbuttonmic.destroy()
                suboptframe.destroy()

                thankyou = Label(footer, text=f'Thankyou', font='Constantia 20 bold italic', fg='#F0ECE5',
                                 background='navy')
                thankyou.pack(pady=10, side=RIGHT, padx=10)

                thankyou_frame.pack(anchor=CENTER, pady=250)

                thanklabel = Label(thankyou_frame, text='Thank You', font='Constantia 40 bold italic', fg='#F0ECE5',
                                   background='#31304D')
                thanklabel.pack()

                scorelabel = Label(thankyou_frame, text=f"Score- {score}", font='Constantia 20 bold italic',
                                   fg='#F0ECE5',
                                   background='#31304D')
                scorelabel.pack(fill=X)
                # enter_score(str(username.get()),score)

                quittime.pack(fill=X, side=BOTTOM)
                root.after(1000, lambda: last_timer(20))

                return
            var.set(0)
            ques.update()
            optA.update()
            optB.update()
            optC.update()
            optD.update()

            # Cancel any existing scheduled updates
            if timer_id:
                root.after_cancel(timer_id)

            # Start the timer for each new question
            recursion_permission = True
            timer_id = root.after(1000, lambda: update_label(20))
            ques.config(state=NORMAL)
            ques.delete(1.0, END)
            ques.insert(END, f'Q{i + 1}. {str(df.iloc[i].question)}')
            ques.config(state=DISABLED)
            optA.config(text=f'Option A: {df.iloc[i].A}')
            optB.config(text=f'Option B: {df.iloc[i].B}')
            optC.config(text=f'Option C: {df.iloc[i].C}')
            optD.config(text=f'Option D: {df.iloc[i].D}')
            ques.update()
            optA.update()
            optB.update()
            optC.update()
            optD.update()
            # time.sleep(1)
            say_question(i)

        # def get_it_checked():
        #     check(ansfield.get(), df, i)

        def check(ans, data):
            global score, recursion_permission, timer_id, i
            ans = str(ans).upper()
            cans = data.iloc[i].correct

            if ans == '1':
                ans = 'A'
            elif ans == '2':
                ans = 'B'
            elif ans == '3':
                ans = 'C'
            elif ans == '4':
                ans = 'D'
            else:
                ans = ''

            if ans == cans:
                score += 10
            elif ans == '':
                score += 0
            else:
                score -= 5

            i += 1
            ansvar.set('')
            print(f"Question No. - {i}")
            print(f'Option Selected- {ans}')
            print(f"Current Score- {score}")
            if i >= len(df):
                # print('quit code')
                score = score
                next_ques(i)
                recursion_permission = False

                # timer_id=root.after(1000, lambda: update_label(0))
            else:
                # print('next code')
                recursion_permission = False
                next_ques(i)

        # GUI INTERFACE
        root = Tk()
        root.title('JLUG QUIZ INTERFACE')
        root.state('zoomed')
        root.configure(background='#31304D')

        header = Frame(root, background='navy')
        header.pack(fill="x")
        photo = PhotoImage(file="Picture1.png")
        logo = Label(header, image=photo)
        logo.pack(side=LEFT)

        poweredby = Label(header, text="Powered By-\nRK Patel and Company", background='navy',
                          font='Constantia 13 bold italic',
                          fg='#F0ECE5')
        poweredby.pack(side=RIGHT, padx=10)

        welcomelabel = Label(header, text="                        Welcome To JLUG Quiz Interface", background='navy',
                             font='Constantia 20 bold italic',
                             fg='#F0ECE5')
        welcomelabel.pack(pady=10, anchor=CENTER)

        quesframe = Frame(root, background='#31304D')
        quesframe.pack(fill=BOTH)

        quesscrolly = Scrollbar(quesframe)

        quesvar = StringVar()

        ques = Text(quesframe, background='#F0ECE5', font='arial 16 bold', fg='navy', height=5, highlightthickness=0,
                    width=150,
                    borderwidth=5, relief=RIDGE, pady=10, padx=10, cursor='pirate', state=DISABLED)

        var = IntVar()

        optA = Radiobutton(quesframe, text='hello', background='#31304D', font='arial 16 bold', fg='#F0ECE5',
                           variable=var,
                           value='1')

        optB = Radiobutton(quesframe, text='hello', background='#31304D', font='arial 16 bold', fg='#F0ECE5',
                           variable=var,
                           value='2')

        optC = Radiobutton(quesframe, text='hello', background='#31304D', font='arial 16 bold', fg='#F0ECE5',
                           variable=var,
                           value='3')

        optD = Radiobutton(quesframe, text='hello', background='#31304D', font='arial 16 bold', fg='#F0ECE5',
                           variable=var,
                           value='4')
        # print(var)

        Label(background='#31304D').pack()
        Label(background='#31304D').pack()

        ansvar = StringVar()
        ansfield = Entry(textvariable=ansvar, font='arial 16 bold', bg='#F0ECE5')

        footer = Frame(root, background='navy')
        footer.pack(fill="x", side=BOTTOM)

        suboptframe = Frame(root, background='#31304D')

        submitbutton = Button(suboptframe, text='Submit', command=lambda: check(str(var.get()), df),
                              font='arial 16 bold',
                              bg='#F0ECE5')
        submitbutton.pack(anchor=CENTER, side=LEFT, pady=10)

        micphoto = PhotoImage(file='mic(reduced).png')

        submitbuttonmic = Button(suboptframe, image=micphoto, command=mic_commanding)
        submitbuttonmic.pack(anchor=CENTER, side=LEFT, ipady=3, padx=5)

        infolabel = Label(suboptframe, text='', background='#31304D', font='arial 16 bold', fg='#F0ECE5')
        infolabel.pack(anchor=CENTER, side=LEFT, ipady=3, padx=5)

        timelabel = Label(footer, text=f'Welcome', font='Constantia 20 bold italic', fg='#F0ECE5',
                          background='navy')
        timelabel.pack(pady=10, side=RIGHT, padx=10)

        startbutton = Button(text='Start Button', command=lambda: start_quiz(), font='arial 16 bold', bg='#F0ECE5')
        startbutton.pack(anchor=CENTER, pady=300)

        thankyou_frame = Frame(root)

        quittime = Label(thankyou_frame, text=f"Window will be closed after {0} Sec.", background='#31304D',
                         fg='#F0ECE5')

        root.mainloop()

        pass

    else:
        messagebox.showerror('ERROR MESSAGE', 'INVALID,BAD CREDENTIALS')


def call_newlogin():
    winsound.Beep(400, 200)

    def call_func():
        if new_login_cred(usern.get(), passwor.get()):
            new_login_per(usern.get(), cname.get(), address.get(), pnum.get())
            print ("newloginper")
            a = messagebox.showinfo("INFORMATION MESSAGE", "YOU HAVE SUCCESSFULLY CREATED YOUR ACCOUNT !!")

            window.destroy()
        else:
            a = messagebox.showinfo("INFORMATION MESSAGE", "THIS USERNAME HAS ALREADY TAKEN")
        print(a)

    window = Tk()
    window.state("zoomed")
    window.title('NEW USER LOGIN PAGE')
    window.geometry("666x666")
    window.configure(background='#F5E8C7')

    user = StringVar()
    passw = StringVar()
    name = StringVar()
    add = StringVar()
    num = IntVar()

    label = Label(window, text="QUIZ SYSTEM", font='Centaur 20 bold', fg='#F5E8C7',
                  background='#363062')
    label.pack(fill=X)

    Label(window, font='arial 11', background='#F5E8C7').pack()

    Label(window, text='ENTER YOUR USER_ID OF YOUR CHOICE', font='arial 16', background='#F5E8C7').pack()

    Label(window, font='arial 11', background='#F5E8C7').pack()
    usern = Entry(window, textvariable=user, font='lucida 20 bold')
    usern.pack()

    Label(window, font='arial 11', background='#F5E8C7').pack()
    Label(window, text="ENTER YOUR PASSWORD", font='arial 16', background='#F5E8C7').pack()

    Label(window, font='arial 11', background='#F5E8C7').pack()
    passwor = Entry(window, textvariable=passw, show='$', font='lucida 20 bold')
    passwor.pack()

    Label(window, font='arial 11', background='#F5E8C7').pack()
    Label(window, text='ENTER YOUR NAME ', font='arial 16', background='#F5E8C7').pack()

    Label(window, font='arial 11', background='#F5E8C7').pack()
    cname = Entry(window, textvariable=name, font='lucida 20 bold')
    cname.pack()

    Label(window, font='arial 11', background='#F5E8C7').pack()
    Label(window, text='ENTER YOUR ADDRESS ', font='arial 16', background='#F5E8C7').pack()

    Label(window, font='arial 11', background='#F5E8C7').pack()
    address = Entry(window, textvariable=add, font='lucida 20 bold')
    address.pack()

    Label(window, font='arial 11', background='#F5E8C7').pack()
    Label(window, text='ENTER YOUR PHONE NUMBER ', font='arial 16', background='#F5E8C7').pack()

    Label(window, font='arial 11', background='#F5E8C7').pack()
    pnum = Entry(window, textvariable=num, font='lucida 20 bold')
    pnum.pack()

    Label(window, font='arial 11', background='#F5E8C7').pack()
    Button(window, text="Submit Details", command=call_func, cursor='hand2', font='lucida 20 bold',
           background='#363062', fg='#F5E8C7').pack()

    footer = Frame(window, background='#363062')
    footer.pack(side="bottom", fill=X)
    # LOGIN PAGE LABEL
    loginlabel = Label(footer, text="NEW USER LOGIN DETAILS PAGE", font="algerian 22 italic", fg='#F5E8C7',
                       background='#363062')
    loginlabel.pack(fill=X, pady=30, padx=50, side=RIGHT)

    window.mainloop()


login = Tk()
login.iconbitmap("rk-logo.ico")
login.state("zoomed")
login.title("RK PATEL AND COMAPANY STOCK MANAGEMENT SYSTEM")
login.geometry("666x666")
login.minsize(width=666, height=666)
login.configure(background='#31304D')

# HEADING LABEL
header = Frame(login, background='navy')
header.pack(fill="x")
photo = PhotoImage(file="Picture1.png")
logo = Label(header, image=photo)
logo.pack(side=LEFT)

poweredby = Label(header, text="Powered By-\nRK Patel and Company", background='navy',
                  font='Constantia 13 bold italic',
                  fg='#F0ECE5')
poweredby.pack(side=RIGHT, padx=10)

welcomelabel = Label(header, text="                        Welcome To JLUG Quiz Interface", background='navy',
                     font='Constantia 20 bold italic',
                     fg='#F0ECE5')
welcomelabel.pack(pady=10, anchor=CENTER)

footer = Frame(login, background='navy')
footer.pack(side="bottom", fill=X)
# LOGIN PAGE LABEL
loginlabel = Label(footer, text="LOGIN PAGE", font="algerian 22 italic", fg='#F5E8C7', background='navy')
loginlabel.pack(fill=X, pady=30, padx=50, side=RIGHT)

# STRING VARIABLES FOR USERNAME AND PASSWORD
userval = StringVar()
passval = StringVar()

buttonFrame = Frame(login, background='#31304D')
# CREDENTIAL FIELDS
user_label = Label(login, text="ENTER USERNAME", font='arial 16', background='#31304D', fg='#F5E8C7')
pass_label = Label(login, text="ENTER PASSWORD", font='arial 16', background='#31304D', fg='#F5E8C7')
username = Entry(textvariable=userval, font='lucida 20 bold')
password = Entry(textvariable=passval, show="*", font='lucida 20 bold')
subButton = Button(buttonFrame, text="SUBMIT", command=call_check_cred, cursor='hand2', font='lucida 20 bold')
password.bind("<Return>", call_check_cred)

Label(login, font='arial 20', background='#31304D').pack()
Label(login, font='arial 20', background='#31304D').pack()
Label(login, background='#31304D').pack()
Label(login, background='#31304D').pack()
Label(login, background='#31304D').pack()
# PACKING CREDENTIAL FIELDS
user_label.pack()
username.pack()
pass_label.pack()
password.pack()
Label(login, background='#31304D').pack()

buttonFrame.pack()
subButton.pack(side=LEFT, anchor=CENTER, padx=5)
Button(buttonFrame, text="NEW LOGIN ?", command=call_newlogin, font='lucida 20 bold').pack(side=LEFT, anchor=CENTER,
                                                                                           padx=5)

login.mainloop()
