# import module
import boto3

# set service client
dynamodb = boto3.client('dynamodb', region_name='us-east-1')

# request user to input the name of the table they want to create
table_name = input("Input Table Name: ")

# create a function for code reusability
def create_table(client, table_name):
    # manually input fields vs list of dictionaries
    response = client.create_table(
        #  name the table by 
        TableName=table_name,
        # assign the primary key and sort key
        AttributeDefinitions=[
            {
                'AttributeName': 'Artist',
                'AttributeType': 'S',
            },
            {
                'AttributeName': 'SongTitle',
                'AttributeType': 'S',
            },
        ],
        KeySchema=[
            {
                'AttributeName': 'Artist',
                'KeyType': 'HASH',
            },
            {
                'AttributeName': 'SongTitle',
                'KeyType': 'RANGE',
            },
        ],    
        # assign both the read/write capacity units 
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        },
    )
    

if __name__ == "__main__": 
    create_table(dynamodb, table_name)
    print("Table Created:", table_name)
    
    