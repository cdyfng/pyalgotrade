import sqlite3
import csv, codecs, cStringIO
class UnicodeWriter:
    """
    A CSV writer which will write rows to CSV file "f",
    which is encoded in the given encoding.
    """
    def __init__(self, f, dialect=csv.excel, encoding="utf-8", **kwds):
        # Redirect output to a queue
        self.queue = cStringIO.StringIO()
        self.writer = csv.writer(self.queue, dialect=dialect, **kwds)
        self.stream = f
        self.encoder = codecs.getincrementalencoder(encoding)()
    def writerow(self, row):
        self.writer.writerow([unicode(s).encode("utf-8") for s in row])
        # Fetch UTF-8 output from the queue ...
        data = self.queue.getvalue()
        data = data.decode("utf-8")
        # ... and reencode it into the target encoding
        data = self.encoder.encode(data)
        # write to the target stream
        self.stream.write(data)
        # empty queue
        self.queue.truncate(0)
    def writerows(self, rows):
        for row in rows:
            self.writerow(row)
#conn = sqlite3.connect('ipaddress.sqlite3.db')
conn = sqlite3.connect('./okcoin_0.1.db')
c = conn.cursor()
c.execute("SELECT datetime(start, 'unixepoch', 'localtime'), open, high, low, close,volume from candles_CNY_BTC")
writer = UnicodeWriter(open("export_data.csv", "wb"))
writer.writerows(c)
c.close()
conn.close()