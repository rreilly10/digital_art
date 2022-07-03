from boto3.session import Session
import boto3

endpoint_url = "http://localhost.localstack.cloud:4566"


def load_images_from_s3(bucket="demo-bucket"):
    s3 = boto3.client("s3", endpoint_url=endpoint_url)

    images = []
    for item in s3.list_objects(Bucket=bucket)["Contents"]:
        presigned_url = s3.generate_presigned_url(
            "get_object", Params={"Bucket": bucket, "Key": item["Key"]}, ExpiresIn=100
        )
        images.append(presigned_url)

    return images
