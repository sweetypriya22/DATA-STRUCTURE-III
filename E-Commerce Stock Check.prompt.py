'''
E-Commerce Stock Check
In an e-commerce system, detecting categories with a large number of items is crucial for effective inventory management.
By identifying categories with more than three items, you can ensure that popular categories are stocked well, 
while under-stocked categories can be prioritised for restocking.
You are given a nested tuple representing product categories and their associated items. 
Each category is represented by a tuple in the following format:
The first element is the category name
The second element is a tuple of items, where each item is represented by a tuple of the form
item_name
quantity
Your task is to write a function filter_heavy_stock(categories) that:
Unpacks each category
Returns a tuple of category names where the number of items in that category exceeds three (i.e., categories with three or fewer items should not be included in the result)

Input Format
A nested tuple representing product categories, where each category is a tuple of the form (category_name: str, items: tuple).
Each item in the items tuple is itself a tuple
item_name (str)
quantity (int)

'''

# Import literal_eval to safely evaluate string input as a Python literal
from ast import literal_eval

# Taking the input
categories = literal_eval(input())

def filter_heavy_stock(categories):
    # Write your code here     
    New =[]
    for i,b in categories:
        if len(b)>3:
            New.append(i)
    return tuple(New)


# Print the output
print(filter_heavy_stock(categories))