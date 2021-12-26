# https://github.com/jorgegonzalez/beginner-projects#magic-8-ball
import random
import tkinter as tk

answer_list = ["As I see it, yes.",
               "Ask again later.",
               "It's not the right moment to tell you now.",
               "Can't predict now.",
               "Concentrate and ask again.",
               "Don't count on it.",
               "It is certain.",
               "It is decidedly so.",
               "Most likely.",
               "Probably.",
               "My reply is no.",
               "My sources say no.",
               "Well, the outlook isn't good.",
               "Outlook good.",
               "Reply hazy,try again.",
               "Signs point to yes.",
               "Very doubtful.",
               "Without a doubt. Definitely.",
               "Yes.",
               "You may rely on it."]


def main_event():
    # FUNCTIONS ------------------------------------------------------
    def ask():
        question_len = len(question.get())
        if question_len == 0:
            output.delete(0,tk.END)
            output.insert(tk.END,"You didn't type anything...")
        else:
            output.delete(0,tk.END)
            output.insert(tk.END,random.choice(answer_list))

    def clear():
        question.delete(0,tk.END)

    def playagain():
        output.delete(0,tk.END)
        output.insert(tk.END,"Type in a question and click Ask.")
        clear()

    # CREATING THE WINDOW ---------------------------------------------
    W_Width = 450
    W_Height = 150
    window = tk.Tk()
    window.geometry('{}x{}'.format(W_Width,W_Height))

    # OUTPUT BOX ----------------------------------------------------
    frame_upper = tk.Frame(window,bg="blue")
    frame_upper.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.2)

    output = tk.Entry(frame_upper,justify=tk.CENTER)
    output.insert(tk.END,"Type in a question and click Ask.")
    output.place(relx=0.05,rely=0.15,relwidth=0.9,relheight=0.7)

    # QUESTION BOX ---------------------------------------------------
    question = tk.Entry(window)
    question.place(relx=0.05,rely=0.3,relwidth=0.9,relheight=0.15)

    # BUTTONS --------------------------------------------------------
    buttonASK = tk.Button(window,text="Ask",command=ask)
    buttonASK.place(relx=0.04,rely=0.5,relwidth=0.2,relheight=0.2)

    buttonCLEAR = tk.Button(window,text="Clear",command=clear)
    buttonCLEAR.place(relx=0.28,rely=0.5,relwidth=0.2,relheight=0.2)

    buttonPLAYAGAIN = tk.Button(window,text="Play Again",command=playagain)
    buttonPLAYAGAIN.place(relx=0.52,rely=0.5,relwidth=0.2,relheight=0.2)

    buttonQUIT = tk.Button(window,text="Quit",command=window.destroy)
    buttonQUIT.place(relx=0.76,rely=0.5,relwidth=0.2,relheight=0.2)

    # LOOPING --------------------------------------------------------
    window.mainloop()

main_event()