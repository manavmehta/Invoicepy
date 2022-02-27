## Scalability of the project

* The library `Invoicepy` is only _partially dependent_ on the system, ie. only in the sense that system must use `catalogItem` class bundled
    and the system's DB schema must be coherent to the attributes of the two classes.

* The catalog and orders reside on DB. Thus, no matter how huge the catalog is, or how many orders the orders DB has, vertical scalability prevails.

* The components have been split into `loggerUtil.py`, other utils in `utils.py` and the library in another directory, acting as a module itself.

* Due to logger configuration being in a separate file and not hard coded, ease of modification and scalability is prevailent.

* Further:
    - The cart can be stored per user and even if the user exits, the cart can reside on the DB itself. For that, every user must have their own DB
    linked to the main user DB by user_id foreign key
    
    - Platform Independence: The invoice object can be returned as a JSON object thus, it can be sent to different platforms.
