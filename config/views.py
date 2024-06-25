from django.shortcuts import render
from burgers.models import Burger
# 브라우저에서 텍스트를 보여주고 싶으면 htttp response를 사용해야함
# 브라우저가 읽을 수 있도록 함
def main(request):
    return render(request,"main.html")

def burger_list(request):
    burgers = Burger.objects.all()
    print("전체 햄버거 목록:",burgers)
    
    #Template으로 전달해줄 dict 객체
    context = {
        "burgers":burgers,
    }

    return render(request,"burger_list.html", context) 

def burger_search(request):
    keyword = request.GET.get("keyword")
    if keyword is not None:
        burgers = Burger.objects.filter(name__contains=keyword)
    # print(keyword)
    # burgers = Burger.objects.filter(name__contains=keyword)
    else:
        burgers = Burger.objects.none()
    # print(burgers)
    context = {
        "burgers":burgers,
    }

    return render(request,"burger_search.html",context)



# 첫번째 인수는 View 함수에 장동으로 전달되는 request 객체를 지정해야함
# 두번째는 Template의 경로를 지정
# 경로는 setting.py에 지정한 TEMPLATES 설정의 DIR에 추가한 경로를 기준

