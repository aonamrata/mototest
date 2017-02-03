
import boto3
from moto import mock_s3, mock_dynamodb
from MyModel3 import MyModel


#decorator

# @mock_s3
# def test_my_model_save():
#     conn = boto3.resource('s3', region_name='us-east-1')
#     conn.create_bucket(Bucket='mybucket')
#
#     model_instance = MyModel('steve', 'is awesome')
#     model_instance.save()
#
#     assert conn.get_bucket('mybucket').get_key('steve') == b'is awesome'

#
# @mock_dynamodb
# def test_my_model_write():
#     conn = boto.connect_dynamodb()
#     mytable_table_schema = conn.create_schema(
#         hash_key_name='forum_name',
#         hash_key_proto_value=str,
#         range_key_name='subject',
#         range_key_proto_value=str
#     )
#
#     table = conn.create_table(
#         name='mytable',
#         schema=mytable_table_schema,
#         read_units=10,
#         write_units=10
#     )
#
#     model_instance = MyModel('steve', 'is awesome')
#     write = model_instance.write_db()
#     print(write)
#     # assert write == False
#     read = model_instance.read_db()
#     assert write == read


import boto3
from moto import mock_s3

@mock_s3
def us_east():
    s3 = boto3.resource('s3', region_name='us-east-1')
    s3.create_bucket(Bucket="blah")
    s3.Object('blah', 'hello.txt').put(Body="some text")
    s3.Object('blah', 'hello.txt').get()['Body']

@mock_s3
def eu_central():
    s3 = boto3.resource('s3', region_name='eu-central-1')
    s3.create_bucket(Bucket="blah")
    s3.Object('blah', 'hello.txt').put(Body="some text")
    s3.Object('blah', 'hello.txt').get()['Body']

print("us")
us_east()
print("eu")
eu_central()