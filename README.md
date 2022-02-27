# InvoicePy
The library provides functionality to generate invoice from a cart - a list of catalog items.

## Installation:
* Download the code
* Install the mysql dumps and fill up the .env variables
* Download and set up a mysql server. Refer [this document](https://www.digitalocean.com/community/tutorials/how-to-install-mysql-on-ubuntu-20-04) by Digital Ocean.
* run `pip install -r requirements.txt`
* run `python3 index.py`

## Structure

Invoicepy<br>
|____ \_\_init.py\_\_<br>
|____ catalogItem.py<br>
|____ Invoice.py<br>


### catalogItem Class
Contains information about a catalog item icluding its name, price, unique item id, discount, category, tax rate and final amount to be paid to checkout.<br>
Member functions `print()` and `printVerbose()` allow priting details of the `catalogItem`.


### Invoice Class
Contains information about the invoice including order_id, customer_id, checkout_amount, address, and cartItems (the items bought).<br>
Member function `print()` allows printing of the invoice as and when required.

