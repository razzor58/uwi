from django.shortcuts import *
from django.http import HttpResponse
from django.template import loader

from .models import MonTerminalStates

def alerts(request):
    template = loader.get_template('uwi/alerts.html')
    return HttpResponse(template.render({}, request))

def terminal_data(request):
    template = loader.get_template('uwi/terminal_data.html')
    db_data=[]
    if 'smid' in request.GET:
        sql_query='select t.rowid,t.smid,t.battery_life,main_blacklist_update_time,gsm_signal_value from mon_terminal_states t where smid=%s and create_date=(select max(create_date) from mon_terminal_states where smid=t.smid)'
        db_data = MonTerminalStates.objects.raw(sql_query,[request.GET['smid']])
    return HttpResponse(template.render({'db_data': db_data}, request))

def info(request):
    template = loader.get_template('uwi/info.html')
    return HttpResponse(template.render({}, request))


def terminal_map(request):
    template = loader.get_template('uwi/terminal_map.html')
    db_data=[]
    if 'smid' in request.GET:
        sql_query='select t.rowid,t.smid,t.battery_life,main_blacklist_update_time,gsm_signal_value from mon_terminal_states t where smid=%s and create_date=(select max(create_date) from mon_terminal_states where smid=t.smid)'
        db_data = MonTerminalStates.objects.raw(sql_query,[request.GET['smid']])
    return HttpResponse(template.render({'db_data': db_data}, request))
