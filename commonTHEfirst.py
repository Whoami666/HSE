# -*- coding: utf-8 -*-
catalog = open("catalog", 'r')
catalog_file = []
product = catalog.readline().rstrip().split(";")
catalog_dict, printer = {}, ""
amount_of_products = 0
while len(product) == 3:
    catalog_dict[product[0]] = [product[1], product[2]]
    amount_of_products += 1
    product = catalog.readline().rstrip().split(";")


def read_catalog():
    printerer = ""
    counter = 1
    for products in catalog_dict:
        printerer += str(counter) + " товар: " + products + "; цена:" + catalog_dict[products][0] + "; количество:" + catalog_dict[products][1] + "\n"
        counter += 1
    return printerer


def count_overall_catalog():
    return amount_of_products


def count_product(number):
    i = 1
    for products in catalog_dict:
        if i == number:
            return int(catalog_dict[products][1])
        else:
            i += 1


def name_from_numbers(number):
    i = 1
    for products in catalog_dict:
        if i == number:
            return products
        else:
            i += 1


