
from c1_lookup import price_of
from menu import MENU


def addvat(price,vat = 1.19) -> float:
    return price * vat

def order_total(code1,code2,code3) -> tuple[float,float]:
    price1 = price_of(code1)
    price2 = price_of(code2)
    price3 = price_of(code3)

    if price1 < 0:
        price1 = 0
        
    if price2 < 0:
        price2 = 0
        
    if price3 < 0:
        price3 = 0
    subtotal = price1 + price2 + price3  
    totalvat = addvat(subtotal)
    return round(totalvat, 2), round(subtotal, 2)

def main():
    code1 = input("Enter the first item code: ").strip().upper()
    code2 = input("Enter the second item code: ").strip().upper()
    code3 = input("Enter the third item code: ").strip().upper()

    if not code1 or code1 not in MENU:
        code1 = ""
        print("Item 1 is Unknown.")
    if not code2 or code2 not in MENU:
        code2 = ""
        print("Item 2 is Unknown.")
    if not code3 or code3 not in MENU:
        code3 = ""
        print("Item 3 is Unknown.")
    total, subtotal = order_total(code1, code2, code3)
    print(f"The subtotal is: {subtotal:.2f} €")
    print(f"The total price including VAT is: {total:.2f} €")

if __name__ == "__main__":
    main()






    
    