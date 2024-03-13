from django.http import JsonResponse

def apiProdutos(request): 
    if request.method == 'GET':
        apiProdutos = {'id':1,'nome':'Bico de Ouro'}
        return JsonResponse(apiProdutos)
