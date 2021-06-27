from tkinter import *
from tkinter import messagebox as msg_box
import requests

guiWindow = Tk()
guiWindow.title('COVID - 19 SYMPTOM CHECKER & TRACKER')
guiWindow.geometry('700x600')


# Displaying message for severe symptoms
def severe_message():
    msg_box.showinfo("Result",
                     "You have some severe COVID-19 symptoms seek immediate medical care")


# Check symptoms
def consult_btn():
    if chk_box_common_sym_1.get() == 1 or chk_box_common_sym_2.get() == 1 or chk_box_common_sym_3.get() == 1:
        msg_box.showinfo("Result", "You have some common COVID-19 symptoms")

        if chk_box_severe_sym_4.get() == 1 or chk_box_severe_sym_5.get() == 1 or chk_box_severe_sym_6.get() == 1 \
                or chk_box_severe_sym_7.get() == 1 or chk_box_severe_sym_8.get() == 1:
            severe_message()

    elif chk_box_severe_sym_4.get() == 1:
        severe_message()

    elif chk_box_severe_sym_5.get() == 1:
        severe_message()

    elif chk_box_severe_sym_6.get() == 1:
        severe_message()

    elif chk_box_severe_sym_7.get() == 1:
        severe_message()

    elif chk_box_severe_sym_8.get() == 1:
        severe_message()

    else:
        msg_box.showinfo("Result",
                         "Other less common symptoms are: Irritability,\n Confusion,\n "
                         "Reduced consciousness (sometimes associated with seizures),\n Anxiety,\n Depression,\n "
                         "Sleep disorders,\n More severe and rare neurological complications such as strokes, "
                         "brain inflammation, delirium and nerve damage.")


# Calling COVID-19 data API to get the world data
def covid_world_data_btn():
    url = "https://covid-19-data.p.rapidapi.com/totals"

    headers = {
        'x-rapidapi-key': "71029e7278msh6c878f2e65d8f94p1c3886jsn428a97d445e8",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)

    msg_box.showinfo("Covid-19 Cases in World", response.text)


# Calling COVID-19 data API to get the Indian data
def covid_india_data_btn():
    url = "https://covid-19-data.p.rapidapi.com/country/code"

    querystring = {"code": "in"}

    headers = {
        'x-rapidapi-key': "71029e7278msh6c878f2e65d8f94p1c3886jsn428a97d445e8",
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    msg_box.showinfo("Covid-19 Cases in India", response.text)


frame1 = Label(guiWindow, bg='#dddddd')
frame1.pack()

chk_box_common_sym_1 = IntVar()
chk_box_common_sym_2 = IntVar()
chk_box_common_sym_3 = IntVar()

chk_box_severe_sym_4 = IntVar()
chk_box_severe_sym_5 = IntVar()
chk_box_severe_sym_6 = IntVar()
chk_box_severe_sym_7 = IntVar()
chk_box_severe_sym_8 = IntVar()

# Adding checkboxes to frame
Checkbutton(frame1, text="Dry Cough", variable=chk_box_common_sym_1, onvalue=1, offvalue=0).grid(row=4, columnspan=10,
                                                                                                 pady=5)
Checkbutton(frame1, text="Fever", variable=chk_box_common_sym_2, onvalue=1, offvalue=0).grid(row=5, columnspan=7,
                                                                                             pady=5)
Checkbutton(frame1, text="Fatigue", variable=chk_box_common_sym_3, onvalue=1, offvalue=0).grid(row=6, columnspan=8,
                                                                                               pady=5)

Checkbutton(frame1, text="Cough, fever, difficulty in breathing or shortness of breath", variable=chk_box_severe_sym_4,
            onvalue=1, offvalue=0, ).grid(row=7, columnspan=15, pady=5)
Checkbutton(frame1, text="Persistent pain or pressure in the chest", variable=chk_box_severe_sym_5, onvalue=1,
            offvalue=0).grid(row=8, columnspan=5, pady=5)
Checkbutton(frame1, text="Loss of speech or movement", variable=chk_box_severe_sym_6, onvalue=1, offvalue=0).grid(row=9,
                                                                                                                  columnspan=2,
                                                                                                                  pady=5)
Checkbutton(frame1, text="Loss of appetite", variable=chk_box_severe_sym_7, onvalue=1, offvalue=0).grid(row=10,
                                                                                                        columnspan=12,
                                                                                                        pady=5)
Checkbutton(frame1, text="Confusion", variable=chk_box_severe_sym_8, onvalue=1, offvalue=0).grid(row=11, columnspan=9,
                                                                                                 pady=5)

# Adding buttons to main GUI window
Button(guiWindow, text="CHECK", command=consult_btn).pack(pady=20)
Button(guiWindow, text="Check Latest Covid-19 Cases in World", command=covid_world_data_btn).pack(pady=20)
Button(guiWindow, text="Check Latest Covid-19 Cases in India", command=covid_india_data_btn).pack()

guiWindow.mainloop()
