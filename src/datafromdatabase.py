import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    #data=[{'thingname':'firstthing', 'temperature':'37.8'}]
    resource = boto3.resource('dynamodb')
    table = resource.Table('TrainingThings')
    scanned_data = table.scan()
    print(scanned_data)
    data = scanned_data['Items']
    
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin' : '*', # Required for CORS support to work
            'Access-Control-Allow-Credentials' : True # Required for cookies, authorization headers with HTTPS 
        },
        'body': json.dumps(data)
    }
