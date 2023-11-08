import requests
import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox
import decimal

#Extraction
url = "https://openexchangerates.org/api/latest.json?app_id=cfba8a45cda24635a6b429a67e0a0607"  
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    rates = data.get("rates", {})
    currencylist = list(rates.keys())

def toUSD(base):
    base = decimal.Decimal(base)
    converted = round((base / decimal.Decimal(rates[dropdown.get()])),4)
    return converted
def toOTHER(base):
    base = decimal.Decimal(base)
    converted = round((base * decimal.Decimal(rates[dropdown2.get()])),4)
    return converted
def choosefun():
    try: 
        x = inputbox.get()
        decimal.Decimal(x)
        if dropdown.get() == dropdown2.get():
            labelOutput2['text'] = x
        elif dropdown.get() == 'USD':
            labelOutput2['text'] = toOTHER(x)
        elif dropdown.get() != 'USD':
            x = toUSD(x)
            if dropdown2.get() == 'USD':
                labelOutput2['text'] = x
            else:
                labelOutput2['text'] = toOTHER(x)
    except: 
            labelOutput2['text'] = 'Invalid input. Enter a number.'
def switching():
    x = dropdown.get()
    y = dropdown2.get()
    dropdown.set(y)
    dropdown2.set(x)
    
#UI
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x200")
root.resizable(height = False, width = False)
#Widgets 
labelInput = tk.Label(root, text = "From:")
inputbox = tk.Entry(root, width = 30)
labelOutput = tk.Label(root, text = "To:")
labelOutput2 = tk.Label(root, textvariable= "")
button = tk.Button(root, width = 30, text = "Convert", command=choosefun)
switchbut = tk.Button(root, width = 10, text = "Switch", command=switching)

dropdown = AutocompleteCombobox(width=10, completevalues=currencylist)
dropdown2 = AutocompleteCombobox(width=10, completevalues=currencylist)

#Placement
labelInput.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
inputbox.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
dropdown.grid(row=0, column=2, sticky=tk.E, padx=5, pady=5)
labelOutput.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
labelOutput2.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
dropdown2.grid(row=1, column=2, sticky=tk.E, padx=5, pady=5)
button.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
switchbut.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)

root.mainloop()
