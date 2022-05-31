

from ast import Try
from datetime import datetime
from ipaddress import ip_address
from multiprocessing import context
from tabnanny import check
from django.conf import settings
from . models import Visitor_Infos
from django.shortcuts import render

import socket
import random


def save_visitor_infos(request):
    try:
        # -------get visitor ip-------#

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.spit(',')[0]
        else:
            ip=request.META.get('REMOTE_ADDR')

            # ----------check if ip adress is valid--------------#*
        try:
            socket.inet_aton(ip)
            ip_valid = True

        except socket.error:
            ip_valid=False

            #-------------- check if ip adress is valid---------------#
        if ip_valid:

            present_data = datetime.datetime.now()
            ref_date_1 = present_data - datetime.timedelta(days =1)
            ref_date_2 = present_data - datetime.timedelta(days=2)

        if Visitor_Infos.objects.filter(ip_address=ip, page_visited=request.path, event_date__gte=ref_date_1).count()==0:
            new_visitor_infos=Visitor_Infos(
                ip_address=ip,
                page_visited = request.path,
                event_date = present_data
            )
            new_visitor_infos.save()

        if Visitor_Infos.objects.filter(ip_address, page_visited=request.path, event_date__gte=ref_date_1).count()==1:
            visitor_infos_obj = Visitor_Infos.objects.get(ip_address=ip, page_visited=request.path,event_date__gte=ref_date_1)
            visitor_infos_obj.event_date=present_data
            visitor_infos_obj.save()

    except:
        pass

    context_nb_visitors=0
    ref_date = present_data - datetime.timedelta(minutes=5)
    context_nb_visitors = Visitor_Infos.objects.filter(event_date__gte=ref_date).values_list('ip_address',flat=True).distinct().count()

    context={
        'nb_visiteur':context_nb_visitors
    }

    return render(request,'pages/header.html',context )


    