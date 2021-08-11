Github: https://github.com/aliyun/aliyun-openapi-python-sdk

Docs: https://www.alibabacloud.com/help/doc-detail/67117.htm

'''
pip install aliyun-python-sdk-core # Install the Alibaba Cloud SDK for Python core library.
pip install aliyun-python-sdk-rds # Install the ECS management library.
pip install aliyun-python-sdk-core-v3 # For Python 3x
'''

How to hide the KEY
1. Environment variables
export KEY="key"
2. Binary files
binaryConfig.py

How to use
1. Env vars
'''
import os
key = os.environ.get('KEY')
# or
# os.getenv
'''
2. Bin
'''
import io
with open("api_file.bin", encoding="utf-8") as binary_file:
    # Read the whole file at once
    api_key = binary_file.read()
str(api_key)
'''