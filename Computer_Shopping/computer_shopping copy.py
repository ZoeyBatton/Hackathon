msi_rtxa5000_price = 4199.35
gigabyte_aero_price = 4295.54
razer_blade15_price = 3696.99
asus_zephyrus_m16_price = 1849.79

products = [msi_rtxa5000_price, gigabyte_aero_price, razer_blade15_price, asus_zephyrus_m16_price]
names = ["MSI RTXA5000", "Gigabyte Aero", "Razer Blade 15", "ASUS Zephyrus M16"]
most_expensive = max(products)
least_expensive = min(products)
print(f"The most expensive laptop is ${most_expensive}")
print(f"The least expensive laptop is ${least_expensive}")

def list_amount():
    for price, name in zip (products, names):
        print("The price of " + (name), "is $", round(price))
list_amount()

def ave():
    average = sum(products) / len(products)
    print(f"The average of all of th elaptops is ${average:.2f}")
ave()