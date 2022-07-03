"""
A virtual cookie shop.
Do not modify this file.
"""

# from pathlib import Path
# import cookie_shop

# # get data from the CSV file into a list
# filepath = Path("data/cookies.csv") # create a file path in a way that is both Mac- and Windows- compatible
# list_of_cookies = cookie_shop.bake_cookies(filepath)

# # open the cookie shop with the cookies read from the file
# # this must run the rest of the program as documented
# cookie_shop.run_shop(list_of_cookies)

# ###some shitty tries###
# # print(cookie_shop.bake_cookies(filepath))
# # cookies = cookie_shop.bake_cookies(filepath)
# # cookie_shop.display_cookies(cookies)
# # cookie_shop.get_cookie_from_dict(5,cookies)
# # cookie_shop.solicit_quantity(1, cookies)
# # order = cookie_shop.solicit_order(cookies)
# # cookie_shop.display_order_total(order, cookies)


### extra credit version ###
from pathlib import Path
import cookie_shop_extra_credit

# get data from the CSV file into a list
filepath = Path("data/cookies.csv") # create a file path in a way that is both Mac- and Windows- compatible
#list_of_cookies = cookie_shop_extra_credit.bake_cookies(filepath)

# open the cookie shop with the cookies read from the file
# this must run the rest of the program as documented
#cookie_shop_extra_credit.run_shop(list_of_cookies)

# cookie_shop_extra_credit.welcome()
cookie_shop_extra_credit.bake_cookies(filepath)
cookies = cookie_shop_extra_credit.bake_cookies(filepath)
cookie_shop_extra_credit.display_cookies(cookies)