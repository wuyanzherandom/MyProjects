class IPWebsite(object):
    @staticmethod
    def get_client_ip(request):
        try:
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
            if x_forwarded_for:
                ip = x_forwarded_for.split(',')[0]
            else:
                ip = request.META.get('REMOTE_ADDR')
            return ip
        except:
            return None

    @staticmethod
    def get_client_website(request):
        try:
            website = request.META.get('HTTP_HOST')
            return website
        except:
            return None


class SessionManagement(object):
    @staticmethod
    def get_request_session(request):
        return request.session[settings.SESSION_ITEMS_KEYS_PREFIX + 'u']


class Utilities(object):
    @staticmethod
    def contains_attrs(obj, attrs):
        not_found = []
        for attr in attrs:
            if not attr in obj:
                not_found.append(attr)
        return not_found if len(not_found) > 0 else None

    @staticmethod
    def get_attrs(obj, attrs, names):
        d = {}
        for idx, attr in enumerate(attrs):
            try:
                d[names[idx]] = reduce(getattr, attr.split('.'), obj)
            except AttributeError:
                d[names[idx]] = None
        return d
