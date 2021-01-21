from django.shortcuts import render
from .models import Member
# 비밀번호 암호화
from django.contrib.auth.hashers import make_password

def insert(request):
    if request.method == 'GET':
        return render(request, 'insert.html') #127.0.0.1:8000/member/insert --get 방식
    elif request.method == 'POST':
        username = request.POST['username']
        pw = request.POST['pw']
        pw1 = request.POST['pw1']
        email = request.POST['email']
        hp = request.POST['hp']
        msg = {}

        if not (username and pw and pw1 and hp):
            msg['err'] = '필수 입력 값을 채우세요'
        elif pw != pw1:
            msg['err'] = '비밀번호를 확인하세요!'
        else:
            m = Member(username=username, pw=make_password(pw), email=email, hp=hp)
            m.save()
        return render(request, 'insert.html', msg)
