import csv

with open('./zillow.csv', 'r') as csvfile:
    house_specs = csv.reader(csvfile, delimiter=',')
    intro = print(
        "What do you want to do? A) print all file contents B) print n first records (where the user enters n) C) print summary information")
    intro_2 = print("D) print all house prices for houses that have a price higher than n (where n is entered by the user) E) print all house information for houses that have n bedrooms")
    function = input()
    if function == "A":
        for row in house_specs:
            print(f'{row}')

    if function == "B":
        number_records = int(input("How many records?"))

        first_row = True
        for row in house_specs:
            if first_row:
                first_row = False
                continue
            if number_records > 0:
                print(f'{row}')
                number_records -= 1

    if function == "C":
        rows = []
        list_prices = []
        cheaper_house_info = []

        first_row = True
        for row in house_specs:
            if first_row:
                first_row = False
                continue
            rows.append(row)
            list_prices.append(row[6])
        min_price = min(list_prices)

        x = 0
        while x < len(rows):
            if rows[x][6] == min_price:
                cheaper_house_info = rows[x]
            x += 1

        print("Summary:")
        print(f'Number of records:{len(rows)}')
        print(f'Most expensive house:{max(list_prices)}')
        print(f'Least expensive house info:{cheaper_house_info}')

    if function == "D":
        price_limit = int(input("What is the bottom price?"))
        rows = []
        list_houses_above_price = []

        first_row = True
        for row in house_specs:
            if first_row:
                first_row = False
                continue
            rows.append(row)

        x = 0
        while x < len(rows):
            if int(rows[x][6]) >= price_limit:
                list_houses_above_price.append(rows[x])
            x += 1

        print(f'Prices above {price_limit}: {list_houses_above_price}')

    if function == "E":
        number_bedrooms = int(input("How many bedrooms?"))
        rows = []
        list_houses_n_bedrooms = []

        first_row = True
        for row in house_specs:
            if first_row:
                first_row = False
                continue
            rows.append(row)

        x = 0
        while x < len(rows):
            if int(rows[x][2]) == number_bedrooms:
                list_houses_n_bedrooms.append(rows[x])
            x += 1

        print(f'Houses with {number_bedrooms} of bedrooms: {list_houses_n_bedrooms}')