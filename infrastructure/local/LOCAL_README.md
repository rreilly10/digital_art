```
localstack start -d


aws configure
AWS Access Key ID [None]: ACCESSKEYAWSUSER
AWS Secret Access Key [None]: sEcreTKey
Default region name [None]: us-west-2
Default output format [None]: json


aws --endpoint-url=http://localhost:4572 s3api put-bucket-acl --bucket demo-bucket --acl public-read
```

```
 1149  export AWS_SECRET_ACCESS_KEY="test"
 1150  export AWS_DEFAULT_REGION="us-east-1"
 1151  aws --endpoint-url=http://localhost:4566 kinesis list-streams
 1152  pip install awscli
 1153  aws configure --profile default
 1154  awslocal s3api create-bucket --bucket demo-bucket
 1155  aws s3 create-bucket --bucket demo-bucket
 1156  pip install awscli-local\n
 1157  awslocal s3api create-bucket --bucket demo-bucket
 1158  awslocal s3 ls
 1159  awslocal s3 ls demo-bucket
 1160  ls
 1161  aws s3 ls
 1162  awslocal s3 ls
 1163  aws s3 --help
 1164  awslocal s3 --help
 1165  awslocal s3
 1166  awslocal s3 awslocal s3api put-object --bucket demo-bucket --key images/
 1167  awslocal s3api put-object --bucket demo-bucket --key images/
 1168  awslocal s3 ls
 1169  awslocal s3 ls demo-bucket
 1170  awslocal s3 ls demo-bucket/images
 1171  cd code
 1172  ls
 1173  cd digital_art
 1174  ls
 1175  cd images
 1176  ls
 1177  awslocal s3api cp --recursive . demo-bucket/images -- dryrun
 1178  awslocal s3  cp --recursive . demo-bucket/images -- dryrun
 1179  awslocal s3  cp --recursive . demo-bucket/images
 1180  awslocal s3  cp --recursive . s3://demo-bucket/images
 1181  aws s3 ls demo-bucket/images
 1182  awslocal s3 ls demo-bucket/images
 1183  awslocal s3 ls demo-bucket/images/
 1184  awslocal s3 ls demo-bucket/images/out
 1185  awslocal s3 ls demo-bucket/images/out/
 1186  awslocal s3 ls demo-bucket/images/
 1187  env | grep key
 1188  env | grep KEY
 1189* pip install boto3
 1190* cd ..
 1191* ls
 1192* cd ..
 1193* ls
 1194* cd app
 1195* ls
 1196* python images.py
 1197* exit
 ```