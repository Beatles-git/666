import requests
# 注册数据
reg_url='http://120.78.128.25:8766/futureloan/member/register'
reg_data={
  "mobile_phone": "15810941763",
  "pwd": "lemon123456",
  "type":"0",
  "reg_name":"管理员用户lemon"
}

# 登录数据
log_url='http://120.78.128.25:8766/futureloan/member/login'
log_data={
  "mobile_phone": "15810941763",
  "pwd": "lemon123456"}
# 充值数据
rec_url='http://120.78.128.25:8766/futureloan/member/recharge'
rec_data={
  "member_id": "2077895",
  "amount": "100.00"
}
header={'X-Lemonban-Media-Type':'lemonban.v2','Authorization':None}




def http_request(url,data,header,method='post'):
    if method=='get':
        response=requests.get(url=url,json=data,headers=header)
    else:
        response = requests.post(url=url, json=data,headers=header)
        return response.json()
if __name__ == '__main__':

    result=http_request(rec_url,rec_data,header)
    print(result)