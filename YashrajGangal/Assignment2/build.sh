#!/bin/bash -x

# This expects file lambda_function.py and utilities.py to be present
# The output is a zip file called S3ToRDBLoader.zip

rm -rf package/* | true
rmdir package | true
mkdir package

# Install dependencies in package folder
pip freeze > requirements.txt
pip install --target ./package -r requirements.txt

# Zip together
cd package
zip -r ../S3ToRDBLoader.zip .

cd ..
zip S3ToRDBLoader.zip lambda_function.py
zip S3ToRDBLoader.zip utilities.py

rm -rf package/*
rmdir package
