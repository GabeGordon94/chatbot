"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json


def getAnswer(input):
    if input.endswith('?'):
        return handleInput(input,'question')
    elif input in ['hello','hi','hey'] :
        return handleInput(input,'greeting')
    elif input.endswith('!'):
        return "Woh! You're excited to meet me"
    return 'default'

def handleInput(input,type):
    if type=='question':
        return getAnswerToQuestion(input)
    elif type == 'greeting':
        return getAnswerToGreeting(input)
    return 'default'

def getAnswerToQuestion(input):
    return 'this is a question'

def getAnswerToGreeting(input):
    return "Hello! How are you?"


@route('/', method='GET')
def index():
    return template("chatbot.html")

@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return ({"animation": "inlove", "msg":getAnswer(user_message)})

@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})


@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')


@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()

