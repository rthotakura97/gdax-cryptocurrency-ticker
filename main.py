import api_handler
import helpers

print ("Cryptocurrency Ticker: Latest prices, stats, and historic data.\n")
reprompt = "0"

while (reprompt == "0"):

    currency = helpers.get_currency()
    unit = helpers.get_units()

    concatenated_unit = currency + "-" + unit
    req_flag = 0
    while (req_flag == 0):
        request = input("Select type of information (0 for real-time, 1 for historical, 2 for trades): ")
        if(request == "0"):
            req_flag =1
            api_handler.get_real_time(concatenated_unit)
        if(request == "1"):
            req_flag = 1
            api_handler.get_historical(concatenated_unit)
        if(request == "2"):
            req_flag = 1;
            api_handler.get_trades(concatenated_unit)

    reprompt = input("\nPress 0 to restart, or press any other key to quit")
    if(reprompt != "0"):
        break
