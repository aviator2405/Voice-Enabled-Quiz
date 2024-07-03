import mysql.connector as mysql
import pandas as pd
from tkinter import messagebox
from tkinter import *

conn = mysql.connect(host='localhost', user='root', password='', database='quiz')
if conn.is_connected():
    messagebox.showinfo("INFORMATION", "DATABASE CONNECTED SUCCESSFULLY")
    print('Databases connected successfully')
    print()
    cursor = conn.cursor()

def retrive_question():
    cursor.execute("select * from question")
    data = pd.DataFrame(cursor.fetchall(),columns=['ques_id','question', 'A', 'B', 'C', 'D', 'correct'])
    # print(data)
    return data
    pass

def check_cred(username, password):
    cursor.execute("select *from credential")
    dataframe = pd.DataFrame(cursor.fetchall(), columns=['username', "password"])
    for i in range(0, len(dataframe)):
        row = dataframe.iloc[i]
        if username == row.username and password == row.password:
            return True

    else:
        return False


def new_login_cred(user, passw):
    cursor.execute("select *from credential")
    dataframe = pd.DataFrame(cursor.fetchall(), columns=['username', "password"])
    print ("new login cred")
    for i in range(0, len(dataframe)):
        row = dataframe.iloc[i]
        if user == row.username:
            return False
    cursor.execute(f"insert into credential values('{str(user)}','{str(passw)}')")
    conn.commit()
    return True


def new_login_per(user, name, add, phone):
    print(phone)
    cursor.execute(f"insert into per_info values('{str(user)}','{str(name)}','{str(add)}','{int(phone)}')")
    cursor.execute(f"insert into leadboard values('{str(user)}','{str(name)}',0);")
    conn.commit()
    return


def enter_score(user, score):
    print('start')
    cursor.execute(f"update leadboard set score={score} where username='{str(user)}'; ")
    conn.commit()
    print('commited')
    return


def rank_provider():
    cursor.execute('select * from leadboard order by score desc ;')
    rankdata = pd.DataFrame(cursor.fetchall(), columns=['username', 'pername', 'score'])
    print(rankdata)
    print(f'Number of user- {len(rankdata)}')
    top = [[]]
    toppointer = 0
    rank = 0
    same = rankdata.iloc[0].score
    # print(same)
    for i in range(len(rankdata)):
        r = rankdata.iloc[i]

        name = r.pername
        if same == r.score:
            top[len(top) - 1].append((r.username, r.pername, r.score))
            # print(top)
        else:
            same = r.score
            top.append([])
            top[len(top) - 1].append((r.username, r.pername, r.score))
    print(f'Rank of the users- {top}')
    return top


def leaderboardmaker(user=''):
    top = rank_provider()
    print(len(top))
    rank = 0
    first = ''
    second = ''
    third = ''
    if len(top) == 1:
        for i in range(len(top)):
            for j in range(len(top[i])):
                if len(first) == 0:
                    first = first + f'{str(top[i][j][1]).capitalize()}'

                else:
                    first = first + f', {str(top[i][j][1]).capitalize()}'
                print(first)
    elif len(top) == 2:
        for i in range(len(top)):
            for j in range(len(top[i])):
                if i == 0:
                    if len(first) == 0:
                        first = first + f'{str(top[i][j][1]).capitalize()}'

                    else:
                        first = first + f', {str(top[i][j][1]).capitalize()}'
                else:
                    if len(second) == 0:
                        second = second + f'{str(top[i][j][1]).capitalize()}'

                    else:
                        second = second + f', {str(top[i][j][1]).capitalize()}'

    elif len(top) == 3:
        for i in range(len(top)):
            for j in range(len(top[i])):
                if i == 0:
                    if len(first) == 0:
                        first = first + f'{str(top[i][j][1]).capitalize()}'

                    else:
                        first = first + f', {str(top[i][j][1]).capitalize()}'
                elif i == 1:
                    if len(second) == 0:
                        second = second + f'{str(top[i][j][1]).capitalize()}'

                    else:
                        second = second + f', {str(top[i][j][1]).capitalize()}'
                else:
                    if len(third) == 0:
                        third = third + f'{str(top[i][j][1]).capitalize()}'

                    else:
                        third = third + f', {str(top[i][j][1]).capitalize()}'
    else:
        for i in range(len(top)):
            for j in range(len(top[i])):
                if i == 0:
                    if len(first) == 0:
                        first = first + f'{str(top[i][j][1]).capitalize()}'

                    else:
                        first = first + f', {str(top[i][j][1]).capitalize()}'
                elif i == 1:
                    if len(second) == 0:
                        second = second + f'{str(top[i][j][1]).capitalize()}'

                    else:
                        second = second + f', {str(top[i][j][1]).capitalize()}'
                elif i == 2:
                    if len(third) == 0:
                        third = third + f'{str(top[i][j][1]).capitalize()}'

                    else:
                        third = third + f', {str(top[i][j][1]).capitalize()}'

    print(first, end='1\n')
    print(second, end='2\n')
    print(third, end='3\n')
    return first, second, third
    pass


