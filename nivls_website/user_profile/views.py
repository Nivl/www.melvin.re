import uuid
from django.http import HttpResponseForbidden
from django.utils.translation import ugettext as _
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.template.loader import render_to_string
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.views import login
from django.core.urlresolvers import resolve, Resolver404, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from commons.forms import BootstrapLoginForm, CroppedImageForm
from social_auth.models import UserSocialAuth
from forms import *

def sign_up(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse('home'))
    else:
        if request.method == 'POST':
            if request.is_ajax():
                form = UserForm(request.POST)
                if form.is_valid():
                    u = User.objects.create_user(form.cleaned_data['username']
                                                 ,form.cleaned_data['email']
                                                 ,form.cleaned_data['password1'])
                    u.first_name = form.cleaned_data['first_name'];
                    u.last_name = form.cleaned_data['last_name'];
                    u.is_staff = False;
                    u.is_active = False;
                    u.is_superuser = False;
                    u.save()
                    profile = UserProfile.objects.get(user=u)
                    profile.activation_code = uuid.uuid4()
                    profile.save()

                    subject = _('Your validation link')
                    text_content = render_to_string('users/sign_up_mail.txt'
                                                    ,{'user': u
                                                      ,'code': profile.activation_code})
                    html_content = render_to_string('users/sign_up_mail.html'
                                                    ,{'user': u
                                                      ,'code': profile.activation_code})
                    msg = EmailMultiAlternatives(subject
                                                 ,text_content
                                                 ,settings.EMAIL_NO_REPLY
                                                 ,[u.email])
                    msg.attach_alternative(html_content, 'text/html')
                    msg.send(fail_silently = True)
                    return render(request, 'users/sign_up_ok.html')
            else:
                return HttpResponseForbidden()
        else:
            form = UserForm()
        return render(request, "users/sign_up.html", {'form': form})


def activate_account(request, code):
    if not request.user.is_authenticated():
        try:
            profile = UserProfile.objects.get(activation_code=code)
            user = profile.user
            user.is_active = 1
            user.save()
            profile.activation_code = ''
            profile.save()
            return login(request, template_name='users/sign_in.html'
                         , authentication_form=BootstrapLoginForm
                         , extra_context={'success': _('Your account has been successfully activated, you can now sign in.')})
        except UserProfile.DoesNotExist:
            return login(request, template_name='users/sign_in.html'
                         , authentication_form=BootstrapLoginForm
                         , extra_context={'error': _('This activation link does not exists. If you are experiencing activation issues, you can contact us using the contact form.')})


@login_required
def view_account(request):
    pass


@login_required
def edit_profile(request):
    if request.method == 'POST':
        if request.is_ajax():
            form = UserProfileForm(request.POST, request.FILES,
                                   instance=request.user.get_profile())
            if form.is_valid():
                form.save()
                return render(request, "users/edit_profile_ok.html"
                              , {'has_file': len(request.FILES) != 0})
        else:
            return HttpResponseForbidden()
    else:
        form = UserProfileForm(instance=request.user.get_profile())
    return render(request, "users/edit_profile.html", {'form': form})


@login_required
def edit_avatar(request):
    profile = request.user.get_profile()
    if not profile.picture:
        return HttpResponseForbidden()

    ratio_list = UserProfile._meta.get_field('avatar').ratio.split('x')
    ratio = float(ratio_list[0]) / float(ratio_list[1])

    min_size = UserProfile._meta.get_field('avatar').min_size
    min_size = min_size if min_size != [0, 0] else False

    max_size = UserProfile._meta.get_field('avatar').max_size
    max_size = max_size if max_size != [0, 0] else False

    select = []
    for select_list in profile.avatar.split(" "):
        x, y = select_list.split("x")
        select.append([x, y])

    if request.method == 'POST':
        if request.is_ajax():
            form = CroppedImageForm(request.POST, field='avatar'
                                    , obj=UserProfile, image=profile.picture)
            if form.is_valid():
                profile.avatar = form.cleaned_data['coordinates']
                profile.save()
                return render(request, 'users/edit_avatar_ok.html')
        else:
            return HttpResponseForbidden()
    else:
        form = CroppedImageForm(field='avatar', obj=UserProfile
                                , image=profile.picture
                                , initial={'coordinates': profile.avatar})

    return render(request, "users/edit_avatar.html", {
            'picture': profile.picture
            , 'current': profile.avatar
            , 'ratio': ratio
            , 'min_size': min_size
            , 'max_size': max_size
            , 'select': select
            , 'form': form
            })


@login_required
def edit_account(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
    else:
        form = UserForm()
    return render(request, "users/edit.html", {'form': form})


@login_required
def manage_social_account(request):
    return render(request, "users/manage_social_accounts.html")


def sign_in(request):
    if request.user.is_authenticated():
        try:
            resolve(request.GET.get('next', ''))
            return HttpResponseRedirect(request.GET.get('next'))
        except Resolver404:
            return HttpResponseRedirect(reverse('home'))
    else:
        return login(request, template_name='users/sign_in.html'
                     ,authentication_form=BootstrapLoginForm)
