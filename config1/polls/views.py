from .models import Question
from django.shortcuts import render
from django.shortcuts import get_object_or_404

def index(request):
    qlist = Question.objects.all()
    return render(request, 'polls/index.html', {'qlist' : qlist})
    # return render(request, 'polls/index.html') 
    # render(요청, 반환할 페이지[, 딕셔너리])

def detail(request, qid):
    # q = Question.objects.get(id=qid)
    # select * from question where id=qid
    q = get_object_or_404(Question, id=qid)
    c = q.choice_set.all()
    print(len(c))
    msg = {}
    msg['q']=q
    if len(c) < 1:
        msg['err'] = '선택할 항목이 없습니다'
    return render(request, 'polls/detail.html', msg)

def vote(request, qid):
    q = Question.objects.get(id=qid)
    # q = get_object_or_404(Question, id=qid)
    cid = request.POST['choice']
    c = q.choice_set.get(id=cid)
    c.votes = c.votes+1
    c.save()
    return render(request, 'polls/result.html', {'q': q})
    # Question과 Choice는 1:N 관계, 외래키로 연결된 경우 모델소문자_set 속성이 제공됨

def dbtest(request):
    # 1) 삽입, 수정 save()
    # q = Question(question_text='좋아하는 운동은', pub_date='2021-01-07')
    # q.save()
    # q = Question(id=1, question_text='싫어하는 색은', pub_date='2021-01-07')
    # q.save()
    # return render(request, 'polls/dbtest.html')
    # 2) 조회
    # qlist= Question.objects.all() # 모든 데이터
    # qlist=Question.objects.get(id=3) # 조건에 맞는 데이터
    # print(qlist)

    # return render(request, 'polls/dbtest.html') 
    # return render(request, 'polls/dbtest.html', {'aa':'bb'}) # 127.0.0.1:8000/polls/dbtest
    # qlist= Question.objects.all() # 모든 데이터
    # return render(request, 'polls/dbtest.html', {'qlist': qlist})

    # 3) 삭제 delete()
    q = Question.objects.get(id=1)
    q.delete()

    return render(request, 'polls/dbtest.html')
