## Architecture of the CLI

Project directory tree
```
|___Invoicepy (Library)
|   |____ __init.py__
|   |____ catalogItem.py
|   |____ Invoice.py
|
|___Docs
|   |___architecure.md
|   |___scalability.md
|
|___Logs
|   |___0.log
|
|___sqldumps
|   |___catalog.sql
|   |___orders.sql
|
|___index.py - Entry point to the CLI
|
|___loggerUtil.py
|
|___utils.py
|
|___logger.config
|
|___README
```


### catalogItem Class
Contains information about a catalog item icluding its name, price, unique item id, discount, category, tax rate and final amount to be paid to checkout.<br>
Member functions `print()` and `printVerbose()` allow priting details of the `catalogItem`.


### Invoice Class
Contains information about the invoice including order_id, customer_id, checkout_amount, address, and cartItems (the items bought).<br>
Member function `print()` allows printing of the invoice as and when required.

