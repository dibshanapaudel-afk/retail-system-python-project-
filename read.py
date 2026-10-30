def read_products(filename="product.txt"):
    prod_dictionary = {}
    with open("product.txt", "r") as file:
        for idx, line in enumerate(file, start=1):
            prod_dictionary[idx] = line.split(",")
    return prod_dictionary
