# Write a function discounted price that take orginal price and discounted price as parameter and prints the final price after discount

def discounted_price (org, dis):
    discount = (dis/100)*org
    print(f"Final price = {org-discount}")

discounted_price(1000,50)