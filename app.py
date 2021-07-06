
from flask import Flask, render_template, request, url_for
from helpers import sanitise_input, sanitise_number_input
app = Flask(__name__)

@app.route('/')
def func():
    return render_template('index.html')

#encyption page
@app.route('/', methods=['GET', 'POST'])
def encrypt():
    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == 'POST':
        message = sanitise_input(request.form["message"])
        key = sanitise_number_input(request.form['key'])
        encryptedmessage = encrypt_caesar(message, key)
        return render_template('index.html', encrypted_message=encryptedmessage)


def encrypt_caesar(message, key):
    result = ""
    for i in range(len(message)):
      char = message[i]
       
      if (char.isupper()):
         result += chr((ord(char) + key-65) % 26 + 65)
      else:
         result += chr((ord(char) + key - 97) % 26 + 97)
    return result
    
if __name__== '__main__':
    app.run(debug=True)