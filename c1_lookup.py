from menu import MENU

def price_of(code:str) -> float:
    return MENU.get(code,{}).get("price", -1)
def name_of(code:str) -> str:
    return MENU.get(code, {}).get("name", "Unknown")

def category_of(code:str) -> str:
    return MENU.get(code, {}).get("category", "Unknown")

def describe(code:str) -> str:
    price = price_of(code)
    if price < 0:
        return "Unknown item."
    else:
        return f"The {name_of(code)} costs {price:.2f} €"


def main():
    code = input("Item code: ").strip().upper()
    print(describe(code))

if __name__ == "__main__":
    main()