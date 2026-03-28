# AWS S3 Enumeration Tool
Python 3.14.3

### Description
This script provides information on an account's S3 presence:
  - Listing the count of general purpose buckets in each region
  - Listing the name and creation date for each bucket
  - Listing the objects in each bucket

### Required Packages
See [requirements.txt](requirements.txt)

### Installation
- Clone the repo.
- Change directory to project root, e.g. ```cd awss3info```
- Install required libraries. ```pip install -r requirements.txt``` (Don't forget to source your venv _first_ if you're using one.)

### Usage
1. Install the demo.
2. Configure the credentials required to access your AWS account as per [the boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html). The initial permissions required for script functionality are:
[ec2:DescribeRegions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRegions.html)
[s3:ListAllMyBuckets](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListBuckets.html)
[s3:ListBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_ListObjectsV2.html)
