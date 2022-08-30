# This program is a GUI application that lets users test their typing speed

# import statements
import tkinter.messagebox
from tkinter import *
testing_value = "this is my test"
test_started = False
timer = None
correct_characters = 0
correct_words = 0
# create window
window = Tk()

# functions
def start_test():
    global test_started
    test_started = True
    count_down(10)

def count_down(count):
    global timer
    timer_label.config(text=f"{count} seconds remaining")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        calculate_score()
        tkinter.messagebox.showinfo(message=f"Test is complete. correct words = {correct_words}, correct characters = {correct_characters}")





# score calculation needs work
def calculate_score():
    global correct_words, correct_characters
    user_sentence = user_input.get()
    user_word_list = user_sentence.split()
    correct_word_list = testing_value.split()
    current_word = len(user_word_list)
    if current_word == 0:
        pass
    elif current_word <= len(correct_word_list):
        for i in range(current_word):
            for l in range(len(user_word_list[i])-1):
                    if user_word_list[i][l] == correct_word_list[i][l]:
                        correct_characters += 1
            if user_word_list[i] == correct_word_list[i]:
                correct_words += 1

    print(f"correct_words ={correct_words}")
    print(f"correct_characters = {correct_characters}")



def check_key(key):
    global test_started
    if not test_started:
        user_input.delete(0, END)
        start_test()
    else:
        pass




#create responsive grid
for i in range(4):
    window.grid_rowconfigure(i, weight=1)
window.grid_columnconfigure(0, weight=1)

# set min window size and other attributes
window.minsize(400, 300)
window.title("Typing Speed Test")


# # Build Canvas
#
# canvas = Canvas(width=700, height=400)
# program_text = canvas.create_text(350, 200, anchor="center", text="Welcome")
# # canvas.config(bg="black")
# canvas.grid(row=1, column=1, sticky=NSEW)

# Timer label for user
timer_label = Label(text="60"+" Seconds Remaining")
timer_label.grid(row=0, column=0, sticky=NSEW)

# Instructions and typing sentence label

instruction_text = Label(text="Welcome to the typing speed test, begin typing the sentence below in the text box to start")
instruction_text.grid(row=1, column=0, sticky=NSEW)
test_sentence = Label(text=testing_value)
test_sentence.grid(row=2, column=0, sticky=NSEW)


# User typing area
user_input = Entry()
user_input.insert(0, "Start typing here")

user_input.grid(row=3, column=0, sticky=NSEW)
user_input.bind("<Key>", check_key)












window.mainloop()