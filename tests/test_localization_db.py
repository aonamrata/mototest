from boto3.session import Session
from moto import mock_dynamodb2

@mock_dynamodb2
def get_resource():
    session = Session()
    # Get the service resource
    dynamodb = session.resource('dynamodb')
    return dynamodb

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
        table.meta.client.get_waiter('table_exists').wait(TableName='test-product_localization')
        # this gives error:
        #AttributeError: 'dict' object has no attribute 'meta'

        # Print out some data about the table.
        print('================')
        print(table)
        # {} empty value


def insert_data(connection):
    table = connection.Table('test-product_localization')
    response = table.put_item({'product_id': 1, 'language_id': 1})
    print(response)


def test_one():
    connection = get_resource()
    main(connection)
    insert_data(connection)
