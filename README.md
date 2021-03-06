Raas
=================
This API SDK was automatically generated by APIMATIC v2.0

This SDK uses the Requests library and will work for Python ```2 >=2.7.9``` and Python ```3 >=3.4```.

How to configure:
=================
The generated code might need to be configured with your API credentials. 
To do that, open the file "Configuration.py" and edit its contents.

How to resolve dependencies: 
===========================
The generated code uses Python packages named requests, jsonpickle and dateutil.
You can resolve these dependencies using pip ( https://pip.pypa.io/en/stable/ ).

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r requirements.txt```

Note: You will need internet access for this step.

How  to test:
=============
You can test the generated SDK and the server with automatically generated test
cases. unittest is used as the testing framework and nose is used as the test
runner. You can run the tests as follows:

  1. From terminal/cmd navigate to the root directory of the SDK.
  2. Invoke ```pip install -r test-requirements.txt```
  3. Invoke ```nosetests```

How to use:
===========
After having resolved the dependencies, you can easily use the SDK following these steps.

  1. Create a "raas_test.py" file in the root directory.
  2. Use any controller as follows:
```python
from __future__ import print_function
from raas.raas_client import RaasClient

api_client = RaasClient()
controller = api_client.status
response = controller.get_system_status(<required parameters if any>)

print(response.status)

# Or you can print more information
print(vars(response))
```