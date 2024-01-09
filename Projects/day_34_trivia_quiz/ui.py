from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.label = Label(text='Score: 0', bg=THEME_COLOR, fg='white', highlightthickness=0)
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150,
                                                     125,
                                                     width=280,
                                                     text='',
                                                     font=('aerial', 20, 'italic'))




        true_image = PhotoImage(file='images/true.png')
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.check_if_correct_t)

        false_image = PhotoImage(file='images/false.png')
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.check_if_correct_f)
        self.true_button.grid(column=0, row=2)

        self.false_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg='white')
        if self.quiz.still_has_questions():
            self.label.configure(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")  

    def check_if_correct_t(self):
        is_correct = self.quiz.check_answer('True')
        self.give_feedback(is_correct)


    def check_if_correct_f(self):
        is_correct = self.quiz.check_answer('False')
        self.give_feedback(is_correct)
    def give_feedback(self, is_correct_p):
        if is_correct_p:
            self.canvas.configure(bg='green')
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)
        # self.canvas.configure(bg="white")



