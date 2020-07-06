import boto3
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = ''
SECRET_KEY = ''


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False


def getUsedSpace(aBucketName):
    s3 = boto3.resource('s3', aws_access_key_id=ACCESS_KEY,
                        aws_secret_access_key=SECRET_KEY)

    space = 0
    for bucket in s3.buckets.all():
        myBucketName = bucket.name
        for key in bucket.objects.all():
            space = space + key.size
            # print(key.key)
        print('Used space in bucket ' + myBucketName +
              ' ' + str(space // (2 ** 20)) + ' Megabytes')


# Main
localFile = '/images/gotIt.jpg'
s3File = 'imagesTest/gotIt.jpg'
bucketName = 'voti-public'


#uploaded = upload_to_aws(localFile, bucketName, s3File)
usedSpace = getUsedSpace(bucketName)
