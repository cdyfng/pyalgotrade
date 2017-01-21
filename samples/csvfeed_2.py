from pyalgotrade.feed import csvfeed

feed = csvfeed.Feed("Date", "%Y-%m-%d %H:%M:%S")
#feed.addValuesFromCSV("quandl_gold_2.csv")
feed.addValuesFromCSV("../tools/export_data.csv")

for dateTime, value in feed:
    print dateTime, value
