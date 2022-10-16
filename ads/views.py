import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ads.models import Cat, Ads


# Create your views here.

class IndexView(View):
    def get(self, request):
        return JsonResponse({"status": "ok"})


@method_decorator(csrf_exempt, name='dispatch')
class CatViews(View):
    def get(self, request):
        get_cat_all = Cat.objects.all()
        response = []

        for cat in get_cat_all:
            response.append({'id': cat.id,
                             'name': cat.name})

        return JsonResponse(response, safe=False)

    def post(self, request):
        cat_data = json.loads(request.body)
        cat = Cat.objects.create(
            name=cat_data["name"],
        )

        return JsonResponse({
            "id": cat.id,
            "name": cat.name,
        })


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
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
                "is_published": ad.is_published
            })
        return JsonResponse(response, safe=False)

    def post(self, request):
        ads_data = json.loads(request.body)

        ads = Ads.objects.create(
            name=ads_data['name'],
            author=ads_data['author'],
            price=ads_data['price'],
            description=ads_data['description'],
            address=ads_data['address'],
            is_published=ads_data['is_published']
        )
        return JsonResponse({"Id": ads.Id,
                             "name": ads.name,
                             "author": ads.author,
                             "price": ads.price,
                             "description": ads.description,
                             "address": ads.address,
                             "is_published": ads.is_published})


class AdsIdViews(View):
    def get(self, request, ad_id):
        ads_id = Ads.objects.get(Id=ad_id)
        return JsonResponse({"Id": ads_id.Id,
                             "name": ads_id.name,
                             "author": ads_id.author,
                             "price": ads_id.price,
                             "description": ads_id.description,
                             "address": ads_id.address,
                             "is_published": ads_id.is_published})


class CatIdViews(View):
    def get(self, request, cat_id):
        cat_id = Cat.objects.get(id=cat_id)

        return JsonResponse({'id': cat_id.id,
                             'name': cat_id.name})
