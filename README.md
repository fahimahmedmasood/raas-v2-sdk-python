# Getting started

With this RESTful API you can integrate a global reward or incentive program into your app or platform. If you have any questions or if you'd like to receive your own credentials, please contact us at devsupport@tangocard.com.

## How to Build


You must have Python ```2 >=2.7.9``` or Python ```3 >=3.4``` installed on your system to install and run this SDK. This SDK package depends on other Python packages like nose, jsonpickle etc. 
These dependencies are defined in the ```requirements.txt``` file that comes with the SDK.
To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type ```pip --version```.
This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including ```requirements.txt```) for the SDK.
* Run the command ```pip install -r requirements.txt```. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?step=installDependencies&workspaceFolder=Raas-Python)


## How to Use

The following section explains how to use the Raas SDK package in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=pyCharm)

Click on ```Open``` in PyCharm to browse to your generated SDK directory and then click ```OK```.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=openProject0&workspaceFolder=Raas-Python)     

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=openProject1&workspaceFolder=Raas-Python&projectName=raas)     

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?step=createDirectory&workspaceFolder=Raas-Python&projectName=raas)

Name the directory as "test"

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?step=nameDirectory)
   
Add a python file to this project with the name "testsdk"

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?step=createFile&workspaceFolder=Raas-Python&projectName=raas)

Name it "testsdk"

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```Python
from raas.raas_client import RaasClient
```

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?step=projectFiles&workspaceFolder=Raas-Python&libraryName=raas.raas_client&projectName=raas&className=RaasClient)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on ```Run```

