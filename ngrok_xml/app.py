from flask import Flask, request, redirect, Response
import plivo
import os

app = Flask(__name__)

@app.route("/inbound",methods=['GET','POST'])
def hello():
    temp = request.args['msg_text']
    xml_text='<Response><Speak>'+temp+'</Speak></Response>'
    return Response(xml_text, mimetype='text/xml')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)