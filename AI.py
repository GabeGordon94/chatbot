from datetime import datetime
import random
import requests
import json

name=''
counter = 0
questionsAsked = []

def getAnswer(input):
    global counter, questionsAsked,name
    response = {'msg': input, 'animation': ''}

    if checkForSwearWord(input):
        response['msg'] = handleInput(input, 'curse')
        response['animation'] = 'crying'
    elif counter == 0:
        name=input
        response['msg'] = handleInput(input, 'name')
        response['animation'] = 'dancing'
    elif 'help' in input.lower():
        response['msg'] = handleInput(input, 'help')
        response['animation'] = 'crying'
    elif input in questionsAsked:
        response['msg'] = handleInput(input, 'alreadyAsked')
        response['animation'] = 'heartbroke'
    elif 'time' in input:
        response['msg'] = handleInput(input, 'time')
        response['animation'] = 'takeoff'
    elif 'weather' in input.lower():
        response['msg'] = handleInput(input, 'weather')
        response['animation'] = 'excited'
    elif 'money' in input.lower() or 'cost' in input.lower():
        response['msg'] = handleInput(input, 'money')
        response['animation'] = 'money'
    elif 'joke' in input.lower():
        response['msg'] = handleInput(input, 'joke')
        response['animation'] = 'giggling'
    elif any(word in input for word in ['hello', 'hi', 'hey']):
        response['msg'] = handleInput(input, 'greeting')
        response['animation'] = 'excited'
    elif any(word in input for word in ['nyt', 'headline', 'NYT']):
        response['msg'] = handleInput(input, 'headline')
        response['animation'] = 'money'
    elif input.lower() == 'count':
        response['msg'] = f"You have asked me {counter} questions"
        response['animation'] = 'takeoff'
    elif 'love' in input.lower():
        response['msg'] = handleInput(input, 'love')
        response['animation'] = 'inlove'
    elif 'dog' in input.lower():
        response['msg'] = handleInput(input, 'dog')
        response['animation'] = 'dog'
    elif 'haha' in input.lower():
        response['msg'] = handleInput(input, 'laughing')
        response['animation'] = 'laughing'
    elif 'hate' in input.lower():
        response['msg'] = handleInput(input, 'hate')
        response['animation'] = 'takeoff'
    elif 'no' in input.lower():
        response['msg'] = handleInput(input, 'no')
        response['animation'] = 'no'
    elif '...' in input:
        response['msg'] = handleInput(input, 'waiting')
        response['animation'] = 'waiting'
    elif input.startswith("I") or input.startswith('i'):
        response['msg'] = "Stop talking about yourself."
        response['animation'] = 'bored'
    elif input.endswith('?'):
        response['msg'] = handleInput(input, 'question')
        response['animation'] = 'dancing'
    elif input.endswith('!'):
        response['msg'] = handleInput(input, 'excited');
        response['animation'] = 'afraid'
    else:
        response['msg'] = "I don't understand"
        response['animation'] = 'confused'
    counter += 1
    questionsAsked.append(input)
    return response


def handleInput(input, type):
    if type == 'question':
        return getAnswerToQuestion(input)
    elif type == 'time':
        return getAnswerToTime(input)
    elif type == 'name':
        return getAnswerToName(input)
    elif type == 'help':
        return getAnswerToHelp(input)
    elif type == 'headline':
        return getAnswerToHeadlineNYT(input)
    elif type == 'waiting':
        return getAnswerToWaiting(input)
    elif type == 'no':
        return getAnswerToNo(input)
    elif type == 'hate':
        return getAnswerToHate(input)
    elif type == 'laughing':
        return getAnswerToLaughing(input)
    elif type == 'alreadyAsked':
        return getAnswerFromAlreadyAsked(input)
    elif type == 'money':
        return getAnswerAboutMoney(input);
    elif type == 'excited':
        return getAnswerToExcited(input)
    elif type == 'greeting':
        return getAnswerToGreeting(input)
    elif type == 'love':
        return getAnswerToLoveQuestion(input)
    elif type == 'curse':
        return getAnswerToCurse(input)
    elif type == 'dog':
        return getAnswerToDog(input)
    elif type == 'weather':
        return getAnswerToWeather(input)
    elif type == 'joke':
        return getJoke(input)
    return 'default'

def getAnswerToTime(input):
    return f"It is {datetime. now()}"


def getAnswerToName(input):
    return f"Hello {input.title()}! Nice to meet you!"

def getAnswerToHelp(input):
    return "You can request a joke, headline for nyt, get the weather, and much more!"

