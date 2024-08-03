def tax_calc(raw_pricer):
    tax = 0.2

    def calc():
        return tax * raw_pricer()

    return calc


@tax_calc
def get_car_price():
    return 1200


print(get_car_price())
