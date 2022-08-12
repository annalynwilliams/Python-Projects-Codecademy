#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Furniture for Neat Suites on Fleet Street. With our newfound knowledge of Python programming, we’re going to build a system to help speed up the process of creating receipts for your customers.
# In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.

# Code:
    
lovely_loveseat_description = '''Loveseat: Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'''
lovely_loveseat_price = 254.00

stylish_settee_description = '''
Settee: Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'''
stylish_settee_price = 180.50

luxurious_lamp_description = '''
Lamp: Glass and iron. 36 inches tall. Brown with cream shade.'''
luxurious_lamp_price = 52.15

sales_tax = .088

customer_one_total = 0
customer_one_itemization = ''
customer_one_total = lovely_loveseat_price
customer_one_itemization = lovely_loveseat_description
customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description
customer_one_tax = sales_tax*customer_one_total
customer_one_total += customer_one_tax 
print('Items Purchased:')
print(customer_one_itemization)
print('Total Cost (after tax): customer_one_total')