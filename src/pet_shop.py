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