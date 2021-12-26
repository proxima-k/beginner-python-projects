# https://github.com/jorgegonzalez/beginner-projects#pomodoro-timer
# Finished on 7 Apr 2020
from tkinter import *
from tkinter.font import Font

class App():

    def __init__(self):
        self.counter = 0
        self.mode = "Work"
        self.main()

    def countdown(self):
        if self.counter == 0:
            pass
        else:
            self.time = self.t.get()
            m, s = self.time.split(":")
            m = int(m)
            s = int(s)

            if s == 0:  # Timer
                if m > 0:
                    m -= 1
                    s = 59
                else:  # Switching modes
                    if self.mode == "Work":
                        self.mode = "Break"
                        m = 5
                        self.text.set("Take a break!")
                        pass
                    else:
                        self.mode = "Work"
                        m = 25
                        self.text.set("Time to focus!!")
                        pass
            else:
                s -= 1

            if (s < 10):
                s = f"0{s}"
            else:
                s = f"{s}"
            if (m < 10):
                m = f"0{m}"
            else:
                m = f"{m}"
            self.t.set(f"{m}:{s}")
            self.root.after(1000,self.countdown)

    def start(self):
        self.counter += 1
        if self.counter == 1:
            self.text.set("Time to focus!!")
            self.root.after(930, self.countdown)

    def reset(self):
        self.counter = 0
        self.t.set("25:00")
        self.text.set("Press Start to begin!")

    def main(self):
        self.root = Tk()
        self.width = 500
        self.height = 450
        self.root.geometry(f"{self.width}x{self.height}")
        self.root.title("Pomodoro Timer")
        self.timerFONT = Font(family="Ubuntu Mono", size=60, weight="bold")
        self.buttonFONT = Font(family="Ubuntu Mono", size=20, weight="bold")

        self.frame = Frame(self.root, bg="#ff9999")
        self.frame.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.9)

        # TIMER
        self.t = StringVar()
        self.t.set("25:00")
        self.label_time = Label(self.frame, bg="white", fg="#ff9999", textvariable=self.t, anchor="center")
        self.label_time.config(font=self.timerFONT)
        self.label_time.place(relx=0.05, rely=0.05, relwidth=0.9, relheight=0.3)

        # NOTIFICATION
        self.text = StringVar()
        self.text.set("Press start to begin!")
        self.label_notify = Label(self.frame, bg="#ff9999", fg="white", textvariable=self.text)
        self.label_notify.config(font=self.buttonFONT)
        self.label_notify.place(relx=0.05, rely=0.4, relwidth=0.9, relheight=0.1)

        # START BUTTON
        self.button_start = Button(self.frame, relief=FLAT, fg="#ff9999", text="START",command=self.start)
        self.button_start.config(font=self.buttonFONT)
        self.button_start.place(relx=0.3, rely=0.55, relwidth=0.4, relheight=0.1)

        # RESET BUTTON
        self.button_reset = Button(self.frame, relief=FLAT, fg="#ff9999", text="RESET",command=self.reset)
        self.button_reset.config(font=self.buttonFONT)
        self.button_reset.place(relx=0.3, rely=0.7, relwidth=0.4, relheight=0.1)


        self.root.mainloop()

app = App()