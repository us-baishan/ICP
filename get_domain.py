

import json, urllib
from urllib.parse import urlencode
import urllib.request




def main():
    # 配置您申请的APPKey


    appkey = "fc3ad5f0b00941079f056ceb07f6d749"
    # 1.备案查询
    request1(appkey, "GET")


# 备案查询
def request1(appkey, m="GET" ):
    domain_j = str(input("请输入需要查询的域名："))
    url = "http://apidata.chinaz.com/CallAPI/Domain"
    params = {
        "key": appkey,  # 应用APPKEY(应用详细页查询)

        'domainName' : domain_j

    }

    params = urlencode(params)
    if m == "GET":
        f = urllib.request.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.request.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    # print(res)
    aa=res['Result']
    if aa == None:
        print('None')

    else:
        print(aa['SiteLicense'])
    a = 'http://icp.chinaz.com/' + domain_j



    print('link:' + a)

    # for pages in res:
    #         page = eval(pages)
    #
    #
    #         if page["success"] == "0":
    #                 print("=========================================")
    #                 print("网站域名：", domain_j)
    #                 print("备案状态:", "数据出错 或 未备案!")
    #                 print("=========================================\n")
    #                 # page=page.decode("utf8")
    #         else:
    #                 # for pagea in page["result"]:
    #                 # print (pagea+'\t\t'+page["result"][pagea])
    #                 print("=========================================")
    #                 print("网站域名：", page["result"]["domain"])
    #                 print("备案状态：", "已备案")
    #                 print("网站备案：", page["result"]["icpno"])
    #                 print("首页地址：", page["result"]["webhome"])
    #                 print("主办单位：", page["result"]["organizers"])
    #                 print("单位性质：", page["result"]["organizers_type"])
    #                 print("审核时间：", page["result"]["exadate"])
    #                 print("=========================================\n")
    # if res:
    #     error_code = res["error_code"]
    #     if error_code == 0:
    #         # 成功请求
    #         print
    #         res["result"]
    #     else:
    #         print
    #         "%s:%s" % (res["error_code"], res["reason"])
    # else:
    #     print
    #     "request api error"


if __name__ == '__main__':
    main()



