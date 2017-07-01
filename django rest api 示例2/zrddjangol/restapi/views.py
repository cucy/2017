from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


from .models import Author
from .serializer import AuthorSerializer


class JsonResponse_(HttpResponse):
    def __init__(self,data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'applicaton/json'
        super(JsonResponse_, self).__init__(content, **kwargs)
# csrf_token
@csrf_exempt
def author_list(request):
    if request.method == 'GET':
        author = Author.objects.all()
        serializer = AuthorSerializer(author, many=True)
        return JsonResponse_(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse_(serializer.data,status=201)
        return JsonResponse_(serializer.data,status=400)

@csrf_exempt
def author_detail(request, pk):
    try:
        author = Author.objects.get(pk=pk)
    except Author.DoesNotExist:
        return JsonResponse_(status=404)

    if request.method == 'GET':
        serializer = AuthorSerializer(author)
        return JsonResponse_(serializer.data)
    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = AuthorSerializer(author, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse_(serializer.data)
        return JsonResponse_(serializer.errors, status=400)

    elif request.method == 'DELETE':
        author.delete()
        return JsonResponse_('',status=204)
