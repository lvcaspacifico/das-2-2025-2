import boto3

s3_client = boto3.resource("s3", region_name="us-east-1")
bucket = s3_client.Bucket("lucaspacifico11022002")

for obj in bucket.objects.all():
    print(f"Objeto: {obj.key} | Tamanho: {obj.size}")