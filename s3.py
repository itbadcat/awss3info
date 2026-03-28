from boto3 import client as b3_client

def get_b3_client(service_id, region='us-east-1'):
    """
    Creates a new boto3 client object with an optionally specified region.
    :param service_id: The AWS service to initialize the client for.
    :param region: The region to interact with. Default: us-east-1
    :return: A client object.
    """
    return b3_client(service_id, region_name=region)

if __name__ == '__main__':
    response = get_b3_client('ec2').describe_regions(AllRegions=True) # Get EC2 client to describe regions
    if 'Regions' in response:
        for region in response['Regions']:
            if region['OptInStatus'] == 'opt-in-not-required' or region['OptInStatus'] == 'opted-in':
                region_name = region['RegionName']
                s3_client = get_b3_client('s3', region=region_name)
                response = s3_client.list_buckets(BucketRegion=region_name)
                if 'Buckets' in response:
                    buckets = response['Buckets']
                    bucket_count = len(buckets)
                    print(f'{region_name}: {bucket_count}')
                    if bucket_count > 0:
                        for bucket in buckets:
                            bucket_name = bucket['Name']
                            print(f'  {bucket_name} - Created {bucket["CreationDate"]}')
                            response = s3_client.list_objects(Bucket=bucket_name)
                            if 'Contents' in response:
                                objects = response['Contents']
                                print(objects)
                            else:
                                print('    No objects')
