import json
import urllib

class OAuth_GITHUB(object):
	def __init__(self,client_id,client_key,redirect_url):
		self.client_id = client_id
		self.client_key = client_key
		self.redirect_url = redirect_url
	
	def _get(self,url,data):
		request_url = '%s?%s' % (url,urllib.parse.urlencode(data))
		response = urllib.request.urlopen(request_url)
		return response.read()
		
	def _post(self,url,data):
		request = urllib.request.Request(url,data = urllib.parse.urlencode(data).encode(encoding='UTF8'))     #1
		response = urllib.request.urlopen(request)
		return response.read()
	
	def get_auth_url(self):
		params = {
			'client_id':self.client_id,
			'response_type':'code',
			'redirect_url':self.redirect_url,
			'scope':'user:email',
			'state':1
		}
		url = 'https://github.com/login/oauth/authorize?%s' % urllib.parse.urlencode(params)
		return url

	def get_access_token(self,code):
		params = {
			'grant_type':'authorization_code',
			'client_id':self.client_id,
			'client_secret':self.client_key,
			'code':code,
			'redirect_url':self.redirect_url
		}
		response = self._post('https://github.com/login/oauth/access_token',params)
		result = urllib.parse.parse_qs(response,True)
		self.access_token = result[b'access_token'][0]    #1
		return self.access_token
	
	def get_user_info(self):
		params ={'access_token':self.access_token}
		response = self._get('https://api.github.com/user',params)
		result = json.loads(response.decode('utf-8'))    #1
		self.openid = result.get('id','')
		return result
		
	def get_email(self):
		params ={'access_token':self.access_token}
		response = self._get('https://api.github.com/user/emails',params)
		result = json.loads(response.decode('utf-8'))
		return result[0]['email']
		
		