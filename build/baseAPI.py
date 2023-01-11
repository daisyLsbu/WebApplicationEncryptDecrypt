from flask import Flask, redirect, url_for, request
from cryptography.fernet import Fernet

app = Flask(__name__)

plainText = "hello geeks"
key = Fernet.generate_key()
fernet = Fernet(key) 

@app.route('/')
def defaultpath():
   return 'welcome to Home page' 

@app.route('/encryption/')
def encryption():
   return  'welcome to enc page' 

@app.route('/decryption/')
def decryption():
   return  "welcome to decrypyion"

@app.route('/encrypt')
def encrypt():
    msg = request.args.get('text')
    option = request.args.get('option')

    encMessage = fernet.encrypt(msg.encode())
    print("original string: ", msg)
    print("encrypted string: ", encMessage)

    return '''<h1>The text value is: {}</h1>
              <h1>The encrypted value is: {}</h1>
              <h1>The option value is: {}'''.format(msg, encMessage, option)

@app.route('/decrypt')
def decrypt():
    encMsg = request.args.get('text')
    option = request.args.get('option')
    txttoByte = encMsg.encode()

    dcrMessage = fernet.decrypt(txttoByte).decode()
    print("decrypted string: ", dcrMessage)

    return '''<h1>The text value is: {}</h1>
              <h1>The decrypted value is: {}</h1>
              <h1>The option value is: {}'''.format(encMsg, dcrMessage, option)

if __name__ == '__main__':
   app.run()