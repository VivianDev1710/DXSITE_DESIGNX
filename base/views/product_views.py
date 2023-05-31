
from rest_framework.response import Response
from rest_framework.decorators import api_view

from base.models import Product
from base.serializers import ProductSerializer
from django.core.paginator import Paginator , EmptyPage , PageNotAnInteger
# Create your views here.



@api_view(['GET'])
def getProducts(request):
    query=request.query_params.get('keyword')
    if query==None:
        query=''
    products = Product.objects.filter(name__icontains = query)

    page=request.query_params.get('page')
    paginator = Paginator(products,4)
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    
    if page == None:
        page = 0

    page =int(page)   

    serializer = ProductSerializer(products, many=True)
    return Response({'products':serializer.data,'page':page,'pages':paginator.num_pages})

@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)