user_rank = 0


def rank_finder(username):
    global user_rank

    top = rank_provider()
    for i in range(len(top)):
        for j in range(len(top[i])):
            if (username == top[i][j][0]):
                user_rank = i + 1
    return user_rank

# firstrank,secondrank,thirdrank = leaderboardmaker()
# rank_finder('aryan')
# leadboard = Tk()
# leadboard.title('JLUG QUIZ INTERFACE')
# leadboard.state('zoomed')
# leadboard.configure(background='#31304D')
#
# header = Frame(leadboard, background='navy')
# header.pack(fill="x")
# photo = PhotoImage(file="Picture1.png")
# logo = Label(header, image=photo)
# logo.pack(side=LEFT)
#
# poweredby = Label(header, text="Powered By-\nRK Patel and Company", background='navy',
#                       font='Constantia 13 bold italic',
#                       fg='#F0ECE5')
# poweredby.pack(side=RIGHT, padx=10)
#
# welcomelabel = Label(header, text="                        Welcome To JLUG Quiz Interface", background='navy',
#                          font='Constantia 20 bold italic',
#                          fg='#F0ECE5')
# welcomelabel.pack(pady=10, anchor=CENTER)
#
# # body
#
#
# winnerlabel = Label(leadboard,text='LEADER-BOARD', font='Constantia 20 bold italic underline', bg='#31304D',fg='#F0ECE5')
# winnerlabel.pack(pady=50)
#
# firstframe= Frame(leadboard,background="#31304D")
# firstframe.pack()
#
# first = Label(firstframe,text='1st- ', font='Constantia 40 bold italic', bg='#31304D',fg='#F0ECE5' )
# first.pack(pady=20,side=LEFT )
#
# firstname = Label(firstframe,text=f'{firstrank}', font='Constantia 20 bold italic', bg='#31304D',fg='#F0ECE5' )
# firstname.pack(pady=10,side=LEFT)
#
# secondframe= Frame(leadboard,background="#31304D")
# secondframe.pack()
#
# second = Label(secondframe,text='2nd- ', font='Constantia 40 bold italic', bg='#31304D',fg='#F0ECE5' )
# second.pack(pady=10,side=LEFT )
#
# secondname = Label(secondframe,text=f'{secondrank}', font='Constantia 20 bold italic', bg='#31304D',fg='#F0ECE5' )
# secondname.pack(pady=50,side=LEFT)
#
# thirdframe= Frame(leadboard,background="#31304D")
# thirdframe.pack()
#
# third = Label(thirdframe,text='3rd- ', font='Constantia 40 bold italic', bg='#31304D',fg='#F0ECE5' )
# third.pack(pady=10,side=LEFT )
#
# thirdname = Label(thirdframe,text=f'{thirdrank}', font='Constantia 20 bold italic', bg='#31304D',fg='#F0ECE5' )
# thirdname.pack(pady=50,side=LEFT)
#
# your_rank_frame= Frame(leadboard,background="#31304D")
# your_rank_frame.pack()
#
# your_rank=Label(your_rank_frame,text='YOUR RANK- ', font='Constantia 10 bold italic', bg='#31304D',fg='#F0ECE5' )
# your_rank.pack(pady=10,side=LEFT )
#
# your_rank_name = Label(your_rank_frame,text=f'{user_rank}', font='Constantia 40 bold italic', bg='#31304D',fg='#F0ECE5' )
# your_rank_name.pack(pady=50,side=LEFT)
#
# footer = Frame(leadboard, background='navy')
# footer.pack(fill="x", side=BOTTOM)
#
# timelabel = Label(footer, text=f'Welcome', font='Constantia 20 bold italic', fg='#F0ECE5',
#                      background='navy')
# timelabel.pack(pady=10, side=RIGHT, padx=10)
#
# leadboard.mainloop()
retrive_question()