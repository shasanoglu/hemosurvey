from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden, HttpResponseNotFound
from hasta.models import Hasta, DiyalizOlayi
from home.models import AylikVeri
from decimal import Decimal
from django.db.models import Avg, Min, Max, F
from datetime import datetime


def median_value(queryset, term):
    count = queryset.count()
    values = queryset.values_list(term, flat=True).order_by(term)
    if count % 2 == 1:
        return values[int(round(count/2))]
    else:
        return sum(values[count/2-1:count/2+1])/Decimal(2.0)

def demografik(request):
    all_hastas = Hasta.objects
    male_hastas = all_hastas.filter(cinsiyet='e')
    female_hastas = all_hastas.filter(cinsiyet='k')
    ahc = all_hastas.count()
    mhc = male_hastas.count()
    fhc = female_hastas.count()

    median_birth_year = median_value(all_hastas,'dogum_yili')
    age = all_hastas.aggregate(age_min = Min(datetime.now().year - F('dogum_yili')),
                               age_max=Max(datetime.now().year - F('dogum_yili')),
                               age_avg=Avg(datetime.now().year - F('dogum_yili')))

    median_diyaliz_year = median_value(all_hastas,'diyaliz_ilk_yil')
    diyaliz_yil = all_hastas.aggregate(diy_min = Min(datetime.now().year - F('diyaliz_ilk_yil')),
                                       diy_max=Max(datetime.now().year - F('diyaliz_ilk_yil')),
                                       diy_avg=Avg(datetime.now().year - F('diyaliz_ilk_yil')))

    stats = {
        'toplam_hasta': ahc,
        'erkek_hasta': "{} (%{})".format(mhc,100.0*mhc/ahc),
        'kadin_hasta': "{} (%{})".format(fhc,100.0*fhc/ahc),
        'age': "Min: {}, Max: {}, Avg: {}, Med: {}".format(age['age_min'],age['age_max'],age['age_avg'], datetime.now().year - median_birth_year),
        'diyaliz_year': "Min: {}, Max: {}, Avg: {}, Med: {}".format(diyaliz_yil['diy_min'],diyaliz_yil['diy_max'],diyaliz_yil['diy_avg'], datetime.now().year - median_diyaliz_year),
    }

    return render(request, 'stats/demografik.html', {'stats':stats})

def ayh_vb(request):
    hastalar = Hasta.objects.order_by('id')
    return render(request, 'stats/ayh_vb.html', {'hastalar': hastalar})

def seroloji_diger(request):
    hastalar = Hasta.objects.order_by('id')
    return render(request, 'stats/seroloji_diger.html', {'hastalar': hastalar})

def aylik_veri(request):
    aylik_veriler = AylikVeri.objects.filter(isUpdated=True).order_by('merkez','yil','ay')
    return render(request, 'stats/aylik_veri.html', {'aylik_veriler': aylik_veriler})

def olay(request):
    olaylar = DiyalizOlayi.objects.all()
    return render(request, 'stats/olay.html', {'olaylar': olaylar})



stat_types = {
    'demografik': {
        'description' : 'Demografik özellikler',
        'func': demografik,
    },
    'ayh_vb': {
        'description': 'Komorbid hastalıklar (tüm hastalar)',
        'func': ayh_vb,
    },
    'seroloji_diger': {
        'description': 'Seroloji/Aşı/Diğer (tüm hastalar)',
        'func': seroloji_diger,
    },
    'aylik_veri': {
        'description': 'Aylık ilk iki gün hasta sayısı verisi',
        'func': aylik_veri,
    },
    'olay': {
        'description': 'Diyaliz olayları',
        'func': olay,
    },
}


@login_required
def stat(request):
    if not request.user.is_staff:
        return HttpResponseForbidden

    stat_type_name = request.GET.get("type",None)

    if stat_type_name:
        stat_type = stat_types.get(stat_type_name,None)
        if stat_type:
            return stat_type['func'](request)
        else:
            return HttpResponseNotFound
    else:
        return render(request,'stats/stat_list.html',{'stat_types': stat_types,})

