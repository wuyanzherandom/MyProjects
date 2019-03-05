#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.views.generic import TemplateView, View
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest, HttpResponseServerError, Http404

from . import utils, models

"""
sample:
class SampleView(SampleClass, TemplateView):

    template_name = ''

    def get_context_data(self, *args, **kwargs):
        context = super(SampleView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)
"""


class DefaultView(View):

    def get(self, request, *args, **kwargs):
        from . import utils
        flag, msg, info = utils.Authentication.login_required(request=request, return_path_with_login='/home',return_path_without_login='/login')
        return HttpResponseRedirect(info)
        #return HttpResponseRedirect('/home')


class HomeView(TemplateView):

    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        #print request.session['ums_u']
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)


class LoginView(TemplateView):

    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        flag, msg, info = utils.Authentication.login_register(request=request, return_path_success='/home', return_path_fail='/login')
        if flag:
            context['trigger_msg'] = 'info'
            context['msg'] = '123'
            return HttpResponseRedirect(info)
        else:
            context['trigger_msg'] = 'info'
            context['msg'] = msg
        return self.render_to_response(context)


class LogoutView(View):
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        flag, msg, info = utils.Authentication.logout(request=request, return_path='/')
        return HttpResponseRedirect(info)


class ProfileView(TemplateView):

    template_name = 'profile.html'

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        flag, msg, info = utils.Authentication.login_required(request=request, return_path_with_login='/profile', return_path_without_login='/login')
        if not flag:
            return HttpResponseRedirect(info)
        try:
            context['account'] = models.Account.objects.get(username__iexact=utils.Session.get_session_specific_info(request, 'username'))
        except:
            return HttpResponseRedirect('/login')
        return self.render_to_response(context)
