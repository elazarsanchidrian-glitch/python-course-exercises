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

def main():
    customer_name = get_customer_name()
    ticket_count = get_ticket_count()
    print("ticket_count", ticket_count)
    total_ticket_price = calculate_total_price(ticket_count)
    print("total_ticket_price", total_ticket_price)
    discounted_final_price = apply_discount(total_ticket_price)
    print("discounted_final_price", discounted_final_price)
    receipt = create_receipt(customer_name, discounted_final_price)
    show_receipt(receipt)


if __name__ == "__main__":
    main()



