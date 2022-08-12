#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# You work at Len’s Slice, a new pizza joint in the neighborhood.
# You are going to use your knowledge of Python lists to organize some of your sales data.
# Make some changes to pizzas offered based on what supply is available at the market that week. 
# Then print the final menue, along with the most and least expernsive pizzas.

# Code: 

toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]
num_two_dollar_slices = prices.count(2)
num_pizzas = len(toppings)
print("We sell", num_pizzas, "different kinds of pizza!")
pizza_and_prices = [[2,"pepperoni"], [6,"pineapple"], [1, "cheese"], [3,"sausage"], [2,"olives"], [7, "anchovies"], [2, "mushrooms"]]
pizza_and_prices.sort()

pizza_and_prices.pop()
pizza_and_prices.insert(1, [2.5,"peppers"])
pizza_and_prices.sort()
print('Final Menue: ', pizza_and_prices)

three_cheapest = pizza_and_prices[:3]
three_priciest = pizza_and_prices[4:]
print('Our 3 cheapest pizzas are ', three_cheapest)
print('Our 3 most expensive pizzas are ', three_priciest)