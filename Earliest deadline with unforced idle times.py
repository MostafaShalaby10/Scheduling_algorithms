from operator import itemgetter
from tkinter import *

shape = Tk()
shape.title("Earliest deadline with unforced idle times")
shape.configure(bg="black")
shape.minsize(500, 250)
list = []


def execute():
    times = sorted(list, key=itemgetter(2))
    print(times)
    # # ----------------------ED-----------------------------------# #
    print("Task no : ", times[0][3], " isn't Missed")
    sum = times[0][0] + times[0][1]
    print("Started from ", times[0][0], " TO ", sum)
    for i in range(1, len(times)):
        if (sum > times[i][2]):
            print("Task no : ", times[i][3], " is Missed")
        elif (sum > times[i][0]):
            sum = sum + times[i][1]
            print("Task no : ", times[i][3], " isn't Missed")
            print("Started from ", (sum - int(times[i][1])), " TO ", sum)

        else:
            sum = sum + times[i][1] + (times[i][0] - sum)
            print("Task no : ", times[i][3], " isn't Missed")
            print("Started from ", (sum - int(times[i][1])), " TO ", sum)


def fun1():
    list.append([int(task_arrive_value.get()), int(task_execution_value.get()), int(task_deadline_value.get()),
                 task_name_value.get()])
    print(list)


task_arrive = Label(text="Arrive time", fg="white", font="Helvetica 10 bold italic", bg="black")
task_arrive.place(x=20, y=20)
task_arrive_value = Entry()
task_arrive_value.place(x=150, y=20)
task_execution = Label(text="Execution time", fg="white", font="Helvetica 10 bold italic", bg="black")
task_execution.place(y=50, x=20)
task_execution_value = Entry()
task_execution_value.place(y=50, x=150)
task_deadline = Label(text="deadline", fg="white", font="Helvetica 10 bold italic", bg="black")
task_deadline.place(y=80, x=20)
task_deadline_value = Entry()
task_deadline_value.place(y=80, x=150)
task_name = Label(text="Name", fg="white", font="Helvetica 10 bold italic", bg="black")
task_name.place(y=110, x=20)
task_name_value = Entry()
task_name_value.place(y=110, x=150)
submit1 = Button(text="enter", command=fun1, width=7, font=7, bg="white", fg="black")
submit1.place(y=150, x=120)

submit = Button(text="Done", command=execute, width=7, font=7, bg="white", fg="black")
submit.place(x=250, y=150)

shape.mainloop()
