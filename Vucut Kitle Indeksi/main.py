from tkinter import *

window=Tk()
window.title("Vucut Kitle Indeksi Hesaplama")
window.minsize(width=600 ,height=600)
def click_button():
    user_input_kilo=float(entry.get())
    user_input_boy=float(boy_entry.get())
    bmi=user_input_kilo/(user_input_boy**2)
    result_label.config(text="Vücut Kitle İndeksiniz (BMI): {:.2f}".format(bmi))
    if bmi < 18.5:
        category_label.config(text="Durum: Zayıf")
    elif 18.5 <= bmi < 24.9:
        category_label.config(text="Durum: Normal")
    elif 24.9 <= bmi < 29.9:
        category_label.config(text="Durum: Fazla Kilolu")
    else:
        category_label.config(text="Durum: Obez")

kilo=Label(text="Enter Your Wight(kg)")
kilo.config(bg="black")
kilo.config(fg="white")
kilo.pack()

entry=Entry(width=50)
entry.pack()

boy=Label(text="Enter Your Height(cm)")
boy.config(bg="black")
boy.config(fg="white")
boy.pack()

boy_entry=Entry(width=50)
boy_entry.pack()

button=Button(text="Calculate",command=click_button)
button.config(width=20)
button.pack()

result_label = Label(text="", font=("Arial", 16))
result_label.pack()

category_label=Label(text="",font=("Arial",16))
category_label.pack()

window.mainloop()
