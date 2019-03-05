#!/usr/bin/env python
# -*- coding: utf-8 -*-

#TODO hardcore

from django.conf import settings

from . import models


class Authentication(object):

    @staticmethod
    def register(request, return_path):
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            account = models.Account.objects.get(
                username=username,
                password=password,
            )
        except:
            account = None

        if account is None:
            new_account = models.Account(
                username=username,
                password=password,
            )
            new_account.save()
            msg = 'success register'
        return return_path

    @staticmethod
    def login_required(request, return_path_with_login, return_path_without_login):
        try:
            if 'username' in request.session[settings.SESSION_ITEMS_KEYS_PREFIX+'_u']:
                return True, 'has_key', return_path_with_login
            else:
                return False, 'no key', return_path_without_login
        except:
            return False, 'no key', return_path_without_login

    @staticmethod
    def login_register(request, return_path_success, return_path_fail):
        flag = True
        msg = ''
        info = ''
        action = request.POST.get('action')
        if action == 'login':
            username = request.POST.get('username1')
            password = request.POST.get('password1')
            try:
                account = models.Account.objects.values(
                    "username", "password", "email_address",
                    "account_group_id", "account_category_id",
                ).get(
                    username__iexact=username,
                    password=password,
                )
                msg = ''
            except:
                account = None
                msg = ''

            if account:
                request.session[settings.SESSION_ITEMS_KEYS_PREFIX+'_u'] = account
                info = return_path_success
            else:
                info = return_path_fail

        elif action == 'register':
            username = request.POST.get('username2')
            password = request.POST.get('password2')
            confirm_password = request.POST.get('confirm_password')
            email = request.POST.get('email')
            if password != confirm_password:
                msg = 'password and confirm password is not matching'
                flag = False
            else:
                try:
                    new_account = models.Account.objects.get(
                        username=username,
                    )
                except:
                    new_account = None
                if new_account:
                    msg = '%s already registered, please use other username' % username
                    flag = False
                else:
                    new_account = models.Account(
                        username=username,
                        password=password,
                        email_address=email,
                    )
                    new_account.save()
                    msg = '%s successful register' % username
            info = return_path_fail
        return flag, msg, info

    @staticmethod
    def logout(request, return_path):
        for key in request.session.keys():
            if key is None or key.startswith(settings.SESSION_ITEMS_KEYS_PREFIX):
                del request.session[key]
        return True, '', return_path


class Session(object):

    @staticmethod
    def get_session_info(request):
        return request.session[settings.SESSION_ITEMS_KEYS_PREFIX+'_u']

    @staticmethod
    def get_session_specific_info(request, field_name):
        return request.session[settings.SESSION_ITEMS_KEYS_PREFIX+'_u'][field_name]
