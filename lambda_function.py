import json
import boto3
import base64

def lambda_handler(event, context):
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Headers': 'Content-Type',
        'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
    }

    try:
        # Parse the request body
        body = json.loads(event['body'])
        if 'body' not in body:
            raise ValueError("Missing 'body' field in request")
        
        image_data = body['body']
        
        # Decode the base64 string to binary data
        image_bytes = base64.b64decode(image_data)
        
        # Initialize the Rekognition client
        rekognition = boto3.client('rekognition')
        
        # Call Rekognition to detect labels
        response = rekognition.detect_labels(
            Image={'Bytes': image_bytes},
            MaxLabels=10,
            MinConfidence=80
        )
        
        # Return the response from Rekognition
        return {
            'statusCode': 200,
            'headers': headers,
            'body': json.dumps(response)
        }
    except json.JSONDecodeError:
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps("Invalid JSON format")
        }
    except Exception as e:
        # Return an error response
        return {
            'statusCode': 400,
            'headers': headers,
            'body': json.dumps(str(e))
        }
