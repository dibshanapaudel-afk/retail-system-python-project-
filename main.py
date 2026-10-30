import datetime
from read import read_products
from write import generate_bill
from operation import process_sale, process_purchase, update_product_file

def main():
    prod_dictionary = read_products()
    while True:
        print("Welcome to WeCare Wholesale System")
        print("1. Sale to Customer")
        print("2. Purchase from Manufacturer")
        print("3. Exit")
        prod_options= input("Enter your option: ")

        if prod_options == "1" or prod_options == "2":
            name = input("Customer Name: ")
            phone_number = input("Customer Phone Number: ")
            now = datetime.datetime.now()
            dt = str(now)  # no strftime used
            if prod_options == "1":
                items, total = process_sale(prod_dictionary)
            else:
                items, total = process_purchase(prod_dictionary)
            shipping_input = input("Need shipping? (Y/N): ")
            if shipping_input.upper() == "Y":
                shipping_charge = 500
            else:
                shipping_charge = 0
            grand_total = total + shipping_charge
            update_product_file(prod_dictionary)
            filename = name + "" + phone_number + ".txt"
            generate_bill(filename, {"name": name, "phone": phone_number, "datetime": dt}, items, total, shipping_charge, grand_total)
            print("Bill saved to " + filename)
        elif prod_options == "3":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid Selections. Try again.")

if __name__ == "__main__":
    main()

