from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class UI:
    def __init__(self,quiz_brain:QuizBrain):
        self.window = Tk()
        self.quiz = quiz_brain
        self.window.title("Quiz")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,width=280,text= "HELLO",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row = 1, column = 0, columnspan = 2,pady = 50)

        self.score_label = Label(text=f"Score: {0}",fg="white",bg=THEME_COLOR)
        self.score_label.grid(row=0,column=2)

        self.img = PhotoImage(file="images/true.png")
        self.button1 = Button(image=self.img,highlightthickness=0,command=self.true)
        self.button1.grid(row=2,column = 0)

        self.img2 = PhotoImage(file="images/false.png")
        self.button1 = Button(image=self.img2, highlightthickness=0,command=self.false)
        self.button1.grid(row=2, column=1)
        
        self.get_next_question()

        self.window.mainloop()
        
    def get_next_question(self):
        self.canvas.config(bg= "white")
        if self.quiz.still_has_questions():
            self.score_label.config(text = f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text,text = q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f"Your score {self.quiz.score}/{self.quiz.question_number}")

    def true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self,is_right):
        if is_right:
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.get_next_question)
