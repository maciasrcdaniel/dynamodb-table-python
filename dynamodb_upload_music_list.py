# import modules
import boto3
import json

# resource will be used instead of client
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

# assign the table name we created to a new variable
table = dynamodb.Table('new_music_table')

# read through the file and assign the contents to json_file temporarily
with open('music_list.json') as json_file: 
    music_list = json.load(json_file)
    #iterate through the items in the json file and match the fields
    for music in music_list: 
        artist = music['Artist']
        song_title = music['SongTitle']
        genre = music['Genre']
        # print progress status
        print("Adding music files:", artist, song_title)
        # put the items from our iterated list into our table 
        table.put_item(
            Item = {
                'Artist': artist, 
                'SongTitle': song_title,
                'Genre': genre
                }
            )
            
print("All items have been upload!")