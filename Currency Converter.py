import requests
import tkinter as tk
from ttkwidgets.autocomplete import AutocompleteCombobox
import decimal
import os

#Extraction
url = "https://openexchangerates.org/api/latest.json?app_id=cfba8a45cda24635a6b429a67e0a0607"  
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    rates = data.get("rates", {})
    currencylist = list(rates.keys())
    fullname = {
    'AED': 'United Arab Emirates Dirham',
    'AFN': 'Afghan Afghani',
    'ALL': 'Albanian Lek',
    'AMD': 'Armenian Dram',
    'ANG': 'Netherlands Antillean Guilder',
    'AOA': 'Angolan Kwanza',
    'ARS': 'Argentine Peso',
    'AUD': 'Australian Dollar',
    'AWG': 'Aruban Florin',
    'AZN': 'Azerbaijani Manat',
    'BAM': 'Bosnia and Herzegovina Convertible Mark',
    'BBD': 'Barbadian Dollar',
    'BDT': 'Bangladeshi Taka',
    'BGN': 'Bulgarian Lev',
    'BHD': 'Bahraini Dinar',
    'BIF': 'Burundian Franc',
    'BMD': 'Bermudian Dollar',
    'BND': 'Brunei Dollar',
    'BOB': 'Bolivian Boliviano',
    'BRL': 'Brazilian Real',
    'BSD': 'Bahamian Dollar',
    'BTC': 'Bitcoin',
    'BTN': 'Bhutanese Ngultrum',
    'BWP': 'Botswana Pula',
    'BYN': 'Belarusian Ruble',
    'BZD': 'Belize Dollar',
    'CAD': 'Canadian Dollar',
    'CDF': 'Congolese Franc',
    'CHF': 'Swiss Franc',
    'CLF': 'Chilean Unit of Account (UF)',
    'CLP': 'Chilean Peso',
    'CNH': 'Chinese Yuan (Offshore)',
    'CNY': 'Chinese Yuan',
    'COP': 'Colombian Peso',
    'CRC': 'Costa Rican Colón',
    'CUC': 'Cuban Convertible Peso',
    'CUP': 'Cuban Peso',
    'CVE': 'Cape Verdean Escudo',
    'CZK': 'Czech Republic Koruna',
    'DJF': 'Djiboutian Franc',
    'DKK': 'Danish Krone',
    'DOP': 'Dominican Peso',
    'DZD': 'Algerian Dinar',
    'EGP': 'Egyptian Pound',
    'ERN': 'Eritrean Nakfa',
    'ETB': 'Ethiopian Birr',
    'EUR': 'Euro',
    'FJD': 'Fijian Dollar',
    'FKP': 'Falkland Islands Pound',
    'GBP': 'British Pound Sterling',
    'GEL': 'Georgian Lari',
    'GGP': 'Guernsey Pound',
    'GHS': 'Ghanaian Cedi',
    'GIP': 'Gibraltar Pound',
    'GMD': 'Gambian Dalasi',
    'GNF': 'Guinean Franc',
    'GTQ': 'Guatemalan Quetzal',
    'GYD': 'Guyanese Dollar',
    'HKD': 'Hong Kong Dollar',
    'HNL': 'Honduran Lempira',
    'HRK': 'Croatian Kuna',
    'HTG': 'Haitian Gourde',
    'HUF': 'Hungarian Forint',
    'IDR': 'Indonesian Rupiah',
    'ILS': 'Israeli New Shekel',
    'IMP': 'Isle of Man Pound',
    'INR': 'Indian Rupee',
    'IQD': 'Iraqi Dinar',
    'IRR': 'Iranian Rial',
    'ISK': 'Icelandic Króna',
    'JEP': 'Jersey Pound',
    'JMD': 'Jamaican Dollar',
    'JOD': 'Jordanian Dinar',
    'JPY': 'Japanese Yen',
    'KES': 'Kenyan Shilling',
    'KGS': 'Kyrgyzstani Som',
    'KHR': 'Cambodian Riel',
    'KMF': 'Comorian Franc',
    'KPW': 'North Korean Won',
    'KRW': 'South Korean Won',
    'KWD': 'Kuwaiti Dinar',
    'KYD': 'Cayman Islands Dollar',
    'KZT': 'Kazakhstani Tenge',
    'LAK': 'Lao Kip',
    'LBP': 'Lebanese Pound',
    'LKR': 'Sri Lankan Rupee',
    'LRD': 'Liberian Dollar',
    'LSL': 'Lesotho Loti',
    'LYD': 'Libyan Dinar',
    'MAD': 'Moroccan Dirham',
    'MDL': 'Moldovan Leu',
    'MGA': 'Malagasy Ariary',
    'MKD': 'Macedonian Denar',
    'MMK': 'Burmese Kyat',
    'MNT': 'Mongolian Tugrik',
    'MOP': 'Macanese Pataca',
    'MRU': 'Mauritanian Ouguiya',
    'MUR': 'Mauritian Rupee',
    'MVR': 'Maldivian Rufiyaa',
    'MWK': 'Malawian Kwacha',
    'MXN': 'Mexican Peso',
    'MYR': 'Malaysian Ringgit',
    'MZN': 'Mozambican Metical',
    'NAD': 'Namibian Dollar',
    'NGN': 'Nigerian Naira',
    'NIO': 'Nicaraguan Córdoba',
    'NOK': 'Norwegian Krone',
    'NPR': 'Nepalese Rupee',
    'NZD': 'New Zealand Dollar',
    'OMR': 'Omani Rial',
    'PAB': 'Panamanian Balboa',
    'PEN': 'Peruvian Nuevo Sol',
    'PGK': 'Papua New Guinean Kina',
    'PHP': 'Philippine Peso',
    'PKR': 'Pakistani Rupee',
    'PLN': 'Polish Złoty',
    'PYG': 'Paraguayan Guarani',
    'QAR': 'Qatari Riyal',
    'RON': 'Romanian Leu',
    'RSD': 'Serbian Dinar',
    'RUB': 'Russian Ruble',
    'RWF': 'Rwandan Franc',
    'SAR': 'Saudi Riyal',
    'SBD': 'Solomon Islands Dollar',
    'SCR': 'Seychellois Rupee',
    'SDG': 'Sudanese Pound',
    'SEK': 'Swedish Krona',
    'SGD': 'Singapore Dollar',
    'SHP': 'Saint Helena Pound',
    'SLL': 'Sierra Leonean Leone',
    'SOS': 'Somali Shilling',
    'SRD': 'Surinamese Dollar',
    'SSP': 'South Sudanese Pound',
    'STD': 'São Tomé and Príncipe Dobra',
    'STN': 'São Tomé and Príncipe Dobra (new)',
    'SVC': 'Salvadoran Colón',
    'SYP': 'Syrian Pound',
    'SZL': 'Swazi Lilangeni',
    'THB': 'Thai Baht',
    'TJS': 'Tajikistani Somoni',
    'TMT': 'Turkmenistani Manat',
    'TND': 'Tunisian Dinar',
    'TOP': 'Tongan Pa\'anga',
    'TRY': 'Turkish Lira',
    'TTD': 'Trinidad and Tobago Dollar',
    'TWD': 'New Taiwan Dollar',
    'TZS': 'Tanzanian Shilling',
    'UAH': 'Ukrainian Hryvnia',
    'UGX': 'Ugandan Shilling',
    'USD': 'United States Dollar',
    'UYU': 'Uruguayan Peso',
    'UZS': 'Uzbekistani Som',
    'VES': 'Venezuelan Bolívar Soberano',
    'VND': 'Vietnamese Đồng',
    'VUV': 'Vanuatu Vatu',
    'WST': 'Samoan Tala',
    'XAF': 'Central African CFA Franc',
    'XAG': 'Silver Ounce (troy)',
    'XAU': 'Gold Ounce (troy)',
    'XCD': 'East Caribbean Dollar',
    'XDR': 'Special Drawing Rights',
    'XOF': 'West African CFA Franc',
    'XPD': 'Palladium Ounce (troy)',
    'XPF': 'CFP Franc',
    'XPT': 'Platinum Ounce (troy)',
    'YER': 'Yemeni Rial',
    'ZAR': 'South African Rand',
    'ZMW': 'Zambian Kwacha',
    'ZWL': 'Zimbabwean Dollar (2009)'
}

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
def meow():
    if cat["relief"] == "sunken":
        cat.configure(image=idle, relief="raised")
    else:
        cat.configure(image=heart, relief="sunken")
