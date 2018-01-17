import json
import urllib

class OAuth_Base(object):
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
		pass

	def get_access_token(self,code):
		pass
		
	def get_open_id(self):
		pass
	
	def get_user_info(self):
		pass
		
	def get_email(self):
		pass

class OAuth_GITHUB(OAuth_Base):
	def get_auth_url(self):
		params = {
			'client_id':self.client_id,
			'response_type':'code',
			'redirect_uri':self.redirect_url,
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
		
class OAuth_QQ(OAuth_Base):
	def get_auth_url(self):
		params = {
			'client_id':self.client_id,
			'response_type':'code',
			'redirect_url':self.redirect_url,
			'scope':'get_user_info',
			'state':1
		}
		url = 'https://graph.qq.com/oauth2.0/authorize?%s' % urllib.parse.urlencode(params)
		return url

	def get_access_token(self,code):
		params = {
			'grant_type':'authorization_code',
			'client_id':self.client_id,
			'client_secret':self.client_key,
			'code':code,
			'redirect_uri':self.redirect_url
		}
		response = self._get('https://graph.qq.com/oauth2.0/token',params)
		result = urllib.parse.parse_qs(response,True)
		self.access_token = result[b'access_token'][0]    #1
		return self.access_token
		
	def get_open_id(self):
		params ={'access_token':self.access_token}
		response = self._get('https://graph.qq.com/oauth2.0/me',params)
		result = json.loads(response.decode('utf-8'))    #1
		self.openid = result.get('openid','')
		return self.openid
	
	def get_user_info(self):
		params ={
			'access_token':self.access_token,
			'openid':self.openid,	
			'oauth_consumer_key':self.client_id,
		}
		response = self._get('https://graph.qq.com/user/get_user_info',params)
		result = json.loads(response.decode('utf-8'))    #1
		return result

class OAuth_WEIBO(OAuth_Base):
	def get_auth_url(self):
		params = {
			'client_id':self.client_id,
			'response_type':'code',
			'redirect_uri':self.redirect_url,
			'scope':'email',
			'state':1
		}
		url = 'https://api.weibo.com/oauth2/authorize?%s' % urllib.parse.urlencode(params)
		return url
		
	def get_access_token(self,code):
		params = {
			'grant_type':'authorization_code',
			'client_id':self.client_id,
			'client_secret':self.client_key,
			'code':code,
			'redirect_uri':self.redirect_url
		}
		response = self._post('https://api.weibo.com/oauth2/access_token',params)
		result = json.loads(response.decode('utf-8'))
		self.access_token = result["access_token"]
		self.openid = result["uid"]
		return self.access_token
	
	def get_open_id(self):
		return self.openid

	def get_user_info(self):
		params ={
			'access_token':self.access_token,
			'uid':self.openid,	
		}
		response = self._get('https://api.weibo.com/2/users/show.json',params)
		result = json.loads(response.decode('utf-8'))    #1
		return result
		
	def get_email(self):
		params ={'access_token':self.access_token}
		response = self._get('https://api.weibo.com/2/account/profile/email.json',params)
		result = json.loads(response.decode('utf-8'))
		return result[0]['email']


		
		