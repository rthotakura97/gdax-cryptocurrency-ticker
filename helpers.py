def get_currency():

    cur_arr = ['BTC', 'ETH']
    cur_flag = 0
    while (cur_flag == 0):
        currency = input("Select a cryptocurrency (0 for BTC, 1 for ETH): ")
        if(currency == "0" or currency == "1"):
            cur_flag = 1
            currency = cur_arr[int(currency)]
    return currency

def get_units():

    cur_units = ['USD', 'EUR', 'GBP']
    unit_flag = 0
    while (unit_flag == 0):
        unit = input("Select a currency (0 for USD, 1 for EUR): ")
        if (unit == "0" or unit == "1"):
            unit_flag = 1
            unit = cur_units[int(unit)]
    return unit

def get_start_iso():
    yr = input("Enter start year('YYYY'): ")
    month = input("Enter start month('MM'): ")
    day = input("Enter start day ('DD'): ")

    return (yr + "-" + month + "-" + day)

def get_end_iso():
    yr = input("Enter end year('YYYY'): ")
    month = input("Enter end month('MM'): ")
    day = input("Enter end day ('DD'): ")

    return (yr + "-" + month + "-" + day)
