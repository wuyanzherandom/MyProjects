# -*- coding: utf-8 -*-

import requests, json

#  facebook page - chuuni-chan

url = 'https://graph.facebook.com/'
page_id = '1494638553898709/'
urls = url + page_id
#urls_post = urls + 'feed'

access_token = 'EAATl9ac5begBABQHR46ZAJIgK9XDCRuZBfa2ZAIyMrZCPYFZAWiPWWgfc5t3tZBmowQ1Dmqivw98YC5AX5ZCbUZBHU1BZCd2VbacFooG2pvFCSHZADR7AkgPSAlQ4cSowZCm9zAXc2HZAn5abalXC8y0P3CEfLab8zWdwUZC5xUoETIISHwZDZD'
_data = {
    'access_token': access_token,
    #'field': 'access_token',
    #'message': 'hi',
}


class GetAction(object): # need to refer to facebook api

    @staticmethod
    def send_url(url, _data):
        value = requests.get(url, params=_data)
        return json.loads(value.text)

    @staticmethod
    def get_admin_notes(_data=_data):
        _urls_post = urls + 'admin_notes'
        return GetAction.send_url(_urls_post, _data=_data)


    @staticmethod
    def get_album(_data=_data):
        _urls_post = urls + 'albums'
        print _urls_post
        return GetAction.send_url(_urls_post, _data=_data)


class PostAction(object):  # need to refer to facebook api

    @staticmethod
    def send_url(url, _data):
        value = requests.post(url, params=_data)
        return json.loads(value.text)

    @staticmethod
    def send_post(_data=_data, message="test"):
        _data.update({
            'message': message,
        })
        _urls_post = urls + 'feed'
        return PostAction.send_url(_urls_post, _data=_data)

    @staticmethod
    def send_single_photo(photo_url, caption, publish=True):
        _data.update({
            'url': photo_url,
            'caption': caption,  # photo message
            'publish': 'true' if publish else 'false',
        })
        urls_post = urls + 'photos'
        return PostAction.send_url(urls_post, _data=_data)

    @staticmethod
    def create_album(name):
        urls_post = urls + 'albums'
        _data.update({
            'name': name,
        })
        return PostAction.send_url(urls_post,_data=_data)

    @staticmethod
    def send_multi_photo(photo_datas, album_name):
        album = PostAction.create_album(album_name)
        urls_post = url + album['id'] + '/photos'
        for photo_data in photo_datas:
            _data.update({
                'url': photo_data['url'],
                'message': photo_data['message'],
            })
            PostAction.send_url(urls_post, _data=_data)
        #return PostAction.send_url(urls_post, _data=_data)


"""
#example
print Action.send_single_photo(
    photo_url='http://52.187.66.115:8000/media/animenet/character/36967_MVEAdWF.jpg',
    caption='test',
    publish=False,
)
"""

"""
photo_datas = [
    {
        'url': 'http://52.187.66.115:8000/media/animenet/character/36967_MVEAdWF.jpg',
        'message': 'Inori',
    },
    {
        'url': 'http://52.187.66.115:8000/media/animenet/character/36967_MVEAdWF.jpg',
        'message': 'Inori2',
    }
]

"""

"""
print PostAction.send_multi_photo(
    photo_datas=photo_datas,
    album_name='Album Test'
)
"""