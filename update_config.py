import requests
import json
import base64
from datetime import datetime, timedelta

# 访问a.com获取json数据
response = requests.get('https://netvpn.cc/api/v1/guest/comm/config')
data = json.loads(response.text)

# 修改数据
data['data']['isEmailVerify'] = data['data'].pop('is_email_verify')
data['data']['isInviteForce'] = data['data'].pop('is_invite_force')
data['data']['emailWhitelistSuffix'] = data['data'].pop('email_whitelist_suffix')
data['data']['isRecaptcha'] = data['data'].pop('is_recaptcha')
data['data']['recaptchaSiteKey'] = data['data'].pop('recaptcha_site_key')
data['data']['appDescription'] = data['data'].pop('app_description')
data['data']['appUrl'] = data['data'].pop('app_url')
# 添加UPtime
#data['data']['uptime'] = (datetime.now() + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
# 移除加8个小时时间差
data['data']['uptime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# 将修改后的数据转换为json格式，并编码为base64
new_data = json.dumps(data).encode('utf-8')
# 推送 net1data 
net1data = json.dumps(data)
print(json.dumps(data))
print(new_data)
print(data)
print(json.loads(response.text))

# 将修改后的数据保存为 net1data.json 文件
with open('net1data', 'w') as f:
    json.dump(data, f)

"""
import requests
import json
import base64
from datetime import datetime, timedelta

def process_domain(domain):
    # 访问域名获取json数据
    response = requests.get(f'https://{domain}/api/v1/guest/comm/config')
    data = json.loads(response.text)

    # 修改数据
    data['data']['isEmailVerify'] = data['data'].pop('is_email_verify')
    data['data']['isInviteForce'] = data['data'].pop('is_invite_force')
    data['data']['emailWhitelistSuffix'] = data['data'].pop('email_whitelist_suffix')
    data['data']['isRecaptcha'] = data['data'].pop('is_recaptcha')
    data['data']['recaptchaSiteKey'] = data['data'].pop('recaptcha_site_key')
    data['data']['appDescription'] = data['data'].pop('app_description')
    data['data']['appUrl'] = data['data'].pop('app_url')
    # 添加UPtime
    #data['data']['uptime'] = (datetime.now() + timedelta(hours=8)).strftime('%Y-%m-%d %H:%M:%S')
    # 移除加8个小时时间差
    data['data']['uptime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    #自定义with open(f'{domain}_{filename}.json', 'w') as f:
    json.dump(data, f)
    
    # 将修改后的数据保存为文件
    with open(f'{domain}.json', 'w') as f:
        json.dump(data, f)
       
    # 返回数据
    return data
    
 process_domain('a.com')
process_domain('b.com')
process_domain('c.com')
#自定义 process_domain('a.com', '1')
"""

"""
# 新的
import requests
import json
from datetime import datetime

def process_domain(domain, filename):
    # 访问域名获取json数据
    response = requests.get(f'https://{domain}/api/v1/guest/comm/config')
    data = json.loads(response.text)

    # 修改数据
    data['data']['isEmailVerify'] = data['data'].pop('is_email_verify')
    data['data']['isInviteForce'] = data['data'].pop('is_invite_force')
    data['data']['emailWhitelistSuffix'] = data['data'].pop('email_whitelist_suffix')
    data['data']['isRecaptcha'] = data['data'].pop('is_recaptcha')
    data['data']['recaptchaSiteKey'] = data['data'].pop('recaptcha_site_key')
    data['data']['appDescription'] = data['data'].pop('app_description')
    data['data']['appUrl'] = data['data'].pop('app_url')

    # 添加UPtime
    data['data']['uptime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    # 将修改后的数据保存为文件
    with open(f'{domain}_{filename}.json', 'w') as f:
        json.dump(data, f)

    # 返回数据
    return data

# 保存第一个域名为 1.json
process_domain('a.com', '1')

# 保存第二个域名为 2.json
process_domain('b.com', '2')

# 保存第三个域名为 3.json
process_domain('c.com', '3')
"""
