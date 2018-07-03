# coding:utf-8
# @author : csl
# @date   : 2018/07/03 14:03
# BU系统迭代v2.0.2.5交易

from common.request2buApi import request2buApi

# 创建单个资产
# service = "/app/createAssert"
# secdata = {"userMobile":"18716200007",
#            "behaviorId":"0002A001B002",
#            "orderNum":"ceshi00099",
#            # "money":"110000"
#            }

# 合作平台内商户的注册
# service = "/app/v1/merchants"
# secdata = {"userMobile":"18716200016", "userName":"eeeee"}

# BU转账
service = "/app/v1/generalTran"
secdata = {"fromUserMobile":"18716200006",
           "toUserMobile":"18716200014",
           "randomNum":"test_003",
           "tranBody":"aaaaaaaaa",
           "outTradeNo":"testoutTradeNo_003",
           "createIp":"192.168.1.31",
           "buAmount":"50",
           # "attachStr":"teststr_001",  # 非必传
           # "notifyUrl":"192.168.1.31",  # 非必传
           "startTime":"20180703170801"
           }

req = request2buApi(service, secdata).send()
print(req)