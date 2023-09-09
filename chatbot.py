from flask import Flask, render_template,request
from nltk.chat.util import Chat,reflections
que1 = r'how are you (.*)'
answ1= [
        ' all well',
        'I am good',
         'awsome'
        ]
que2 = r'what can you do'
answ2= [
        'I can reply your queries',
        'I am here to chat with you',
        ] 
que3 = r'(.*) your name'
answ3= [
        'My name is Chatty',
        'I am chatty'
        ]
que4 = r'(.*)mausam (.*)baarish'
answ4= [
        'baarish ka mausam hai',
        'It will look rain today',
        'Baarish ho skti hai mausam kharab hai'
        ]        
qa_pair = [(que1,answ1),
           (que2,answ2),
           (que3,answ3),
           (que4,answ4),
          ]
chatbot = Chat(qa_pair)

app = Flask(__name__)

@app.route('/')
def home():
    global chatbot
    query = request.args.get('query') 
    if query!=None:
        response = chatbot.respond(query)
    else:
        response = 'Sorry I am not sure'
    return render_template('index.html',result=response)
@app.route('/chatbot')
def chat():
    return "<h2> Chat Bot</h2>"

app.run(debug = True)


