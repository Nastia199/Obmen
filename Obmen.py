from idlelib.pyshell import usage_msg

import requests
import json
from tkinter import *
from tkinter import messagebox as mb


1 usage
def exchange():
    code = entry.get()

    if code:
        try:
            response = requests("https://open.er-api.com/v6/latest/USD")
            response.raise_for_status()
            data = response.json()
            if code in data["rates"]:
                exchange_rate = data["rates"][code]
                mb.showinfo ("Курс обмена",  f"Курс:{exchange_rate} {code} за 1 доллар")
    else:
        mb.showinfo ("Ошибка!"), f"Валюта"{code} не найдена!")

except Exception as e:
    mb.showinfo( "Ошибка!" ), f"Произошла ошибка: {e}.")

else:
mb.showwarning ( "Внимание!"), "Введите код валют!)"


window = Tk()
window.title("Курсы обмена валют")
window.geometry("360x180")

Label(text="Введите код валюты"). pack (padx=10, pady=10)

entry = Entry()
entry.pack(padx=10, pady=10)
Button(text= "Получить курс обмена к доллару", command=exchange).pack(pand=10, pand=10)

window.mainloop()


