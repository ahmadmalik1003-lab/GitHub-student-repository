from c3_discount import customer_discount,big_spender_bonus,happy_hour_discount
from c2_total import addvat


def explain_price(subtotal, customer, hour):
    running_total = subtotal
    explanation = f"Subtotal: {subtotal:.2f} €\n"
    
    if customer == "student":
        customer_label = "Student -10%: "
        discount = round((subtotal*0.90)-subtotal,2)
        running_total = customer_discount(subtotal,customer)
        explanation += f' - {customer_label}{discount:.2f}€ → {running_total:.2f}€\n'

    elif customer == "staff":
        customer_label = "Staff -25%: "
        discount = round((subtotal*0.75)-subtotal,2)
        running_total = customer_discount(subtotal,customer)
        explanation += f' - {customer_label}{discount:.2f}€ → {running_total:.2f}€\n'
    else:
        customer_label = "Regular:"
        discount = "No discount"
        running_total = customer_discount(subtotal,customer)
        explanation += f' - {customer_label} {discount}€ → {running_total:.2f}€\n'

    if 15 <= hour < 17:
        discount = round((running_total*0.85)-running_total,2)
        running_total = happy_hour_discount(running_total,hour)  
        explanation += f' - Happy hour (-15%): {discount:.2f}€ → {running_total:.2f}€\n'
    else:
        explanation += f' - {hour} not in Happy Hour: No Discount → {running_total:.2f}\n' 

    if running_total > 20:  
        running_total = big_spender_bonus(running_total) 
        explanation += f' - Big-spender bonus (-2.00 €): -2.00 € → {running_total:.2f} €\n'
    else:
        explanation += f' - {running_total:.2f} under 20€: No Discount → {running_total:.2f} €\n'

    vat = round(running_total*0.19,2)
    running_total = round(addvat(running_total),2)
    explanation += f' + VAT (19%): {vat:.2f} → {running_total:.2f} €\n'

    final = running_total
    explanation += f'FINAL: {round(running_total,2):.2f}€'

    return explanation


def main(): 
    subtotal = float(input("Enter Subtotal: "))
    customer = input("Enter Customer: ").strip()
    hour = int(input("Enter Hour(0-23): "))
    explaintion = explain_price(subtotal,customer,hour)
    print(explaintion)

if __name__ == "__main__":
    main()