from lesson17.proxy_patern.csv_reader import CsvReader
from lesson17.proxy_patern.csv_proxy_reader import CsvProxyReader

csv_reader = CsvReader('users.csv')
proxy_reader = CsvProxyReader(csv_reader)
print(proxy_reader.read())