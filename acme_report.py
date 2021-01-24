#!/usr/bin/env python

from random import randint, sample, uniform
from acme import Product

# Useful to use with random.sample to generate names
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult', 'Disguise', 'Mousetrap', '???']


def generate_products(num_products=30):
    products = []
    
    for i in range(num_products):
        name = f'{sample(ADJECTIVES,1)[0]} {sample(NOUNS,1)[0]}'
        price = randint(5,100)
        weight = randint(5, 100)
        flammability = uniform(0.0, 2.5)
        products.append(Product(name, price, weight, flammability))
    return products


def inventory_report(products):

    num_products = len(products)

    prods_info = [(prod.name, prod.price, prod.weight, prod.flammability) for prod in products]

    prod_names, prod_prices, prod_weights, prod_flammability = zip(*prods_info)
    
    unique_prod_names = set(prod_names)
    num_unique_prod_names  = len(unique_prod_names)

    avg_price = sum(prod_prices)/num_products
    avg_weight = sum(prod_weights)/num_products
    avg_flammability = sum(prod_flammability)/num_products

    print('ACME CORPORATION OFFICIAL INVENTORY REPORT')
    print(f'Unique product names: {num_unique_prod_names}')
    print(f'Average price: {avg_price:0.2f}')
    print(f'Average weight: {avg_weight}')
    print(f'Average flammability: {avg_flammability}')

if __name__ == '__main__':
    inventory_report(generate_products())