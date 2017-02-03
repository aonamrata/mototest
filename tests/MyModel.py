import boto
from boto.s3.key import Key

class MyModel(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def save(self):
        conn = boto.connect_s3()
        bucket = conn.get_bucket('mybucket')
        k = Key(bucket)
        k.key = self.name
        k.set_contents_from_string(self.value)

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