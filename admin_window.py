from tkinter import *
import mysql.connector
from tkinter import messagebox
import pandas as pd


class QuizAdminWindow:
    def __init__(self, root):
        self.root = root
        self.root.state("zoomed")
        self.root.title('ADMIN WINDOW')
        self.root.title("QUIZ SYSTEM ADMIN WINDOW")
        self.root.geometry("666x666")
        self.root.minsize(width=666, height=666)
        self.root.configure(background='#31304D')

        self.conn = mysql.connector.connect(host='localhost', user='root', password='', database='quiz')
        if self.conn.is_connected():
            print("DATABASE CONNECTED SUCCESSFULLY")
            messagebox.showinfo("SUCCESSFULL", "DATABASE CONNECTED SUCCESSFULLY...PRESS OK TO CONTINUE")
            self.cursor = self.conn.cursor()
        else:
            messagebox.showerror("ERROR", "DATABASE NOT CONNECTED...RESTART  THE APP")
            print("ERROR", "DATABASE NOT CONNECTED...RESTART  THE APP")
            quit()

        # Widgets for the main window
        # HEADER SECTION
        self.header = Frame(root, background='navy')
        self.header.pack(fill="x")
        self.photo = PhotoImage(file="Picture1.png")
        self.logo = Label(self.header, image=self.photo)
        self.logo.pack(side=LEFT)

        self.poweredby = Label(self.header, text="Powered By-\nRK Patel and Company", background='navy',
                               font='Constantia 13 bold italic', fg='#F0ECE5')
        self.poweredby.pack(side=RIGHT, padx=10)

        self.welcomelabel = Label(self.header, text="                        Welcome To JLUG Quiz Interface",
                                  background='navy', font='Constantia 20 bold italic', fg='#F0ECE5')
        self.welcomelabel.pack(pady=10, anchor=CENTER)

        # FOOTER SECTION
        self.footer = Frame(root, background='navy')
        self.footer.pack(side="bottom", fill=X)

        self.loginlabel = Label(self.footer, text="ADMIN WINDOW", font="algerian 22 italic", fg='#F5E8C7',
                                background='navy')
        self.loginlabel.pack(fill=X, pady=30, padx=50, side=RIGHT)

        # FEATURE PANEL
        self.left_frame = Frame(root, background="#435585", borderwidth=2, relief=GROOVE)
        self.left_frame.pack(fill="y", anchor="w", side="left")

        self.new_ques_button = Button(self.left_frame, text="Add New Question", font="latha 15 bold",
                                      command=self.add_button_active)
        self.new_ques_button.pack(anchor="center", padx=5, pady=100)

        self.del_ques_button = Button(self.left_frame, text="Delete Question", font="latha 15 bold", padx=13,
                                      command=self.del_button_active)
        self.del_ques_button.pack(anchor="center", padx=5)

        self.quit_button = Button(self.left_frame, text="Quit", font="latha 15 bold", padx=13, command=quit)
        self.quit_button.pack(anchor="center", padx=5, pady=50)

        # ADD NEW QUESTION WINDOW ELEMENTS STARTS
        self.head_label = Label(root, text="ADD NEW QUESTION", font="latha 20 bold italic underline",
                                background="#31304D", fg='#F0ECE5')

        # QUESTION SECTION
        self.ques_frame = Frame(root, background="#31304D")
        self.ques_label = Label(self.ques_frame, text="Enter Question", font="latha 15 bold ",
                                background="#31304D", fg='#F0ECE5', pady=5)
        self.ques_field = Text(self.ques_frame, height=2, font="Constantia 20 bold", state="normal")

        # OPTION A SECTION
        self.optA_frame = Frame(root, background="#31304D")
        self.optA_label = Label(self.optA_frame, text="OPTION A : ", font="latha 15 bold ",
                                background="#31304D", fg='#F0ECE5', pady=5)
        self.optA_field = Text(self.optA_frame, height=2, font="Constantia 20 bold", state="normal")

        # OPTION B SECTION
        self.optB_frame = Frame(root, background="#31304D")
        self.optB_label = Label(self.optB_frame, text="OPTION B : ", font="latha 15 bold ",
                                background="#31304D", fg='#F0ECE5', pady=5)
        self.optB_field = Text(self.optB_frame, height=2, font="Constantia 20 bold", state="normal")

        # OPTION C SECTION
        self.optC_frame = Frame(root, background="#31304D")
        self.optC_label = Label(self.optC_frame, text="OPTION C : ", font="latha 15 bold ",
                                background="#31304D", fg='#F0ECE5', pady=5)
        self.optC_field = Text(self.optC_frame, height=2, font="Constantia 20 bold", state="normal")

        # OPTION D SECTION
        self.optD_frame = Frame(root, background="#31304D")
        self.optD_label = Label(self.optD_frame, text="OPTION D : ", font="latha 15 bold ",
                                background="#31304D", fg='#F0ECE5', pady=5)
        self.optD_field = Text(self.optD_frame, height=2, font="Constantia 20 bold", state="normal")

        # SELECT CORRECT OPTION SECTION
        self.corr_int = IntVar()
        self.correct_frame = Frame(root, background="#31304D")
        self.corr_label = Label(self.correct_frame, text="CORRECT OPTION ?  : ", font="latha 15 bold ",
                                background="#31304D", fg='#F0ECE5', pady=5)
        self.radio1 = Radiobutton(self.correct_frame, variable=self.corr_int, value=1, text="A",
                                  font="latha 15 bold ", background="#31304D", fg='#F0ECE5')
        self.radio2 = Radiobutton(self.correct_frame, variable=self.corr_int, value=2, text="B",
                                  font="latha 15 bold ", background="#31304D", fg='#F0ECE5')
        self.radio3 = Radiobutton(self.correct_frame, variable=self.corr_int, value=3, text="C",
                                  font="latha 15 bold ", background="#31304D", fg='#F0ECE5')
        self.radio4 = Radiobutton(self.correct_frame, variable=self.corr_int, value=4, text="D",
                                  font="latha 15 bold ", background="#31304D", fg='#F0ECE5')

        # CONFIRMATION FOR ADDING BUTTON
        self.ch_but_frame = Frame(root, background="#31304D")
        self.ch_button = Button(self.ch_but_frame, text="ADD QUESTION TO DATABASE", font="Constantia 15 bold",
                                command=self.add_question)

        # WELCOME WINDOW ELEMENTS STARTS
        self.wel_label = Label(root, text="Welcome to\nQuizMate\nA Voice-Enabled Quiz/Exam System.",
                               background="#31304D", font="Constantia 30 bold", fg='#F0ECE5')
        self.wel_label.pack(pady=220)

        # DELETE QUESTION WINDOW ELEMENTS STARTS
        self.del_label = Label(root, text="DELETE QUESTION", font="latha 20 bold italic underline",
                               background="#31304D", fg='#F0ECE5')

        # QUESTION LIST SECTION
        self.list_frame = Frame(root, background="#31304D")
        self.ques_list = Listbox(self.list_frame, font="latha 14 bold ")

        # CONFIRMATION BUTTON FOR DELETING
        self.del_but_frame = Frame(root, background="#31304D")
        self.del_button = Button(self.del_but_frame, text="DELETE QUESTION FROM DATABASE", font="Constantia 15 bold",
                                 command=self.delete_ques_func)

        self.question_list_creator()

    # Function to create question list
    def question_list_creator(self):
        self.ques_list.delete(0, END)
        self.cursor.execute("select * from question")
        data = pd.DataFrame(self.cursor.fetchall(), columns=['ques_id', "ques", "A", "B", "C", "D", "correct"])
        for i in range(len(data)):
            entry = str(data.iloc[i].ques_id) + str(f":- {data.iloc[i].ques}")
            self.ques_list.insert(END, entry)

    # Function to delete question
    def delete_ques_func(self):
        confirm = messagebox.askyesno("Confirm?", f'Are you sure you want to delete the selected question?')
        if confirm:
            index = self.ques_list.curselection()
            copy = str(self.ques_list.get(index))
            self.cursor.execute(f'delete from question where ques_id={int(copy.split(":-")[0])}')
            self.conn.commit()
            messagebox.showinfo("Confirmation message",
                                f'Question with Question id:-{int(copy.split(":-")[0])} has been permanently deleted')
            self.question_list_creator()
        else:
            messagebox.showinfo("Information", "Action has been cancelled and database has been restored properly.")

    # Function to add question
    def add_question(self):
        a = messagebox.askyesno("Confirm", "Confirm the Changes?")
        if a:
            ques = self.ques_field.get("1.0", END)
            opta = self.optA_field.get("1.0", END)
            optb = self.optB_field.get("1.0", END)
            optc = self.optC_field.get("1.0", END)
            optd = self.optD_field.get("1.0", END)
            correct = int(self.corr_int.get())

            if correct == 1:
                correct_string = "A"
            elif correct == 2:
                correct_string = "B"
            elif correct == 3:
                correct_string = "C"
            else:
                correct_string = "D"

            self.cursor.execute(
                f"insert into question (ques,A,B,C,D,correct) values('{ques}','{opta}','{optb}','{optc}','{optd}','"
                f"{correct_string}')")
            self.conn.commit()
            messagebox.showinfo("Confirmation Message", "Question added to the database successfully")
            self.question_list_creator()

            # Clear all fields after adding question
            self.ques_field.delete('1.0', END)
            self.optA_field.delete('1.0', END)
            self.optB_field.delete('1.0', END)
            self.optC_field.delete('1.0', END)
            self.optD_field.delete('1.0', END)
            self.corr_int.set(0)

    # Function to switch to add question window
    def add_button_active(self):
        self.wel_label.pack_forget()
        self.del_label.pack_forget()
        self.list_frame.pack_forget()
        self.ques_list.pack_forget()
        self.del_but_frame.pack_forget()
        self.del_button.pack_forget()

        self.head_label.pack(anchor="center")
        self.ques_frame.pack()
        self.ques_label.pack(side=LEFT, anchor=NW)
        self.ques_field.config(state='normal')  # Enable editing
        self.ques_field.pack(side=LEFT, anchor=NW, pady=5)
        self.optA_frame.pack()
        self.optA_label.pack(side=LEFT, anchor=NW)
        self.optA_field.config(state='normal')  # Enable editing
        self.optA_field.pack(side=LEFT, anchor=NW, pady=5)
        self.optB_frame.pack()
        self.optB_label.pack(side=LEFT, anchor=NW)
        self.optB_field.config(state='normal')  # Enable editing
        self.optB_field.pack(side=LEFT, anchor=NW, pady=5)
        self.optC_frame.pack()
        self.optC_label.pack(side=LEFT, anchor=NW)
        self.optC_field.config(state='normal')  # Enable editing
        self.optC_field.pack(side=LEFT, anchor=NW, pady=5)
        self.optD_frame.pack()
        self.optD_label.pack(side=LEFT, anchor=NW)
        self.optD_field.config(state='normal')  # Enable editing
        self.optD_field.pack(side=LEFT, anchor=NW, pady=5)
        self.correct_frame.pack(fill=X)
        self.corr_label.pack(side=LEFT, anchor=NW)
        self.radio1.pack(side=LEFT, padx=10)
        self.radio2.pack(side=LEFT, padx=10)
        self.radio3.pack(side=LEFT, padx=10)
        self.radio4.pack(side=LEFT, padx=10)
        self.ch_but_frame.pack(fill=X)
        self.ch_button.pack(side=RIGHT, pady=50, padx=10)

    # Function to switch to delete question window
    def del_button_active(self):
        self.wel_label.pack_forget()
        self.head_label.pack_forget()
        self.ques_field.pack_forget()
        self.ques_label.pack_forget()
        self.ques_frame.pack_forget()
        self.optA_field.pack_forget()
        self.optA_label.pack_forget()
        self.optA_frame.pack_forget()
        self.optB_field.pack_forget()
        self.optB_label.pack_forget()
        self.optB_frame.pack_forget()
        self.optC_field.pack_forget()
        self.optC_label.pack_forget()
        self.optC_frame.pack_forget()
        self.optD_field.pack_forget()
        self.optD_label.pack_forget()
        self.optD_frame.pack_forget()
        self.radio4.pack_forget()
        self.radio3.pack_forget()
        self.radio2.pack_forget()
        self.radio1.pack_forget()
        self.corr_label.pack_forget()
        self.correct_frame.pack_forget()
        self.ch_button.pack_forget()
        self.ch_but_frame.pack_forget()

        self.del_label.pack(anchor="center")
        self.list_frame.pack(fill=X)
        self.ques_list.pack(fill=X, padx=80)
        self.del_but_frame.pack(fill=X)
        self.del_button.pack(side=RIGHT, pady=50, padx=10)
        self.question_list_creator()


if __name__ == "__main__":
    adwin = Tk()
    quiz_admin_window = QuizAdminWindow(adwin)
    adwin.mainloop()