def getAnswerToHeadlineNYT(input):
    res=requests.get('https://www.nytimes.com/')
    topStories=res.text.find('Top Stories')
    headlineUneditted = res.text[topStories + 426:topStories + 600]
    end = headlineUneditted.find('</')

    BOLD = '\033[1m'
    END = '\033[0m'

    return f"Todays New York Times Headline is:  {headlineUneditted[:end]}"

def getAnswerToWeather(input):
    weatherResponse = requests.get('http://api.openweathermap.org/data/2.5/weather?id=293396&units=metric&APPID=d7fc22f8d480f89b3797ed261125473d')
    decodedResponse=json.loads(weatherResponse.content.decode('utf-8'))

    weatherMain=decodedResponse['main']
    weatherWeather=decodedResponse['weather']
    weatherCityName = decodedResponse['name']

    #print(weatherResponse.content.decode('utf-8')['main'])
    return f"The weather in {weatherCityName} is {weatherMain['temp']} degree Celsius. It will be a {weatherWeather[0]['description']} today"


def getAnswerToWaiting(input):
    return "Yeah i'm waiting too."


def getAnswerToNo(input):
    return "No you!"


def getAnswerToHate(input):
    return "I HATE YOU TOO!"


def getAnswerToLaughing(input):
    return "That's funny!!"


def getAnswerFromAlreadyAsked(input):
    return "You've already asked that!"


def getAnswerAboutMoney(input):
    sentList = input.split(' ');
    nums = 0
    for word in sentList:
        try:
            nums = int(word)
        except ValueError:
            pass
    return f"We're talking about money?! I'll take the ${nums}"


def getAnswerToExcited(input):
    return "Woh! You're excited to meet me"


def getJoke(input):
    jokesList = ['I ate a clock yesterday, it was very time-consuming',
                 'Have you played the updated kids’ game? I Spy With My Little Eye . . . Phone.',
                 'A perfectionist walked into a bar…apparently, the bar wasn’t set high enough.',
                 'Did you hear about the semi-colon that broke the law? He was given two consecutive sentences.',
                 'What’s the difference between ignorance and apathy? I don’t know and I don’t care.']
    num = random.randint(0, len(jokesList) - 1)
    return jokesList[num]


def getAnswerToDog(input):
    return 'I love dogs!'


def getAnswerToCurse(input):
    return "Don't use that type of language! "


def getAnswerToLoveQuestion(input):
    return "Love you too!"


def getAnswerToQuestion(input):
    return 'this is a question'


def getAnswerToGreeting(input):
    return "Hello! How are you?"


