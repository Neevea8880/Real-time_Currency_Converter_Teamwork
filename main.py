import requests
from tkinter import *
import tkinter.messagebox
from PIL import ImageTk, Image

root=Tk()
root.title("Real-time currency converter")
root.geometry("800x500")
frame1 = Frame(root, highlightbackground="black", highlightthickness=4,width=800, height=500, bd= 0)
frame1.pack()

photo = ImageTk.PhotoImage(Image.open("C:\\Users\\user\\PycharmProjects\\Real-time_Currency_converter\\pic.png"))
img_label = Label(frame1,image=photo)
img_label.pack()

convert_from = Label(root,font=('Helvetica',17,'bold'), text = "  Convert from : ",fg="black",borderwidth=1,relief="solid")
convert_from.place(x = 135,y = 100)
convert_to = Label(root,font=('Helvetica',17,'bold'), text = "  Convert to : ",fg="black",borderwidth=1,relief="solid")
convert_to.place(x = 500,y = 100)
user_from_entry_area = Entry(root, width = 18, font=('Helvetica',17,'bold'),bd=5, bg="#cce0ff")
user_from_entry_area.place(x = 100,y = 175 )
user_to_entry_area = Entry(root, width = 18, font=('Helvetica',17,'bold' ),bd =5, bg="#cce0ff")
user_to_entry_area.place(x = 460,y = 175)

input = StringVar(root)
output = StringVar(root)
input.set("Select")
output.set("Select")

Currency_list = ['USD','EUR','JPY','BGN','CZK','DKK','GBP','HUF','PLN','RON','SEK','CHF','ISK','NOK','HRK','RUB','TRY','AUD','BRL','CAD','CNY','HKD','IDR','INR','KRW','MXN','MYR','NZD','PHP','SGD','THB','ZAR']
From_Currency = OptionMenu(root,input, *Currency_list)
From_Currency["menu"].config(bg="#cce0ff")
To_Currency = OptionMenu(root,output, *Currency_list)
To_Currency["menu"].config(bg="#cce0ff")

From_Currency.place(x=180, y=270)
To_Currency.place(x=550, y=270)

def CurrencyConversion() :
    if (user_to_entry_area.get() == "") :

        input_currency = input.get()
        output_currency = output.get()

        if (user_from_entry_area.get() == ""):
            tkinter.messagebox.showerror("Error", "Enter your amount.\n")

        elif (input_currency == "Select" or output_currency == "Select"):
            tkinter.messagebox.showerror("Error", "Select currency.\n")

        else:

            api_key = "XYCXDGONCRLY5X9M"

            base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

            main_url = base_url + "&from_currency=" + input_currency + "&to_currency=" + output_currency + "&apikey=" + api_key


            req_ob = requests.get(main_url)

            result = req_ob.json()

            Exchange_Rate = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])

            amount = float(user_from_entry_area.get())

            new_amount = round(amount * Exchange_Rate, 3)

            user_to_entry_area.insert(0, str(new_amount))
    else:
        tkinter.messagebox.showerror("Error", "If you want to convert again, RESET and enter new amount.\n")

def clear():
    user_from_entry_area.delete(0, END)
    user_to_entry_area.delete(0, END)
    input.set("Select")
    output.set("Select")

convert_btn = Button(root,font=('Helvetica',13,'bold'),bg="#2EDBF2", text = 'CONVERT', bd = '5', command= CurrencyConversion)
convert_btn.place(x = 300,y = 375)
clear_btn = Button(root,font=('Helvetica',13,'bold'),bg="#2EDBF2", text = '  CLEAR  ', bd = '5', command= clear)
clear_btn.place(x = 430,y = 375)

root.mainloop()

