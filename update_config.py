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
new_data_b64 = base64.b64encode(new_data).decode('utf-8')

# 使用GitHub API推送更改后的内容到仓库中
g = Github('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')
repo = g.get_repo('netVPN1')
contents = repo.get_contents('/api/v1/passport/comm/config')
message = 'Update config'
branch = 'main'
commiter = {'name': 'yangyucacaa', 'email': '1462749078@qq.com'}
now = datetime.utcnow() + timedelta(hours=8)
timestamp = now.strftime('%Y-%m-%d %H:%M:%S')
content = contents.decoded_content.decode('utf-8')
if content != new_data_b64:
    repo.update_file(contents.path, message, new_data_b64, contents.sha, branch=branch, committer=commiter, author=commiter)
    print(f'[{timestamp}] Config updated')
else:
    print(f'[{timestamp}] Config not changed')
