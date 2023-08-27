import time
from lesson20.conftest import dashboard, driver

def test_go2_sales_and_discount(dashboard):
    dashboard.go_to_sales_and_discounts()
    time.sleep(5)