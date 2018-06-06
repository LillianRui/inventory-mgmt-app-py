import csv
import os

def menu(username="@prof-rossetti", products_count=100):
    # this is a multi-line string, also using preceding `f` for string interpolation
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
        'Reset'   | Reset the list of products.
    Please select an operation: """ # end of multi- line string. also using string interpolation
    return menu

csv_headers = ["id", "name", "aisle", "department", "price"]

def read_products_from_file(filename="products.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = []
    #TODO: open the file and populate the products list with product dictionaries
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        for ordered_dict in reader:
            products.append(dict(ordered_dict))
    return products



def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")
    #TODO: open the file and write a list of dictionaries. each dict should represent a product.
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=csv_headers)
        writer.writeheader()
        for product in products:
            writer.writerow(product)

def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    write_products_to_file(filename, products)


def auto_incremented_id (products):
    return int(products[-1]["id"])+1


def run():
    # First, read products from file...
    products = read_products_from_file()

    # Then, prompt the user to select an operation...
    #print(menu(username="@some-user")) #TODO instead of printing, capture user input
    number_of_products = len(products)
    my_menu = menu(username = "@some-user", products_count = number_of_products)
    operation = input(my_menu)
    #print("YOU CHOSE: " + operation)
    # Then, handle selected operation: "List", "Show", "Create", "Update", "Destroy" or "Reset"...
    operation = operation.title()

    if operation == "List":
        print("LISTING PRODUCTS")
        for p in products:
            print("..." + p["id"] +" "+ p["name"])


    elif operation == "Show":
        print("SHOWING A PRODUCT")
        product_id = input ("What's the id of the product you want to display?")
        print(product_id)
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        print(matching_product)


    elif operation == "Create":

        new_id = auto_incremented_id(products)
        new_product = input ("--What is your new product name?  ")
        new_aisle = input ("--What is your new product's aisle?  ")
        new_dept = input ("--What is your new product's department?  ")
        new_price = input ("--What is your new product's price?  ")
        new_product = {
            "id": new_id,
            "name": new_product,
            "aisle": new_aisle,
            "department": new_dept,
            "price": new_price
        } ## TODO:
        products.append(new_product)
        print("YOU HAVE CREATED A NEW PRODUCT: ", new_product)





    elif operation == "Update":
        product_id = input("What's the id of the product you would like to update?")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        update_product = input("--What is your new product name? Please type the original product name if there is no change:   ")
        update_aisle = input("--What is your new product aisle? Please type the original aisle name if there is no change: ")
        update_department = input("--What is your new product department? Please type the original department name if there is no change:  ")
        update_price = input("--What is your new product price? please type the original price if there is no change:  ")
        matching_product ={
            "id": product_id,
            "name": update_product,
            "aisle": update_aisle,
            "department": update_department,
            "price": update_price
        }
        print("YOU HAVE UPDATED A PRODUCT: ", matching_product)



    elif operation == "Destroy":
        product_id = input ("What's the id of the product you would like to destroy?")
        matching_products = [p for p in products if int(p["id"]) == int(product_id)]
        matching_product = matching_products[0]
        del products[products.index(matching_product)]
        print("DELETING A PRODUCT")


    elif operation == "Reset":
        reset_products_file()
        return

    else:
        print("Unrecognized Operation, please select one of 'List'，‘Show’,'Create', 'Update', 'Destory' or 'reset'.")

    # Finally, save products to file so they persist after script is done...
    write_products_to_file(products=products)
# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions
if __name__ == "__main__":
    run()
