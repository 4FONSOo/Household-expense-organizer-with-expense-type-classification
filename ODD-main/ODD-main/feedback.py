from tkinter import Tk, Label, Text, Entry, Button, messagebox
import os
from datetime import datetime

class Feedback:
    def __init__(self, master):
        self.master = master
        master.title('Feedback')
        master.geometry('300x350')
        master.configure(background='#e9edf5')
        master.resizable(width=False, height=False)

        self.label_feedback = Label(master, text='Deixe seu feedback:', font=('Verdana 10 bold'), background='#e9edf5')
        self.label_feedback.grid(row=0, column=0, padx=10, pady=10, sticky='w')

        self.text_feedback = Text(master, width=30, height=8, font=('Verdana 10'))
        self.text_feedback.grid(row=1, column=0, padx=10, pady=10)

        self.label_username = Label(master, text='Seu Nome:', font=('Verdana 10 bold'), background='#e9edf5')
        self.label_username.grid(row=2, column=0, padx=10, pady=10, sticky='w')

        self.entry_username = Entry(master, font=('Verdana 10'))
        self.entry_username.grid(row=3, column=0, padx=10, pady=10)

        self.button_enviar = Button(master, text='Enviar', command=self.enviar_feedback, font=('Verdana 10 bold'),
                                     background='#038cfc', foreground='#ffffff')
        self.button_enviar.grid(row=4, column=0, padx=10, pady=10)

    def enviar_feedback(self):
        feedback_text = self.text_feedback.get('1.0', 'end-1c')
        username = self.entry_username.get()
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  #OBTÉM A DATA ATUAL

        #GUARDA O FEEDBACK NUM ARQUIVO .TXT COM A DATA E O NOME DO USER
        with open('feedback.txt', 'a') as arquivo:
            arquivo.write(f'{current_date} - {username}: {feedback_text}\n')

        messagebox.showinfo('Feedback Enviado', 'Obrigado pelo seu feedback!')

        self.master.destroy()