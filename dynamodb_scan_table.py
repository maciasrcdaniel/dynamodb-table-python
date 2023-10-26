# import modules
import boto3
from boto3.dynamodb.conditions import Key 

# set up client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# retrieve the table and store it in variable named table
table = dynamodb.Table('new_music_table')

# scan the table to look for songs by specific artist
response = table.scan(
    FilterExpression = Key('Artist').eq('Zac Brown Band')
)

# iterate through the findings and print the song titles
for songs in response['Items']: 
    print(songs['Artist'], '-',  songs['SongTitle'], '-', songs['Genre'] )



