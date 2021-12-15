from django.core.checks import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from youtuber.models import MyYoutuber
from django.urls import reverse
from allauth.account.views import PasswordChangeView
from .models import User
from django.contrib import messages
# from django.contrib.auth.models import User
# from django.contrib import auth

@login_required
def my_page(request, user_id):

    my_youtubers = MyYoutuber.objects.filter(user=user_id, activated=True).order_by('-listed_date')
    context = {'my_youtuber': my_youtubers}
    
    return render(request, 'accounts/mypage.html', context)


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("youtuber:index")

@login_required
def change_nickname(request):
    if request.method == 'POST':
        change_nickname = request.POST.get('change_nickname')
        try:
            user = User.objects.get(nickname=change_nickname)
            messages.info(request, '중복된 닉네임이 있습니다')
            return redirect('account_change_nickname')
        except ObjectDoesNotExist:
            request.user.nickname = change_nickname
            request.user.save()
            messages.info(request, '닉네임 변경 완료')
            return redirect('account_change_nickname')
    return render(request, 'accounts/change_nickname.html')
    


# 이전 인증 기능
# def sign_up(request):
#     context ={}

#     if request.method == 'POST':
#         if (request.POST.get('username') and 
#             request.POST.get('password') and
#             request.POST.get('password') == request.POST.get('password_check')):

#             new_user = User.objects.create_user(
#                 username = request.POST.get('username'),
#                 password = request.POST.get('password'),
#             )

#             auth.login(request, new_user)
#             return redirect('youtuber:index')
        
#         else:
#             context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'

#     return render(request, 'accounts/sign_up.html', context)    
    
# def login(request):
#     context = {}

#     if request.method == 'POST':
#         if request.POST.get('username') and request.POST.get('password'):

#             user = auth.authenticate(
#             request,
#             username = request.POST.get('username'),
#             password = request.POST.get('password')
#             )

#             if user is not None:
#                 auth.login(request, user)
#                 return redirect('youtuber:index')
#             else:
#                 context['error'] = '아이디와 비밀번호를 다시 확인해주세요..'

#         else:
#             context['error'] = '아이디와 비밀번호를 모두 입력해주세요.'
    
#     return render(request, 'accounts/login.html', context)

# def logout(request):
#     auth.logout(request)

#     return redirect('youtuber:index')
