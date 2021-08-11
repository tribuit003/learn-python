# -*- coding: utf8 -*-
import json

from config import *
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkresourcemanager.request.v20200331.ListResourceGroupsRequest import ListResourceGroupsRequest

if __name__ == '__main__':
    client = AcsClient(KEY_ID, KEY_SECRET, REGION_ID)
    request = ListResourceGroupsRequest()
    # request.set_accept_format('json')
    request.set_PageSize(100)
    response = client.do_action_with_exception(request)
    re_gr = json.loads(str(response, encoding = 'utf-8'))
    print(re_gr)