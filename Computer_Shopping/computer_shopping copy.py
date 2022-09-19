msi_rtxa5000_price = 4199.35
gigabyte_aero_price = 4295.54
razer_blade15_price = 3696.99
asus_zephyrus_m16_price = 1849.79


products = [msi_rtxa5000_price, gigabyte_aero_price, razer_blade15_price, asus_zephyrus_m16_price]
names = ["MSI RTXA5000", "Gigabyte Aero", "Razer Blade 15", "ASUS Zephyrus M16"]
most_expensive = max(products)
least_expensive = min(products)
print(most_expensive)
print(least_expensive)
num = len(products)
x = 0
def list_amount():

    
    for price in products: 
        
        print(round(price))
    
   
    # while x == 0:
    
        # print(new[x])
        # x += 1
        # print(new[x])
        # x += 1
        # print(new[x])
        # x += 1
        # print(new[x])
        # for x in range(num):
        # print(new[x])
        # x += 1
        
        # if x == len(products):
        #     break

    # y = len(products)
    # if x == y:
        
    #     return x
list_amount()
 
def ave():
    average = sum(products) / len(products)
    print(f"{average:.2f}")
ave()
# def round():
    
#     return products

# round()
# msi_price, gig_price, razer_price, asus_price msi_rtxa5000_price, gigabyte_aero_price, razer_blade15_price, asus_zephyrus_m16_price

# def laptop_prices(most_expensive, least_expensive):
#     print(f"The most expensive laptop amount is: ${most_expensive}")
#     print(f"The least expensive laptop amoutn is: ${least_expensive}")
#     msi_price = round(msi_rtxa5000_price)
#     print(f"The rounded price of the MSI RTX 5000 is ${msi_price}")
#     gigabyte_price = round(gigabyte_aero_price)
#     print(f"The rounded price of the Gigabyte Aero is ${gigabyte_price}")
#     razer_price = round(razer_blade15_price)
#     print(f"The rounded price of the Razer Blade 15 is ${razer_price}")
#     asus_price = round(asus_zephyrus_m16_price)
#     print(f"The rounded price of the Asus Zephyrus is ${asus_price}")
#     average = (msi_rtxa5000_price + gigabyte_aero_price + razer_blade15_price + asus_zephyrus_m16_price) / 4
#     print(f"The average price of all computers is: ${average:.2f}")

# laptop_prices(gigabyte_aero_price, asus_zephyrus_m16_price)
