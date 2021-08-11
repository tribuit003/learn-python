from config import *
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
client = AcsClient(KEY_ID, KEY_SECRET, REGION_ID)
request = CommonRequest()
# Call an RPC API operation
request.set_domain('ecs.aliyuncs.com')
request.set_version('2014-05-26')
request.set_action_name('DescribeInstanceStatus')
# or:
# request = CommonRequest(domain='ecs.aliyuncs.com', version='2014-05-26', action_name='DescribeInstanceStatus')
request.add_query_param('PageNumber', '1')
request.add_query_param('PageSize', '30')
response = client.do_action_with_exception(request)
print(response)

# Call a RESTful API operation
# request.set_domain('cs.aliyuncs.com')
# request.set_version('2015-12-15')
# request.set_uri_pattern('/clusters')
# # or:
# # request = CommonRequest(domain='ecs.aliyuncs.com', version='2014-05-26', uri_pattern='/clusters')
# response = client.do_action_with_exception(request)
# print(response)