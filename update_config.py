import requests
import json
import base64
from datetime import datetime, timedelta
from github import Github

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

# 将修改后的数据转换为json格式，并编码为base64
new_data = json.dumps(data).encode('utf-8')

print(new_data)
print(data)


