from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

data = {
      "id": 1,
      "name": "Zia",
      "job": "backend developer",
}

@api_view()
def post_list(request):
      return Response("ok")

@api_view()
def post_detail(request,id):
      return Response(data)