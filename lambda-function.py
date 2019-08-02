import json
import boto3

def lambda_handler(event, context):
    translate = boto3.client(service_name='translate', region_name='us-west-2')
    
    print(event);

    result = translate.translate_text(Text=event.get('text'), 
            SourceLanguageCode=event.get('source'), TargetLanguageCode=event.get('target'))
    return {
        'statusCode': 200,
        'body': result
    }
