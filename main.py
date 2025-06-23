from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
  w.after_cancel(timer)
  timer_text.config(text="Timer",fg=GREEN)
  canvas.itemconfig(time,text=f"00:00")
  check.config(text="")
  global reps
  reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_time():
  global reps

  reps +=1

  work_sec = WORK_MIN * 60
  short_break_sec = SHORT_BREAK_MIN * 60
  long_break_sec = LONG_BREAK_MIN * 60

  if reps in (1,3,5,7):
    countdown(work_sec)
    timer_text.config(text="WORK",fg=GREEN)
  elif reps == 8:
    countdown(long_break_sec)
    timer_text.config(text="BREAK",fg=RED)
  elif reps in (2,4,6):
    countdown(short_break_sec)
    timer_text.config(text="BREAK",fg=PINK)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def countdown(count):
  global reps
  
  count_min = math.floor(count / 60)
  count_sec = count%60
  
  if count_min < 10:
    count_min = f"0{count_min}"

  if count_sec < 10:
    count_sec = f"0{count_sec}"

  canvas.itemconfig(time,text=f"{count_min}:{count_sec}")
  if count > 0:
    global timer
    timer = w.after(1000,countdown,count-1)
  else:
    start_time()
    mark = ""
    for _ in range(math.floor(reps/2)):
      mark += "✔"
    check.config(text=mark, fg=GREEN,bg=YELLOW)


# ---------------------------- UI SETUP ------------------------------- #
w = Tk()
w.title("Pomodoro")
w.config(padx=100,pady=50,bg=YELLOW)


canvas = Canvas(width=200,height=224,bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="pomodoro/tomato.png")
canvas.create_image(100,112,image=img)
time = canvas.create_text(100,130,text="00:00", fill="white",font=(FONT_NAME,34,"bold"))
canvas.grid(column=1,row=1)

timer_text = Label(text="Timer", fg=GREEN, bg=YELLOW,font=(FONT_NAME,40))
timer_text.grid(column=1,row=0)

check = Label(fg=GREEN,bg=YELLOW, font=(FONT_NAME,15))
check.grid(column=1,row=3)

start = Button(text="Start",highlightthickness=0,command=start_time)
start.grid(column=0,row=2)

reset = Button(text="Reset",highlightthickness=0, command=reset_timer)
reset.grid(column=2,row=2)


w.mainloop()