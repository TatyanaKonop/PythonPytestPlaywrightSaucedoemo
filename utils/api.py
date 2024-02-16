import re


def extract_number(row_price: str):
    price = round(float(re.search(r'\b\d+\.\d+\b', row_price)[0]), 2)
    return price


def find_sum_elements(row_elements):
    sum = 0
    for i in row_elements:
        int_price = round(float(extract_number(i.text_content())), 2)
        sum += int_price
    return sum



