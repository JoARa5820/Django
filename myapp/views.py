# 클라이언트로 정보를 전송하기 위한 역할을 하는 함수 : def index()
# request(=파라미터) : 파라미터의 인자로 요청과 관련된 여러가지 정보가 들어오도록 약속되어있는 객체를 전달해주도록 되어있음 / 파라미터 이름은 아무거나 상관없지만, 관습적으로 request를 사용함
# 우리가 처리한 결과를 client로 보내줄 때 return값으로 보내주는데, Http를 이용해서 응답하겠다는 의미에서 HttpResponse라는 객체를 이용함 / 이 객체를 이용하기 위해서는 import 해줘야함

from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('Welcome!')

def create(request):
    return HttpResponse('Create')

def read(request, id):
    return HttpResponse('Read!' + id)















