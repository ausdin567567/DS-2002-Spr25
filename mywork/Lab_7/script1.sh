#!/bin/bash

#Checking for 3 args
if [ "$#" -ne 3 ]; then
  echo "This is how it should be placed: $0 <local_file> <bucket_name> <expiration_seconds>"
  exit 1
fi

LOCAL_FILE=$1
BUCKET=$2
EXPIRES_IN=$3

# Making sure file exists
if [ ! -f "$LOCAL_FILE" ]; then
  echo "File '$LOCAL_FILE' not found."
  exit 1
fi

# Getting file name
FILE_NAME=$(basename "$LOCAL_FILE")

echo "Uploading '$LOCAL_FILE' to s3://$BUCKET/$FILE_NAME..."
aws s3 cp "$LOCAL_FILE" "s3://$BUCKET/$FILE_NAME" --acl private
echo "Generating a presigned URL good for $EXPIRES_IN seconds..."
aws s3 presign "s3://$BUCKET/$FILE_NAME" --expires-in "$EXPIRES_IN"
