'''
Author: Guinter Chissengue

Program Title: Grocery Store Receipt Program

Program Description: This program reads two CSV files: one that contains a list of products sold by a grocery store and another that contains 
a customer's order. The program looks up each requested product in the product catalog, calculates the subtotal, 
sales tax, and total amount due, and then prints a receipt to the terminal.
The program also handles common errors such as missing files and unknown product IDs.

Learning Objectives: Practice reading data from CSV files, Use dictionaries to store and retrieve data, Apply exception handling using try and except
Perform basic calculations with numbers, Format and display output clearly in the terminal.

Modules Used: csv, datetime

Function Names: read_dictionary, main

Enhancements: The program prints a return by date that is 30 days in the future at 9:00 PM.
'''


import csv
from datetime import datetime, timedelta


def read_dictionary(filename, key_column_index):
    dictionary = {}

    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row

    return dictionary


def main():
    try:
        products_dict = read_dictionary('products.csv', 0)

        print('Inkom Emporium')

        total_items = 0
        subtotal = 0

        with open('request.csv', 'r', newline='') as file:

            reader = csv.reader(file)
            next(reader)

            for row in reader:
                product_id = row[0]
                quantity = int(row[1])

                product = products_dict[product_id]
                name = product[1]
                price = float(product[2])

                print(f'{name}: {quantity} @ {price:.2f}')

                total_items += quantity
                subtotal += price * quantity

        sales_tax = subtotal * 0.06
        total = subtotal + sales_tax

        print(f'Number of Items: {total_items}')
        print(f'Subtotal: {subtotal:.2f}')
        print(f'Sales Tax: {sales_tax:.2f}')
        print(f'Total: {total:.2f}')

        print('Thank you for shopping at the Inkom Emporium.')

        current_date = datetime.now()
        print(current_date.strftime('%a %b %d %H:%M:%S %Y'))

        return_date = current_date + timedelta(days=30)
        return_date = return_date.replace(hour=21, minute=0, second=0)
        print('Return by:', return_date.strftime('%a %b %d %H:%M:%S %Y'))

    except FileNotFoundError as error:
        print('Error: missing file')
        print(error)

    except PermissionError as error:
        print('Error: permission denied')
        print(error)

    except KeyError as error:
        print('Error: unknown product ID in the request.csv file')
        print(error)


if __name__ == '__main__':
    main()
