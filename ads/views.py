from django.http import JsonResponse
from django.views import View
from ads.models import Cat, Ads


# Create your views here.

class IndexView(View):

    def get(self, request):
        return JsonResponse({"status": "ok"})


class CatViews(View):
    def get(self, request):
        get_cat_all = Cat.objects.all()
        response = []

        for cat in get_cat_all:
            response.append({'id':cat.id,
                             'name':cat.name})

        return JsonResponse(response,safe=False)


class AdView(View):
    def get(self,request):
        ads = Ads.objects.all()
        response = []

        for ad in ads:
            response.append({
                "Id": ad.Id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published":ad.is_published
            })
        return JsonResponse(response, safe=False)