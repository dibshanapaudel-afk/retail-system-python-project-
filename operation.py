def display_products(prod_dictionary, sale=True):
    print("S.N.\tProduct Name\tCompany Name\tQuantity\tPrice\tCountry")
    print("------------------------------------------------------------")
    for idx in prod_dictionary:
        data = prod_dictionary[idx]
        unit_price = int(data[3])
        if sale:
            unit_price *= 2
        print(str(idx) + "\t" + data[0] + "\t" + data[1] + "\t" +
              data[2] + "\t" + str(unit_price) + "\t" + data[4])  

def update_product_file(prod_dictionary, filename="product.txt"):
    with open(filename, "w") as file:
        for values in prod_dictionary.values():
            file.write(",".join(values) + "\n")

def process_sale(prod_dictionary):
    product_purchased = []
    total = 0
    while True:
        display_products(prod_dictionary, sale=True )
        try:
            product_id = int(input("Enter Product ID to purchase: "))
            product_quantity = int(input("Enter quantity: "))
            product = prod_dictionary[product_id]
            stock = int(product[2])
            free_item = product_quantity // 3
            if product_quantity + free_item > stock:
                print("Insufficient stock.")
                continue
            product[2] = str(stock - product_quantity - free_item)
            unit_price = int(product[3]) * 2
            total_price = unit_price * product_quantity
            product_purchased.append([product[0], product_quantity, unit_price, total_price, free_item])
            total = total + total_price
        except:
            print("Invalid input.")
            continue
        more = input("Add more items? (Y/N): ")
        if more.upper() != "Y":
            break
    return product_purchased, total

def process_purchase(prod_dictionary):
    product_purchased = []
    total = 0
    while True:
        display_products(prod_dictionary, sale=False)
        try:
            product_id = int(input("Enter Product ID to add stock: "))
            qty = int(input("Enter quantity: "))
            product = prod_dictionary[product_id]
            product[2] = str(int(product[2]) + product_quantity)
            price = int(product[3])
            total_price = product_quantity * price
            product_purchased.append([product[0], product_quantity, unit_price, total_price])
            grand_total = total + total_price
        except:
            print("Invalid input.")
            continue
        more = input("Add more items? (Y/N): ")
        if more.upper() != "Y":
            break
    return product_purchased, total
