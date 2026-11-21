from menu import MENU
import c2_total
def customer_discount(subtotal, customer): 
    if customer == "student":
        return subtotal * 0.9  
    elif customer == "staff":
        return subtotal * 0.75  
    else:
        return subtotal  

def happy_hour_discount(amount, hour):
    if 15 <= hour < 17:  
        return amount * 0.85  
    else:
        return amount 

def big_spender_bonus(amount): 
    if amount > 20:  
        return amount - 2 
    else:
        return amount 

def final_price(subtotal, customer, hour):
    cm_discount = customer_discount(subtotal, customer)
    hh_discount = happy_hour_discount(cm_discount, hour)
    bs_bonus = big_spender_bonus(hh_discount)
    if customer =="tourist":
        return round(bs_bonus, 2)
    else:
        return round(c2_total.addvat(bs_bonus), 2)

def main():
    code1 = input("Enter the first item code: ").strip().upper()
    code2 = input("Enter the second item code: ").strip().upper()
    code3 = input("Enter the third item code: ").strip().upper()
    customer = input("Enter customer type (student/staff/regular): ").strip().lower()
    hour = int(input("Enter the current hour (0-23): ").strip())
    
    if not code1 or code1 not in MENU:
        code1 = ""
        print("Item 1 is Unknown.")
    if not code2 or code2 not in MENU:
        code2 = ""
        print("Item 2 is Unknown.")
    if not code3 or code3 not in MENU:
        code3 = ""
        print("Item 3 is Unknown.")

    total , subtotal = c2_total.order_total(code1, code2, code3)
    

    print(f"The subtotal is: {subtotal:.2f} €")
    final_total = final_price(subtotal, customer, hour)
    print(f"The total price after discounts and bonuses is: {final_total:.2f} €")

if __name__ == "__main__":
    main()