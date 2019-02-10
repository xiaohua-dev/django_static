from django.http import HttpResponse

class BlockedIPSMiddleware(object):
    EXCLUB_IPS = ['223.71.231.4']

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockedIPSMiddleware.EXCLUB_IPS:
            return HttpResponse('<h1>deny</h1>')