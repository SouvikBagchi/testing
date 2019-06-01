import boto3
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

s3_resource.Object('jokerecommender', 'jokes.csv').download_file(
    f'/{'jokes.csv'}')