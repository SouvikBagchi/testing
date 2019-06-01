import boto3
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

bucket = s3_resource.Bucket('jokerecommender')
bucket.download_file('ratings.csv','ratingtest.csv')
