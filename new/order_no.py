# from configs.config import HOST
import requests
import re
import jieba
import datetime

class orderNo:
     def orderNo(selef):
           url =f'{HOST}'
           payload ='inData'  #参数
           resp = requests.post(url,json=payload)   #请求
           return resp.json()
# if __name__ == '__main__':
#     res=orderNo().orderNo()"":"")
#     print(res)








