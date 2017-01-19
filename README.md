# mototest

## Virtual ENV
```
namrata.patel@STSLP42  ~/PycharmProjects/mototest
$ virtualenv myenv2
```

## Installing requirements
```
(myenv2)
namrata.patel@STSLP42  ~/PycharmProjects/mototest
$ pip install -r requirements.txt
```

## Run Tests
```
lap  /d/orchardws/mototest (master)
$ py.test tests/ -v
```

Results:

```
============================= test session starts =============================
platform win32 -- Python 3.4.3, pytest-2.8.0, py-1.4.32, pluggy-0.3.1 -- c:\python34\python.exe
cachedir: tests\.cache
rootdir: D:\orchardws\mototest\tests, inifile:
plugins: mock-1.2, cov-2.2.0
collecting ... collected 1 items

tests\test_localization_db.py::test_one FAILED

================================== FAILURES ===================================
__________________________________ test_one ___________________________________

    def test_one():
        connection = get_resource()
>       main(connection)

tests\test_localization_db.py:62:
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
C:\Python34\Lib\site-packages\moto\core\models.py:70: in wrapper
    result = func(*args, **kwargs)
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

dynamodb = dynamodb.ServiceResource()

    @mock_dynamodb2
    def main(dynamodb):

            # Create the DynamoDB table.
            table = dynamodb.create_table(
                TableName='test-product_localization',
                KeySchema=[
                    {
                        'AttributeName': 'product_id',
                        'KeyType': 'HASH'
                    },
                    {
                        'AttributeName': 'language_id',
                        'KeyType': 'RANGE'
                    }
                ],
                AttributeDefinitions=[
                    {
                        'AttributeName': 'product_id',
                        'AttributeType': 'S'
                    },
                    {
                        'AttributeName': 'language_id',
                        'AttributeType': 'S'
                    },
                ],
                ProvisionedThroughput={
                    'ReadCapacityUnits': 5,
                    'WriteCapacityUnits': 5
                }
            )

            # Wait until the table exists.
>           table.meta.client.get_waiter('table_exists').wait(TableName='test-product_localization')
E           AttributeError: 'dict' object has no attribute 'meta'

tests\test_localization_db.py:44: AttributeError
========================== 1 failed in 2.24 seconds ===========================

```


System details
```
(myenv2)
lap  ~/PycharmProjects/mototest
$ python --version
Python 3.4.3
(myenv2)
lap  ~/PycharmProjects/mototest
$ pip --version
pip 9.0.1 from C:\Python34\Lib\site-packages (python 3.4)
```