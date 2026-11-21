from datetime import datetime
from c1_lookup import price_of, name_of
from c3_discount import final_price
from c4_change import change_for,format_change
from c2_total import order_total



'''
def print_receipt(code1, code2, code3, customer, hour, paid): #first attempt 
    now = datetime.now()
    total,subtotal = order_total(code1,code2,code3)

    print("---------------------")
    print("     CAFÉ LAMBDA     ")
    print(now.strftime("%d-%m-%Y"),now.strftime("%H:%M"))
    print("-----------------------------------------------")
    print(f'{name_of(code1)}             {price_of(code1)}€')
    print(f'{name_of(code2)}             {price_of(code2)}€')
    print(f'{name_of(code3)}             {price_of(code3)}€')
    print("-----------------------------------------------")
    print(f'Subtotal: {subtotal}€')
    if customer == "student":
        print(f'Student 10%: {round((subtotal * 0.9) - subtotal,2)}€' ) 
    elif customer == "staff":
        print(f'Staff 25%: {round((subtotal * 0.75 ) - subtotal,2)}€' ) 
    else:
        print("Regular: No Discount")
    print(f'Vat 19%: {round((subtotal*1.19)-subtotal,2)}€')  
    print(f'TOTAL: {final_price(subtotal,customer,hour)}€')
    print(f'Paid: {paid}€')
    print(f'Change: {round (paid - final_price(subtotal,customer,hour),2)}€\n{format_change(change_for(final_price(subtotal,customer,hour),paid))}')
    print("-----------------------------------------------")
    print(f"     Thank you, {customer}!     ")
    print("-----------------------------------------------")
'''

def print_receipt_pretty(code1, code2, code3, customer, hour, paid):    #Refined Attempt ith correct aligment
    now = datetime.now()
    total,subtotal = order_total(code1,code2,code3)
    if customer == "student":
        customer_label = "Student 10%: "
        discount = round((subtotal*0.90)-subtotal,2)
    elif customer == "staff":
        customer_label = "Staff 25%: "
        discount = round((subtotal*0.75)-subtotal,2)
    else:
        customer_label = "Regular"
        discount = "No discount"
    Vat = round(((subtotal + discount)*0.19),2)
    total = final_price(subtotal,customer,hour)
    change = round(paid - total,2)
    if paid >= total:
        print(f'''
--------------------------
        CAFÉ LAMBDA
{now.strftime("%d-%m-%Y")}{now.strftime("%H:%M")}       
--------------------------
{f"{name_of(code1):<18}{price_of(code1):>6.2f} €" if code1 else ""}
{f"{name_of(code2):<18}{price_of(code2):>6.2f} €" if code2 else ""}
{f"{name_of(code3):<18}{price_of(code3):>6.2f} €" if code3 else ""}
--------------------------
{"Subtotal:":<18}{subtotal:>6}€
{customer_label:<18}{discount:>6}€
{"VAT 19%:":<18}{Vat:>6}€
{"TOTAL:":<18}{total:>6}€
{"Paid:":<18}{paid:>6}€
{"Change:":<18}{change:>6}€
{format_change(change_for(final_price(subtotal,customer,hour),paid))}
==========================
   Thank you, {customer}
==========================
    ''')
    else:
        print("Transaction Declined")
   

def main():
    code1 = input("Enter the first item code: ").strip().upper()
    code2 = input("Enter the second item code: ").strip().upper()
    code3 = input("Enter the third item code: ").strip().upper()
    customer = input("Enter customer type (student/staff/regular): ").strip().lower()
    hour = datetime.now().hour
    paid = float(input("Enter the amount paid: "))
    print_receipt_pretty(code1, code2, code3, customer, hour, paid)
    

if __name__ == "__main__":
    main()