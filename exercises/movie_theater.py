TICKET_PRICE = 40
DISCOUNT_AMOUNT = 10

def get_customer_name():
    return input("Enter customer name: ")

def get_ticket_count():
    return int(input("How many tickets to buy?: "))

def calculate_total_price(ticket_count):
    return TICKET_PRICE * ticket_count

def apply_discount(total_price):
    return total_price - DISCOUNT_AMOUNT

def create_receipt(customer_name, final_price):
    receipt = {customer_name: final_price}
    return receipt

def show_receipt(receipt):
    print(receipt)






