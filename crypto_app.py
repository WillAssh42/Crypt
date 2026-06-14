import tkinter as tk
import requests

# app root and corner image

root = tk.Tk()
root.title("Crypt")
root.geometry("400x150")

logo = tk.PhotoImage(file= r"C:\Users\willa\OneDrive\Desktop\Python\CryptoCoin App\Logo.png")
logo = logo.subsample(5)
label = tk.Label(root, image=logo)
label.lower()
label.place(x=3, y=-18, anchor="nw")

price_label = tk.Label(root, text="", font=("Arial", 16), fg="black")
price_label.place(x=200, y=35)

print("APP IS ONLINE")

# coin labels

def get_prices():
    print("FUNCTION RAN")
   
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,ripple,solana&vs_currencies=usd"

    response = requests.get(url)
    response = requests.get(url, timeout=5)
    data = response.json()
    print("API RESPONSE:", data)

    prices_text = (
            f"BTC: ${data['bitcoin']['usd']}\n"
            f"ETH: ${data['ethereum']['usd']}\n"
            f"XRP: ${data['ripple']['usd']}\n"
            f"SOL: ${data['solana']['usd']}"
        )
    price_label.config(text=prices_text)


    if "bitcoin" not in data:
     price_label.config(text="API ERROR / RATE LIMIT")
     root.after(30000, get_prices)
     return
    
    root.after(30000, get_prices)
    
get_prices()
root.mainloop()
