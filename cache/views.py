from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from django.views.decorators.cache import cache_control
from rest_framework.response import Response
from rest_framework import status
 
# Create your views here.
 
from .models import Produto 


from django.core.cache import cache


from django.conf import settings

 



from django.views.decorators.cache import cache_page

@api_view(['GET'])
def view_produtos(request):
 
    produtos = Produto.objects.all()
    results = [p.to_json() for p in produtos]
    return Response(results, status=status.HTTP_201_CREATED)


from rest_framework.renderers import JSONRenderer

@cache_page(60 * 5,cache="MYCACHE")
@api_view(['GET'])
@renderer_classes((JSONRenderer,))
#cache_control(private=True, max_age=3600)
def view_cached_produtos(request):
    
    produtos = Produto.objects.all()
    results = [p.to_json() for p in produtos]

    content = {'produtos': results}

    return Response(content, status=status.HTTP_201_CREATED)    

#    return render(request, context={
#        'recipes': results
#        }
#    )    
#    return Response(results, status=status.HTTP_201_CREATED)    