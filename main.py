# This program is a basic GUI application that lets users test their typing speed

# import statements
import tkinter.messagebox
from tkinter import *

# constants
TEST_TIME = 30
MINUTE = 60
TEST_FONT = ("Times", "24", "bold")
BASE_FONT = ("Times", "16")
# testing sentence taken from 10fastfingers.com
TESTING_VALUE = "He found himself sitting at his computer, typing whatever came to mind. He was on a website " \
                "entitled\n " \
                "10 fast fingers. This site tested how fast you were at typing. So he typed. He was currently typing\n " \
                "about himself typing, which is odd in a way. He was now describing about how he was typing about\n " \
                "himself typing. "
# variable to allow for retesting
test_started = False
timer = None
# base values of variables modified by functions
correct_characters = 0
correct_words = 0
char_per_minute = 0
words_per_minute = 0

# create window
window = Tk()


# functions
def start_test():
    global test_started
    test_started = True
    count_down(TEST_TIME)


def end_message():
    # allows user to retry the typing test
    retry = tkinter.messagebox.askretrycancel(title="results",
                                              message=f"Test is complete.\ncorrect words = {correct_words}, correct "
                                                      f"characters = {correct_characters}\n resulting in {char_per_minute} cpm and {words_per_minute} wpm ")
    if retry:
        restart()


def count_down(count):
    global timer
    timer_label.config(text=f"{count} seconds remaining")
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
        get_correct(count)
    elif count == 0:
        get_correct(count)
        end_message()


def get_correct(count):
    global correct_words, correct_characters
    # function resets correct values to 0 so that it can recalculate the score, useful if user deletes and retypes words
    correct_characters = 0
    correct_words = 0
    user_sentence = user_input.get()
    # break sentences into words
    user_word_list = user_sentence.split()
    correct_word_list = TESTING_VALUE.split()
    # checks which list is longer to prevent index errors
    if len(user_word_list) <= len(correct_word_list):
        shorter_list = user_word_list
    else:
        shorter_list = correct_word_list
    current_word = len(shorter_list)
    if current_word == 0:
        # passes if no word has been typed
        pass
    for word in range(current_word):
        user_word = user_word_list[word]
        correct_word = correct_word_list[word]
        # checks which word is longer to prevent index errors
        if len(user_word) < len(correct_word):
            shorter_word = user_word
        else:
            shorter_word = correct_word

        for letter in range(len(shorter_word)):
            if user_word[letter] == correct_word[letter]:
                correct_characters += 1
            # #used for testing
            #     print(f"letter {user_word[letter]} is correct")
            # else:
            #     print(f"letter {user_word[letter]} is incorrect")
        if user_word == correct_word:
            correct_words += 1
        # #used for testing
        #     print(f"word {user_word} is correct")
        # else:
        #     print(f"word {user_word} is incorrect")
    # #used for testing
    # print(f"correct_words ={correct_words}")
    # print(f"correct_characters = {correct_characters}")

    # call calculate function
    calculate_score(count)


def calculate_score(count):
    global char_per_minute, words_per_minute
    try:
        char_per_minute = correct_characters / ((TEST_TIME - count) / MINUTE)
        words_per_minute = correct_words / ((TEST_TIME - count) / MINUTE)
    except ZeroDivisionError:
        # passes on first time being called to avoid divide by zero error
        pass
    else:
        result_label.config(text=f"CPM:{char_per_minute}      WPM:{words_per_minute}")


def check_key(key):
    global test_started
    if not test_started:
        # clear user entry field when key pressed
        user_input.delete(0, END)
        start_test()
    else:
        pass


def restart():
    # allows user to restart the test, clears input field and puts instruction in input field, changes testing variable
    global test_started
    test_started = False
    user_input.delete(0, END)
    user_input.insert(0, "Start typing here")


# create responsive grid
for i in range(4):
    window.grid_rowconfigure(i, weight=1)
window.grid_columnconfigure(0, weight=1)

# set min window size and other attributes
window.minsize(400, 300)
window.title("Typing Speed Test")

# Timer label for user
timer_label = Label(text="60" + " Seconds Remaining", font=BASE_FONT)
timer_label.grid(row=0, column=0, sticky=NSEW)

# Instructions and typing sentence label

instruction_text = Label(
    text="Welcome to the typing speed test, begin typing the sentence below in the text box to start", font=BASE_FONT)
instruction_text.grid(row=1, column=0, sticky=NSEW)
test_sentence = Label(text=TESTING_VALUE, font=TEST_FONT, bg="black", fg="white")
test_sentence.grid(row=2, column=0, sticky=NSEW)

# Results label
result_label = Label(text="CPM:      WPM:", font=BASE_FONT)
result_label.grid(row=4, column=0)

# User typing area
user_input = Entry()
user_input.insert(0, "Start typing here")
user_input.grid(row=3, column=0, sticky=NSEW)
user_input.bind("<Key>", check_key)

window.mainloop()