def seefull():
    z = dropdown3.get()
    try:
        searchlabel['text'] = fullname[z]
    except KeyError:
        searchlabel['text'] = 'Select a currency.'


#UI
root = tk.Tk()
root.title("Currency Converter")
root.geometry("500x300")
root.resizable(height = False, width = False)
#Widgets 
labelInput = tk.Label(root, text = "From:")
inputbox = tk.Entry(root, width = 30)
labelOutput = tk.Label(root, text = "To:")
labelOutput2 = tk.Label(root, textvariable= "")
button = tk.Button(root, width = 30, text = "Convert", command=choosefun)
switchbut = tk.Button(root, width = 10, text = "Switch", command=switching)
catlabel = tk.Label(root, text = "Emotional support cat, in case you had a bad day.",wraplength=60)
searchlabel = tk.Label(root, text = "")
searchbut = tk.Button(root, width = 10, text = "Search", command=seefull)


idlepath = os.path.join('sprites', 'idle cat.png')
heartpath = os.path.join('sprites', 'heart cat.png')
idle = tk.PhotoImage(file=idlepath)
heart = tk.PhotoImage(file=heartpath)
cat = tk.Button(root, image=idle, relief="raised", command=meow)


dropdown = AutocompleteCombobox(width=10, completevalues=currencylist)
dropdown2 = AutocompleteCombobox(width=10, completevalues=currencylist)
dropdown3 = AutocompleteCombobox(width=10, completevalues=currencylist)

#Placement
labelInput.grid(row=0, column=0, sticky=tk.E, padx=5, pady=5)
inputbox.grid(row=0, column=1, sticky=tk.W, padx=5, pady=5)
dropdown.grid(row=0, column=2, sticky=tk.E, padx=5, pady=5)
labelOutput.grid(row=1, column=0, sticky=tk.E, padx=5, pady=5)
labelOutput2.grid(row=1, column=1, sticky=tk.W, padx=5, pady=5)
dropdown2.grid(row=1, column=2, sticky=tk.E, padx=5, pady=5)
button.grid(row=2, column=1, sticky=tk.W, padx=5, pady=5)
switchbut.grid(row=2, column=2, sticky=tk.W, padx=5, pady=5)
cat.grid(row=3, column=1, sticky=tk.E, padx=5, pady=5)
catlabel.grid(row=3, column=2, sticky=tk.W, padx=5, pady=5)
dropdown3.grid(row=4, column=1, sticky=tk.E, padx=5, pady=5)
searchbut.grid(row=4, column=2, sticky=tk.E, padx=5, pady=5)
searchlabel.grid(row=4, column=3, sticky=tk.E, padx=5, pady=5)

root.mainloop()