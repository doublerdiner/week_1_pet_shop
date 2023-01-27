# WRITE YOUR FUNCTIONS HERE

# Test 1 - Pet Shop Name
def get_pet_shop_name(pet_shop_details):
    return pet_shop_details["name"]

# Test 2 - Total Cash
def get_total_cash(pet_shop_details):
    return pet_shop_details["admin"]["total_cash"]

# Test 3 & 4 - Add or Remove Cash
def add_or_remove_cash(pet_shop_details, cash):
    pet_shop_details["admin"]["total_cash"] += cash

# Test 5 - Pets Sold
def get_pets_sold(pet_shop_details):
    return pet_shop_details["admin"]["pets_sold"]

# Test 6 - Increase Pets Sold
def increase_pets_sold(pet_shop_details, pets_sold):
    pet_shop_details["admin"]["pets_sold"] += pets_sold

# Test 7 - Stock Count
def get_stock_count(pet_shop_details):
    return len(pet_shop_details["pets"])

# Test 8 & 9 - Pets by Breed
def get_pets_by_breed(pet_shop_details, breed_name):
    pets_by_breed = []
    for pet in pet_shop_details["pets"]:
        if pet["breed"] == breed_name:
            pets_by_breed.append(pet)
    return pets_by_breed

# Test 10 & 11 - Find Pet by Name
def find_pet_by_name(pet_shop_details, pet_name):
    for pet in pet_shop_details["pets"]:
        if pet["name"] == pet_name:
            return pet
    return None

# Test 12 - Remove Pet by Name
def remove_pet_by_name(pet_shop_details, pet_name):
    pet = find_pet_by_name(pet_shop_details, pet_name)
    pet_shop_details["pets"].remove(pet)

# Test 13 - Add Pet to Stock
def add_pet_to_stock(pet_shop_details, new_pet):
    pet_shop_details["pets"].append(new_pet)

# Test 14 - Customer Cash
def get_customer_cash(customer):
    return customer["cash"]

# Test 15 - Remove Customer Cash
def remove_customer_cash(customer, cash_to_be_removed):
    customer["cash"] -= cash_to_be_removed

# Test 16 - Customer Pet Count
def get_customer_pet_count(customer):
    return len(customer["pets"])

# Test 17 - Add Pet to Customer
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)