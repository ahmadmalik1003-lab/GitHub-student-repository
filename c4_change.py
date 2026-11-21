def make_change(amount_cents):
    amount_cents = int(round(amount_cents))  # Ensure amount is an integer
    change = {}
    
    if amount_cents <= 0:
        return change  # No change needed for zero or negative amounts
    else:

        if amount_cents >= 500:
            change['5€'] = amount_cents // 500
            amount_cents %= 500
        if amount_cents >= 200:
            change['2€'] = amount_cents // 200
            amount_cents %= 200
        if amount_cents >= 100:
            change['1€'] = amount_cents // 100
            amount_cents %= 100
        if amount_cents >= 50:
            change['50c'] = amount_cents // 50
            amount_cents %= 50 
        if amount_cents >= 20:
            change['20c'] = amount_cents // 20
            amount_cents %= 20
        if amount_cents >= 10:
            change['10c'] = amount_cents // 10
            amount_cents %= 10
        if amount_cents >= 5:
            change['5c'] = amount_cents // 5
            amount_cents %= 5
        if amount_cents >= 2:
            change['2c'] = amount_cents // 2
            amount_cents %= 2
        if amount_cents >= 1:
            change['1c'] = amount_cents // 1
            amount_cents %= 1  
        return change

def change_for(price, paid):
    if paid < price:
        return None  # Not enough money paid
    else:
        change_amount = int(round((paid - price) * 100))  # Convert to cents
        return make_change(change_amount)

def format_change(change_dict):
    if not change_dict:
        return "No change needed."
    
    formatted_change = ""
    if change_dict.get('5€'):
        formatted_change += f"{change_dict['5€']} x 5€\n"
    if change_dict.get('2€'):
        formatted_change += f"{change_dict['2€']} x 2€\n"
    if change_dict.get('1€'):
        formatted_change += f"{change_dict['1€']} x 1€\n"
    if change_dict.get('50c'):
        formatted_change += f"{change_dict['50c']} x 50c\n"
    if change_dict.get('20c'):
        formatted_change += f"{change_dict['20c']} x 20c\n"
    if change_dict.get('10c'):
        formatted_change += f"{change_dict['10c']} x 10c\n"
    if change_dict.get('5c'):
        formatted_change += f"{change_dict['5c']} x 5c\n"
    if change_dict.get('2c'):
        formatted_change += f"{change_dict['2c']} x 2c\n"
    if change_dict.get('1c'):
        formatted_change += f"{change_dict['1c']} x 1c\n"

    return formatted_change



def main():
    price = float(input("Enter the price of the item: "))
    paid = float(input("Enter the amount paid: "))
    
    change = change_for(price, paid)
    
    if change is None:
        print("Not enough money paid.")
    elif not change:
        print("No change needed.")
    else:
        print("Change to be given:")
        print(format_change(change))

if __name__ == "__main__":
    main()