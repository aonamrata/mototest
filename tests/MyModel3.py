import boto3

class MyModel(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def save(self):
        s3 = boto3.resource('s3', region_name='us-east-1')
        # Print out bucket names
        # for bucket in s3.buckets.all():
        #     print(bucket.name)

        s3.Object('mybucket', 'film_localization.py').put(
            Body=open('D:/tmp/film_localization.py', 'rb'))

        # Upload a new file
        # s3.Bucket('mybucket').put_object(Key=self.name,
        #                                  Body=bytes(self.value, 'utf-8'))


    def write_db(self):
        conn = boto.connect_dynamodb()
        table = conn.get_table('mytable')

        item_data = {
            'forum_name': self.name,
            'subject': self.value
        }
        item = table.new_item(
            # Our hash key is 'forum'
            hash_key= self.name,
            # Our range key is 'subject'
            range_key= self.value
            # This has the
            # attrs=item_data
        )
        item.put()
        return item

    def read_db(self):
        conn = boto.connect_dynamodb()
        table = conn.get_table('mytable')

        item = table.get_item(
            # Your hash key was 'forum_name'
            hash_key=self.name,
            # Your range key was 'subject'
            range_key=self.value
        )

        return item