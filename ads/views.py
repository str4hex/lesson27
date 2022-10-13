from django.http import JsonResponse
from django.views import View


# Create your views here.

class IndexView(View):

    def get(self, request):
        return JsonResponse({"status": "ok"})