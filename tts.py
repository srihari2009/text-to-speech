import tkinter as tk
import pyttsx3 
 
engine = pyttsx3.init()

class Widget():
    def  __init__(self):
        self.root = tk.Tk()
        self.root.title('TTS')
        self.root.resizable(0,0)
        self.root.configure(background="blue")
        self.lable1 = tk.Label(self.root, bg= "red", fg="blue", font="Arial 20", text="what do you want me to speak?")
        self.lable1.pack()
        self.entry = tk.Entry(self.root, width=35, font="Arial 20")
        self.entry.pack(padx=20,pady=20)
        self.button = tk.Button(self.root, bg="red", fg="blue", text="speak!", command = self.clicked)
        self.button.pack(pady=20)
        self.root.mainloop()

    def clicked(self):
        text = self.entry.get()
        self.speak(text)

    def speak(self,text):
        engine.say(text)
        engine.runAndWait()

if __name__ ==  '__main__':
    temp = Widget()