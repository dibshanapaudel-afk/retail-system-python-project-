def generate_bill(filename, customer_info, items, total, shipping_charge, grand_total):
    with open("product.txt", "w") as file:
        file.write("Product Shop Bill:\n")
        file.write("Macchapokhari, kathmandu | Phone No: 9877802255\n")
        file.write("------------------------------------------------------------------\n")
        file.write("Customer Details:\n")
        file.write("------------------------------------------------------------------\n")
        file.write("Name of the Customer: " + customer_info["name"] + "\n")
        file.write("Contact Number: " + customer_info["phone"] + "\n")
        file.write("Date and time of purchase: " + customer_info["datetime"] + "\n")
        file.write("------------------------------------------------------------------\n")
        file.write("Purchase Details:\n")
        file.write("------------------------------------------------------------------\n")
        file.write("Item Name\tQuantity\tFree\tUnit Price\tTotal\n")
        file.write("------------------------------------------------------------------\n")
        for i in product_purchased:
            file.write(item[0] + "\t" + str(item[1]) + "\t" +
                       str(item[4] if len(item) > 4 else 0) + "\t" +
                       str(item[2]) + "\t" + str(item[3]) + "\n")
        file.write("------------------------------------------------------------------\n")
        if shipping_charge > 0:
            file.write("Shipping Charge: " + str(shipping_charge) + "\n")
        file.write("Grand Total: " + str(grand_total) + "\n")
