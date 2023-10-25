import requests
import tkinter as tk
import urllib, json

    
url = "https://openexchangerates.org/api/latest.json?app_id=cfba8a45cda24635a6b429a67e0a0607"
data = [i for i in requests.get(url).json()['rates']]
data.sort()

response = urllib.request.urlopen(url)
full = json.loads(response.read())

calc = full["rates"]

print(calc)

#UI
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x400")
root.resizable(height = False, width = False)
#widgets 
inn = tk.Entry(root, width = 30)

currency = tk.StringVar()
currency.set("USD")

dropdown = tk.OptionMenu(root, currency, *data).pack()
root.mainloop()
