import requests
import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox
import urllib, json
import decimal

#Extraction
url = "https://openexchangerates.org/api/latest.json?app_id=cfba8a45cda24635a6b429a67e0a0607"
response = urllib.request.urlopen(url)
full = json.loads(response.read())
rates = full["rates"] #Dictionary of all currency exchange USD based
currencylist = [i for i in rates]

class Calculate:
    def __innit__(self,base,converted):
        self.base = decimal.Decimal(base)
        self.converted = decimal.Decimal(converted)
    def toUSD(self, base):
        self.base = decimal.Decimal(base)
        self.converted = round((self.base / decimal.Decimal(rates.get(self))),4)
        return self.converted
    def toOTHER(self, base):
        self.base = decimal.Decimal(base)
        self.converted = round((self.base * decimal.Decimal(rates.get(self))),4)
        return self.converted

#UI
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x400")
root.resizable(height = False, width = False)
#widgets 
labelInput = tk.Label(root, text = "From:")
inputbox = tk.Entry(root, width = 30)
labelOutput = tk.Label(root, text = "To:")
labelOutput2 = tk.Label(root, textvariable= "")


currency = tk.StringVar()
currency.set("USD")

dropdown = AutocompleteCombobox(width=10, completevalues=currencylist)
dropdown2 = AutocompleteCombobox(width=10, completevalues=currencylist)

#Placement
labelInput.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
inputbox.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
dropdown.grid(row=0, column=2, sticky=tk.E, padx=5, pady=5)
labelOutput.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
labelOutput2.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
dropdown2.grid(row=1, column=2, sticky=tk.E, padx=5, pady=5)

root.mainloop()