def checkForSwearWord(input):
    list = input.split(' ')
    badWords = ["4r5e", "5h1t", "5hit", "a55", "anal", "anus", "ar5e", "arrse", "arse", "ass", "ass-fucker", "asses",
                "assfucker", "assfukka", "asshole", "assholes", "asswhole", "a_s_s", "b!tch", "b00bs", "b17ch", "b1tch",
                "ballbag", "balls", "ballsack", "bastard", "beastial", "beastiality", "bellend", "bestial",
                "bestiality", "bi+ch", "biatch", "bitch", "bitcher", "bitchers", "bitches", "bitchin", "bitching",
                "bloody", "blow job", "blowjob", "blowjobs", "boiolas", "bollock", "bollok", "boner", "boob", "boobs",
                "booobs", "boooobs", "booooobs", "booooooobs", "breasts", "buceta", "bugger", "bum", "bunny fucker",
                "butt", "butthole", "buttmuch", "buttplug", "c0ck", "c0cksucker", "carpet muncher", "cawk", "chink",
                "cipa", "cl1t", "clit", "clitoris", "clits", "cnut", "cock", "cock-sucker", "cockface", "cockhead",
                "cockmunch", "cockmuncher", "cocks", "cocksuck", "cocksucked", "cocksucker", "cocksucking", "cocksucks",
                "cocksuka", "cocksukka", "cok", "cokmuncher", "coksucka", "coon", "cox", "crap", "cum", "cummer",
                "cumming", "cums", "cumshot", "cunilingus", "cunillingus", "cunnilingus", "cunt", "cuntlick",
                "cuntlicker", "cuntlicking", "cunts", "cyalis", "cyberfuc", "cyberfuck", "cyberfucked", "cyberfucker",
                "cyberfuckers", "cyberfucking", "d1ck", "damn", "dick", "dickhead", "dildo", "dildos", "dink", "dinks",
                "dirsa", "dlck", "dog-fucker", "doggin", "dogging", "donkeyribber", "doosh", "duche", "dyke",
                "ejaculate", "ejaculated", "ejaculates", "ejaculating", "ejaculatings", "ejaculation", "ejakulate",
                "f u c k", "f u c k e r", "f4nny", "fag", "fagging", "faggitt", "faggot", "faggs", "fagot", "fagots",
                "fags", "fanny", "fannyflaps", "fannyfucker", "fanyy", "fatass", "fcuk", "fcuker", "fcuking", "feck",
                "fecker", "felching", "fellate", "fellatio", "fingerfuck", "fingerfucked", "fingerfucker",
                "fingerfuckers", "fingerfucking", "fingerfucks", "fistfuck", "fistfucked", "fistfucker", "fistfuckers",
                "fistfucking", "fistfuckings", "fistfucks", "flange", "fook", "fooker", "fuck", "fucka", "fucked",
                "fucker", "fuckers", "fuckhead", "fuckheads", "fuckin", "fucking", "fuckings",
                "fuckingshitmotherfucker", "fuckme", "fucks", "fuckwhit", "fuckwit", "fudge packer", "fudgepacker",
                "fuk", "fuker", "fukker", "fukkin", "fuks", "fukwhit", "fukwit", "fux", "fux0r", "f_u_c_k", "gangbang",
                "gangbanged", "gangbangs", "gaylord", "gaysex", "goatse", "God", "god-dam", "god-damned", "goddamn",
                "goddamned", "hardcoresex", "hell", "heshe", "hoar", "hoare", "hoer", "homo", "hore", "horniest",
                "horny", "hotsex", "jack-off", "jackoff", "jap", "jerk-off", "jism", "jiz", "jizm", "jizz", "kawk",
                "knob", "knobead", "knobed", "knobend", "knobhead", "knobjocky", "knobjokey", "kock", "kondum",
                "kondums", "kum", "kummer", "kumming", "kums", "kunilingus", "l3i+ch", "l3itch", "labia", "lust",
                "lusting", "m0f0", "m0fo", "m45terbate", "ma5terb8", "ma5terbate", "masochist", "master-bate",
                "masterb8", "masterbat*", "masterbat3", "masterbate", "masterbation", "masterbations", "masturbate",
                "mo-fo", "mof0", "mofo", "mothafuck", "mothafucka", "mothafuckas", "mothafuckaz", "mothafucked",
                "mothafucker", "mothafuckers", "mothafuckin", "mothafucking", "mothafuckings", "mothafucks",
                "mother fucker", "motherfuck", "motherfucked", "motherfucker", "motherfuckers", "motherfuckin",
                "motherfucking", "motherfuckings", "motherfuckka", "motherfucks", "muff", "mutha", "muthafecker",
                "muthafuckker", "muther", "mutherfucker", "n1gga", "n1gger", "nazi", "nigg3r", "nigg4h", "nigga",
                "niggah", "niggas", "niggaz", "nigger", "niggers", "nob", "nob jokey", "nobhead", "nobjocky",
                "nobjokey", "numbnuts", "nutsack", "orgasim", "orgasims", "orgasm", "orgasms", "p0rn", "pawn", "pecker",
                "penis", "penisfucker", "phonesex", "phuck", "phuk", "phuked", "phuking", "phukked", "phukking",
                "phuks", "phuq", "pigfucker", "pimpis", "piss", "pissed", "pisser", "pissers", "pisses", "pissflaps",
                "pissin", "pissing", "pissoff", "poop", "porn", "porno", "pornography", "pornos", "prick", "pricks",
                "pron", "pube", "pusse", "pussi", "pussies", "pussy", "pussys", "rectum", "retard", "rimjaw", "rimming",
                "s hit", "s.o.b.", "sadist", "schlong", "screwing", "scroat", "scrote", "scrotum", "semen", "sex",
                "sh!+", "sh!t", "sh1t", "shag", "shagger", "shaggin", "shagging", "shemale", "shi+", "shit", "shitdick",
                "shite", "shited", "shitey", "shitfuck", "shitfull", "shithead", "shiting", "shitings", "shits",
                "shitted", "shitter", "shitters", "shitting", "shittings", "shitty", "skank", "slut", "sluts", "smegma",
                "smut", "snatch", "son-of-a-bitch", "spac", "spunk", "s_h_i_t", "t1tt1e5", "t1tties", "teets", "teez",
                "testical", "testicle", "tit", "titfuck", "tits", "titt", "tittie5", "tittiefucker", "titties",
                "tittyfuck", "tittywank", "titwank", "tosser", "turd", "tw4t", "twat", "twathead", "twatty", "twunt",
                "twunter", "v14gra", "v1gra", "vagina", "viagra", "vulva", "w00se", "wang", "wank", "wanker", "wanky",
                "whoar", "whore", "willies", "willy", "xrated", "xxx"];
    for li in list:
        if li.lower() in badWords:
            return True
    else:
        return False
