```
localstack start -d

aws configure
AWS Access Key ID [None]: ACCESSKEYAWSUSER
AWS Secret Access Key [None]: sEcreTKey
Default region name [None]: us-west-2
Default output format [None]: json
```

### Localstack AWS Setup
```
export AWS_SECRET_ACCESS_KEY="test"
export AWS_DEFAULT_REGION="us-east-1"

aws configure --profile default
```

### Image Bucket Creation
```
awslocal s3api create-bucket --bucket demo-bucket
awslocal s3  cp --recursive . s3://demo-bucket/images
aws s3 ls demo-bucket/images
```