![Run Test Project - Step 1](https://apidocs.io/illustration/python?step=runProject&workspaceFolder=Raas-Python&libraryName=raas.raas_client&projectName=raas&className=RaasClient)


## How to Test

You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

## Initialization

### Authentication
In order to setup authentication and initialization of the API client, you need the following information.

| Parameter | Description |
|-----------|-------------|
| platform_name | RaaS v2 API Platform Name |
| platform_key | RaaS v2 API Platform Key |



API client can be initialized as following.

```python
# Configuration parameters and credentials
platform_name = 'QAPlatform2' # RaaS v2 API Platform Name
platform_key = 'apYPfT6HNONpDRUj3CLGWYt7gvIHONpDRUYPfT6Hj' # RaaS v2 API Platform Key

client = RaasClient(platform_name, platform_key)
```



# Class Reference

## <a name="list_of_controllers"></a>List of Controllers

* [OrdersController](#orders_controller)
* [AccountsController](#accounts_controller)
* [CatalogController](#catalog_controller)
* [ExchangeRatesController](#exchange_rates_controller)
* [StatusController](#status_controller)
* [CustomersController](#customers_controller)
* [FundController](#fund_controller)

## <a name="orders_controller"></a>![Class: ](https://apidocs.io/img/class.png ".OrdersController") OrdersController

### Get controller instance

An instance of the ``` OrdersController ``` class can be accessed from the API Client.

```python
 orders_controller = client.orders
```

### <a name="create_order"></a>![Method: ](https://apidocs.io/img/method.png ".OrdersController.create_order") create_order

> TODO: Add a method description

```python
def create_order(self,
                     body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = CreateOrderRequestModel()

result = orders_controller.create_order(body)

```


### <a name="get_order"></a>![Method: ](https://apidocs.io/img/method.png ".OrdersController.get_order") get_order

> TODO: Add a method description

```python
def get_order(self,
                  reference_order_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| referenceOrderID |  ``` Required ```  | Reference Order ID |



#### Example Usage

```python
reference_order_id = 'referenceOrderID'

result = orders_controller.get_order(reference_order_id)

```


### <a name="get_orders"></a>![Method: ](https://apidocs.io/img/method.png ".OrdersController.get_orders") get_orders

> TODO: Add a method description

```python
def get_orders(self,
                   options=dict())
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| accountIdentifier |  ``` Optional ```  | TODO: Add a parameter description |
| customerIdentifier |  ``` Optional ```  | TODO: Add a parameter description |
| externalRefID |  ``` Optional ```  | TODO: Add a parameter description |
| startDate |  ``` Optional ```  | TODO: Add a parameter description |
| endDate |  ``` Optional ```  | TODO: Add a parameter description |
| elementsPerBlock |  ``` Optional ```  | TODO: Add a parameter description |
| page |  ``` Optional ```  | TODO: Add a parameter description |



#### Example Usage

```python
collect = {}

account_identifier = 'accountIdentifier'
collect['account_identifier'] = account_identifier

customer_identifier = 'customerIdentifier'
collect['customer_identifier'] = customer_identifier

external_ref_id = 'externalRefID'
collect['external_ref_id'] = external_ref_id

start_date = datetime.now()
collect['start_date'] = start_date

end_date = datetime.now()
collect['end_date'] = end_date

elements_per_block = 152
collect['elements_per_block'] = elements_per_block

page = 152
collect['page'] = page


result = orders_controller.get_orders(collect)

```


### <a name="create_resend_order"></a>![Method: ](https://apidocs.io/img/method.png ".OrdersController.create_resend_order") create_resend_order

> TODO: Add a method description

```python
def create_resend_order(self,
                            reference_order_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| referenceOrderID |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
reference_order_id = 'referenceOrderID'

result = orders_controller.create_resend_order(reference_order_id)

```


[Back to List of Controllers](#list_of_controllers)

## <a name="accounts_controller"></a>![Class: ](https://apidocs.io/img/class.png ".AccountsController") AccountsController

### Get controller instance

An instance of the ``` AccountsController ``` class can be accessed from the API Client.

```python
 accounts_controller = client.accounts
```

### <a name="get_account"></a>![Method: ](https://apidocs.io/img/method.png ".AccountsController.get_account") get_account

> Get an account

```python
def get_account(self,
                    account_identifier)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| accountIdentifier |  ``` Required ```  | Account Identifier |



#### Example Usage

```python
account_identifier = 'accountIdentifier'

result = accounts_controller.get_account(account_identifier)

```


### <a name="get_accounts_by_customer"></a>![Method: ](https://apidocs.io/img/method.png ".AccountsController.get_accounts_by_customer") get_accounts_by_customer

> Gets a list of accounts for a given customer

```python
def get_accounts_by_customer(self,
                                 customer_identifier)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerIdentifier |  ``` Required ```  | Customer Identifier |



#### Example Usage

```python
customer_identifier = 'customerIdentifier'

result = accounts_controller.get_accounts_by_customer(customer_identifier)

```


### <a name="create_account"></a>![Method: ](https://apidocs.io/img/method.png ".AccountsController.create_account") create_account

> Create an account under a given customer

```python
def create_account(self,
                       customer_identifier,
                       body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerIdentifier |  ``` Required ```  | Customer Identifier |
| body |  ``` Required ```  | Request Body |



#### Example Usage

```python
customer_identifier = 'customerIdentifier'
body = CreateAccountRequestModel()

result = accounts_controller.create_account(customer_identifier, body)

```


### <a name="get_all_accounts"></a>![Method: ](https://apidocs.io/img/method.png ".AccountsController.get_all_accounts") get_all_accounts

> Gets all accounts under the platform

```python
def get_all_accounts(self)
```

#### Example Usage

```python

result = accounts_controller.get_all_accounts()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="catalog_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CatalogController") CatalogController

### Get controller instance

An instance of the ``` CatalogController ``` class can be accessed from the API Client.

```python
 catalog_controller = client.catalog
```

### <a name="get_catalog"></a>![Method: ](https://apidocs.io/img/method.png ".CatalogController.get_catalog") get_catalog

> Get Catalog

```python
def get_catalog(self)
```

#### Example Usage

```python

result = catalog_controller.get_catalog()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="exchange_rates_controller"></a>![Class: ](https://apidocs.io/img/class.png ".ExchangeRatesController") ExchangeRatesController

### Get controller instance

An instance of the ``` ExchangeRatesController ``` class can be accessed from the API Client.

```python
 exchange_rates_controller = client.exchange_rates
```

### <a name="get_exchange_rates"></a>![Method: ](https://apidocs.io/img/method.png ".ExchangeRatesController.get_exchange_rates") get_exchange_rates

> Retrieve current exchange rates

```python
def get_exchange_rates(self)
```

#### Example Usage

```python

result = exchange_rates_controller.get_exchange_rates()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="status_controller"></a>![Class: ](https://apidocs.io/img/class.png ".StatusController") StatusController

### Get controller instance

An instance of the ``` StatusController ``` class can be accessed from the API Client.

```python
 status_controller = client.status
```

### <a name="get_system_status"></a>![Method: ](https://apidocs.io/img/method.png ".StatusController.get_system_status") get_system_status

> *Tags:*  ``` Skips Authentication ``` 

> Retrieve system status

```python
def get_system_status(self)
```

#### Example Usage

```python

result = status_controller.get_system_status()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="customers_controller"></a>![Class: ](https://apidocs.io/img/class.png ".CustomersController") CustomersController

### Get controller instance

An instance of the ``` CustomersController ``` class can be accessed from the API Client.

```python
 customers_controller = client.customers
```

### <a name="get_customer"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.get_customer") get_customer

> Get a customer

```python
def get_customer(self,
                     customer_identifier)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| customerIdentifier |  ``` Required ```  | Customer Identifier |



#### Example Usage

```python
customer_identifier = 'customerIdentifier'

result = customers_controller.get_customer(customer_identifier)

```


### <a name="create_customer"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.create_customer") create_customer

> Create a new customer

```python
def create_customer(self,
                        body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | Request Body |



#### Example Usage

```python
body = CreateCustomerRequestModel()

result = customers_controller.create_customer(body)

```


### <a name="get_all_customers"></a>![Method: ](https://apidocs.io/img/method.png ".CustomersController.get_all_customers") get_all_customers

> Gets all customers under the platform

```python
def get_all_customers(self)
```

#### Example Usage

```python

result = customers_controller.get_all_customers()

```


[Back to List of Controllers](#list_of_controllers)

## <a name="fund_controller"></a>![Class: ](https://apidocs.io/img/class.png ".FundController") FundController

### Get controller instance

An instance of the ``` FundController ``` class can be accessed from the API Client.

```python
 fund_controller = client.fund
```

### <a name="get_credit_cards"></a>![Method: ](https://apidocs.io/img/method.png ".FundController.get_credit_cards") get_credit_cards

> List all credit cards registered on this platform

```python
def get_credit_cards(self)
```

#### Example Usage

```python

result = fund_controller.get_credit_cards()

```


### <a name="create_credit_card"></a>![Method: ](https://apidocs.io/img/method.png ".FundController.create_credit_card") create_credit_card

> Register a new credit card

```python
def create_credit_card(self,
                           body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = CreateCreditCardRequestModel()

result = fund_controller.create_credit_card(body)

```


### <a name="create_unregister_credit_card"></a>![Method: ](https://apidocs.io/img/method.png ".FundController.create_unregister_credit_card") create_unregister_credit_card

> Unregister a credit card

```python
def create_unregister_credit_card(self,
                                      body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = UnregisterCreditCardRequestModel()

result = fund_controller.create_unregister_credit_card(body)

```


### <a name="create_deposit"></a>![Method: ](https://apidocs.io/img/method.png ".FundController.create_deposit") create_deposit

> Fund an account

```python
def create_deposit(self,
                       body)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| body |  ``` Required ```  | TODO: Add a parameter description |



#### Example Usage

```python
body = DepositRequestModel()

result = fund_controller.create_deposit(body)

```


### <a name="get_deposit"></a>![Method: ](https://apidocs.io/img/method.png ".FundController.get_deposit") get_deposit

> Get details for a specific credit card deposit

```python
def get_deposit(self,
                    deposit_id)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| depositId |  ``` Required ```  | Deposit ID |



#### Example Usage

```python
deposit_id = 'depositId'

result = fund_controller.get_deposit(deposit_id)

```


### <a name="get_credit_card"></a>![Method: ](https://apidocs.io/img/method.png ".FundController.get_credit_card") get_credit_card

> Get details for a specific credit card

```python
def get_credit_card(self,
                        token)
```

#### Parameters

| Parameter | Tags | Description |
|-----------|------|-------------|
| token |  ``` Required ```  | Card Token |



#### Example Usage

```python
token = 'token'

result = fund_controller.get_credit_card(token)

```


[Back to List of Controllers](#list_of_controllers)



