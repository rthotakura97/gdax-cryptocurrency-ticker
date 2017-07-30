import gdax
import helpers
import time

global client
client = gdax.PublicClient()

def get_real_time(id):

    real_time = client.get_product_ticker(id)
    past_twenty_four = client.get_product_24hr_stats(id)

    strings_out = ["Price: ", "Size: ", "Last Trade ID: ", "Bid Price: ", "Ask Price: ", "Volume: ", "Trade Time: "]
    strings_api = ["price", "size", "trade_id", "bid", "ask", "volume", "time"]
    strings_day_out = ["Open: ", "High: ", "Low: ", "Last: ", "30 Day Volume: "]
    strings_day_api = ["open", "high", "low", "last", "volume_30day"]

    print("\nCurrent Info:")
    for i in range(0, len(strings_api)):
        print(strings_out[i] + str(real_time.get(strings_api[i])))

    print("\nPast 24 Hours:")
    for i in range(0, len(strings_day_api)):
        print(strings_day_out[i] + str(past_twenty_four.get(strings_day_api[i])))

def get_historical(id):

    print("\n")
    strings_out = ["Start Time: ", "Low: ", "High: ", "Open: ", "Close: ", "Volume: "]

    start = helpers.get_start_iso()
    end = helpers.get_end_iso()
    timeslice = input("Desired timeslice (in seconds): ")

    historical = client.get_product_historic_rates(id, start=start, end=end, granularity=int(timeslice))
    print("\nData:")
    for i in range (0,len(historical)):
        print("Bucket #: " + str(i))
        for j in range(0, len(strings_out)):
            if(j == 0):
                print(strings_out[j] + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(historical.__getitem__(i)[j])))
            else:
                print(strings_out[j] + str(historical.__getitem__(i)[j]))
        print("\n")

def get_trades(id):

    trades = client.get_product_trades(id)
    string_out = ["Time: ", "Trade ID: ", "Price: ", "Size: ", "Type: "]
    string_api = ["time", "trade_id", "price", "size", "side"]

    print("\nMost recent trades:")
    for i in range(0, len(trades)):
        for j in range(0, len(string_api)):
            print(string_out[j] + str(trades.__getitem__(i).get(string_api[j])))
        print("\n")