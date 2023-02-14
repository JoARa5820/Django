# 클라이언트로 정보를 전송하기 위한 역할을 하는 함수 : def index()
# request(=파라미터) : 파라미터의 인자로 요청과 관련된 여러가지 정보가 들어오도록 약속되어있는 객체를 전달해주도록 되어있음 / 파라미터 이름은 아무거나 상관없지만, 관습적으로 request를 사용함
# 우리가 처리한 결과를 client로 보내줄 때 return값으로 보내주는데, Http를 이용해서 응답하겠다는 의미에서 HttpResponse라는 객체를 이용함 / 이 객체를 이용하기 위해서는 import 해줘야함

from django.shortcuts import render, HttpResponse, redirect
import random
from django.views.decorators.csrf import csrf_exempt

nextId = 4
topics = [
            {'id':1, 'title':'routing', 'body':'Routing is ..'},
            {'id':2, 'title':'view', 'body':'View is ..'},
            {'id':3, 'title':'model', 'body':'Model is ..'},
]

def HTMLTemplate(articleTag, id=None):
    global topics
    contextUI = ''
    if id != None:
        contextUI = f'''
          <li>
            <form action="/delete/" method="post">
                <input type="hidden" name="id" value={id}>
                <input type="submit" value="delete">
            </form>
          </li>
        '''
    ol = ''
    for topic in topics:
        ol += f'<li><a href="/read/{topic["id"]}">{topic["title"]}</a></li>'
    return f'''
    <html>
    <body>
        <h1><a href="/">Django</a></h1>
        <ul>
            {ol}
        </ul>
        {articleTag}
        <ul>
          <li><a href="/create/">create</a></li>
          {contextUI}
        </ul>
    </body>
    </html>
    '''


def index(request):
    article = '''
    <h2>Welcome</h2>
    Hello, Django
    '''
    return HttpResponse(HTMLTemplate(article))


def read(request, id):
    global topics
    article = ''
    for topic in topics:
        if topic['id'] == int(id):
            article = f'<h2>{topic["title"]}</h2>{topic["body"]}'
    return HttpResponse(HTMLTemplate(article, id))


@csrf_exempt
def create(request):
    global nextId
    if request.method == 'GET':
        article = '''
        <form action="/create/" method="post">
            <p><input type="text" name="title" placeholder="title"></p>
            <p><textarea name="body" placeholder="body"></textarea></p>
            <p><input type="submit"></p>
        </form>
        '''
        return HttpResponse(HTMLTemplate(article))
    elif request.method == 'POST':
        title = request.POST['title']
        body = request.POST['body']
        newTopic = {"id":nextId, "title":title, "body":body}
        topics.append(newTopic)
        url = '/read/' + str(nextId)
        nextId = nextId + 1
        return redirect(url)


@csrf_exempt
def delete(request):
    global topics
    if request.method == 'POST':
        id = request.POST['id']
        newTopics = []
        for topic in topics:
            if topic['id'] != int(id):
                newTopics.append(topic)
        topics = newTopics
        return redirect('/')

