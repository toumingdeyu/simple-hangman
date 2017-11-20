import web
import random
from hangman import word

# edit here for personalized word dictionary
dicPath = '/usr/share/dict/words'
wordDic = []
with open(dicPath, 'r') as dicFile:
    wordDic = list(dicFile)
# filter words needed
wordDic = [w[:-1] for w in wordDic if len(w) > 5 and len(w) < 10]

urls = ('/game', 'Game', '/', 'Index')

app = web.application(urls, globals())

# check if session exists, otherwise create one
if web.config.get('_session') is None:
    store = web.session.DiskStore('sessions')
    session = web.session.Session(app, store,
                                  initializer={'word': None})
    web.config._session = session
else:
    session = web.config._session


render = web.template.render('templates/', base="layout")

session.record = [0, 0]

def updateRecord(word):
    if word.remains == 0:
        session.record[0] += 1
    elif word.life == 0:
        session.record[1] += 1




class Index(object):
    def GET(self):
        session.word = word.Word(wordDic[random.randint(0,len(wordDic)-1)])
        web.seeother("/game")

class Game(object):
    def GET(self):
        if not session.word:
            session.word = word.Word(wordDic[random.randint(0,len(wordDic)-1)])
        return render.show_word(word=session.word, record=session.record)
    def POST(self):
        form = web.input(action=None)
        if session.word and form.action:
            session.word = session.word.reveal(form.action)
            updateRecord(session.word)
            web.seeother("/game")
        else:
            web.seeother("/game")




if __name__ == "__main__":
    app.run()
