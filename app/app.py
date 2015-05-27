from flask import Flask, render_template, request
import plivo
import urllib2
import BeautifulSoup
import nltk
import requests
 
app = Flask(__name__)
auth_id = "MAYJG5ZJJHYTQWYWFHYT"
auth_token = "MmQ4ZjA3MzM2NzgyMWQ0YjBkMzMzYzhkNWQ4M2Uz"
p = plivo.RestAPI(auth_id, auth_token)

# Params for sending an sms
# params = {
#     'src': '+919686798312', # Caller Id
#     'dst' : '+919945247441', # User Number to Call
#     'text' : "Hi, message from Plivo",
#     'type' : "sms",
# }

# Params for making a call
params = {
    'from': '+18552033185', # Caller Id
    'to' : '+919945247441', # User Number to Call
    'ring_url' : "http://a31b7b30.ngrok.io/inbound",
    'answer_url' : "http://a31b7b30.ngrok.io/inbound",
    'hangup_url' : "http://a31b7b30.ngrok.io/inbound",
}
@app.route('/')
def ReturnForm():
  return app.send_static_file('form.html')
 
@app.route('/', methods=['POST'])
def FormPost():
  params['to'] = request.form['Number']
  url = request.form['Url']
  cnt = 0
  page = urllib2.urlopen(url)
  page_content = page.read()
  page_contbyte = bytearray(page_content)
  page_content = page_contbyte.decode("ISO-8859-1")
  page_content = page_content.upper()
  a = 0
  pos = page_content.find("PLIVO")  
  while pos != -1:
    cnt = cnt + 1
    a = a + pos + 1
    pos = page_content[a:].find("PLIVO")
  if cnt == 0 :
  	params['ring_url'] = "http://a31b7b30.ngrok.io/inbound?msg_text=No Plivo"
  elif cnt >= 1 and cnt <= 100 :
  	params['ring_url'] = "http://a31b7b30.ngrok.io/inbound?msg_text=Yes Plivo"
  elif cnt>100:
  	params['ring_url'] = "http://a31b7b30.ngrok.io/inbound?msg_text=Many Plivo"
  else :
    params['ring_url'] = "http://a31b7b30.ngrok.io/inbound?msg_text=Error"

  message = p.make_call(params)
  return app.send_static_file('success.html')
 
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5002)