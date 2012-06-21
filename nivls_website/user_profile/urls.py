from django.conf.urls.defaults import patterns, include, url
from forms import UserProfile

urlpatterns = patterns(
    'user_profile.views',

    url(r'^view/(?P<name>[\w.@+-]+)/$',
        'view_account',
        name='view-account'),

    url(r'^edit/$',
        'edit_account',
        name='edit-account'),

    url(r'^admin/$',
        'user_admin',
        name='user-admin'),

    url(r'^admin/password/$',
        'edit_password_form',
        name='edit-password-form'),

    url(r'^admin/email/$',
        'edit_email_form',
        name='edit-email-form'),

    url(r'^edit/form/$',
        'edit_account_form',
        name='edit-account-form'),

    url(r'^edit-settings/$',
        'edit_settings',
        name='edit-settings'),

    url(r'^edit-settings/form/$',
        'edit_settings_form',
        name='edit-settings-form'),

    url(r'^edit-avatar/$',
        'edit_avatar',
        name='edit-avatar'),

    url(r'^edit-avatar/form/$',
        'edit_avatar_form',
        name='edit-avatar-form'),

    url(r'^manage-social-account/$',
        'manage_social_account',
        name='manage-social-account'),

    url(r'^sign-in/$',
        'sign_in',
        name='sign-in'),

    url(r'^sign-up/$',
        'sign_up',
        name='sign-up'),

    url(r'^sign-up/form/$',
        'sign_up_form',
        name='sign-up-form'),

    url(r'^activate/(?P<code>[a-f0-9]{8}-' \
            '[a-f0-9]{4}-4[a-f0-9]{3}-' \
            '[89ab][a-f0-9]{3}-' \
            '[a-f0-9]{12})/$',
        'activate_account',
        name='activate-account'),

    url(r'^social/', include('social_auth.urls')),
    )

urlpatterns += patterns(
    '',
    url(r'^sign-out/$', 'django.contrib.auth.views.logout',
         {'next_page': '/'},
        name='sign-out'),
    )
