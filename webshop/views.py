from django.shortcuts import render,HttpResponse
from webshop.models import Commodity
from webshop.models import Thumb
from webshop.models import Option
from django.http import JsonResponse
from django.core import serializers
from django.db.models import Q

# Create your views here.
class HttpCode(object):
	success = 0
	error = 1

def result(code=HttpCode.success, message='', data=None, kwargs=None):
    json_dict = {'status': code, 'message': message, 'data': data}
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict, json_dumps_params={'ensure_ascii': False})
 
 
def success(data=None):
    return result(code=HttpCode.success, message='success', data=data)
 
 
def error(data=None):
    return result(code=HttpCode.error, message='error', data=data)

def commodity_content(request):
	json_list = []
	type = request.GET.get('type',default='computer')
	number = int(request.GET.get('number',default=2))
	commoditys = Commodity.objects.all().filter(type=type)[:number]
	for commodity in commoditys:
		json_dict = {}
		json_dict["id"] = commodity.id
		json_dict["name"] = commodity.name
		json_dict["introduce"] = commodity.introduce
		json_dict["img_url"] = commodity.img_url
		json_dict["thumb_url"] = commodity.thumb_url
		json_dict["price"] = commodity.price
		json_list.append(json_dict)
	json_list = {type:json_list}
	return success(json_list)
def commodity_search(request):
	json_list = []
	word = request.GET.get('word')
	commoditys = Commodity.objects.all().filter(Q(name__contains=word)|Q(introduce__contains=word))
	for commodity in commoditys:
		json_dict = {}
		json_dict["id"] = commodity.id
		json_dict["name"] = commodity.name
		json_dict["introduce"] = commodity.introduce
		json_dict["img_url"] = commodity.img_url
		json_dict["thumb_url"] = commodity.thumb_url
		json_dict["price"] = commodity.price
		json_list.append(json_dict)
	return success(json_list)
def commodity_detail(request,id):
	commodity = Commodity.objects.all().get(id=id)
	thumbs = Thumb.objects.all().filter(itemid=id)
	options = Option.objects.all().filter(itemid=id)
	json_dict = {}
	json_dict["id"] = commodity.id
	json_dict["name"] = commodity.name
	json_dict["introduce"] = commodity.introduce
	json_dict["img_url"] = commodity.img_url
	json_dict["thumb_url"] = commodity.thumb_url
	json_dict["price"] = commodity.price
	json_dict["stock"] = commodity.stock
	img_list = []
	for thumb in thumbs:
		img_dict = {}
		img_dict["img_url"] = thumb.imgurl
		img_list.append(img_dict)
	option_list = []
	for option in options:
		option_dict = {}
		option_dict["option"] = option.name
		option_list.append(option_dict)
	json_dict["small_image"] = img_list
	json_dict["option"] = option_list
	return success(json_dict)