from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

from ..models import Question

def index(request):
    """
    pybo 목록 출력
    """
    # 입력 인자
    page = request.GET.get('page', '1') #페이지
    kw = request.GET.get('kw', '')

    # 조회
    question_list = Question.objects.order_by('-create_date') # '-' 기호는 작성일시의 역순을 의미한다.
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw) |                # 제목 검색
            Q(content__icontains=kw) |                # 내용 검색
            Q(author__username__icontains = kw) |      # 질문 글쓴이 검색
            Q(answer__author__username__icontains=kw) # 답변 글쓴이 검색
        ).distinct()

    # 페이징 처리
    paginator = Paginator(question_list, 10) # 페이지 당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context = {'question_list' : page_obj, 'page': page, 'kw': kw} #page와 kw가 추가가
    return render(request, 'pybo/question_list.html', context)
    #render함수는 context에 있는 question 모델 데이터 question_list를 pybo/question_list.html 파일에 적용하여
    #HTML 코드로 변환한다.


    #return HttpResponse("안녕하세요 pybo에 오신 것을 환엽합니다.")

def detail(request, question_id):
    """
    pybo 내용 출력
    """
    #question = Question.objects.get(id = question_id)
    question = get_object_or_404(Question, pk = question_id)
    context = {'question' : question}
    return render(request, 'pybo/question_detail.html', context)
