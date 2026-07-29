import movie_theater
import random


def main():

    print(random.randint(1, 2))

    customer_name = movie_theater.get_customer_name()
    ticket_count = movie_theater.get_ticket_count()
    print("ticket_count", ticket_count)
    total_ticket_price = movie_theater.calculate_total_price(ticket_count)
    print("total_ticket_price", total_ticket_price)
    discounted_final_price = movie_theater.apply_discount(total_ticket_price)
    print("discounted_final_price", discounted_final_price)
    receipt = movie_theater.create_receipt(customer_name, discounted_final_price)
    movie_theater.show_receipt(receipt)




if __name__ == "__main__":
    main()