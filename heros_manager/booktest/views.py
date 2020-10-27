from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from booktest.models import HeroInfo,BookInfo
import json


# Create your views here.

# # 接口1：获取所有的英雄人物数据
# =============================================================================
# API: GET /heros/
# =============================================================================
# 请求参数:
#     无
# =============================================================================

class show_heros(View):

    def get(self, request):
        hero_list=[]
        heros=HeroInfo.objects.all()
        for hero in heros:
            hero_dict={
                "id": hero.id,
                "hname": hero.hname,
                "hgender": hero.hgender,
                "hcomment": hero.hcomment,
                "hbook": hero.hbook.btitle
            }
            hero_list.append(hero_dict)

        return JsonResponse({"code": "响应码", "message": "提示信息", "heros": hero_list})

    # # 接口2：新增一个英雄人物数据
    # =============================================================================
    # API: POST /heros/
    # =============================================================================
    def post(self, request):
        # 0.json 数据传入
        # 1. 查看英雄是否存在
        # 2. 用户输入的参数是否完整

        request_data=json.loads(request.body)
        hname=request_data["hname"]
        hgender=request_data["hgender"]
        hcomment=request_data["hcomment"]
        hbook_id=request_data["hbook_id"]
        param=[hname, hgender, hcomment, hbook_id]

        if not all(param):
            return JsonResponse({"message": "参数不完整！"})

        # 图书是否存在
        try:
            book = BookInfo.objects.get(id=hbook_id)
        except BookInfo.DoesNotExist:
            return JsonResponse({'code': 400,
                                 'message': '图书数据不存在!'})

        # ③ 更新指定英雄人物的数据
        try:
            hero=HeroInfo.objects.create(hname=hname,
                                         hgender=hgender,
                                         hcomment=hcomment,
                                         hbook_id=hbook_id)
        except Exception as e:
            return JsonResponse({'code': 400,
                                 'message': '更新数据出错!'})

        # ④ 将更新的英雄人物的数据返回
        data = {
            'id': hero.id,
            'hname': hero.hname,
            'hgender': hero.hgender,
            'hcomment': hero.hcomment,
            'hbook': hero.hbook.btitle
        }
        return JsonResponse({'code': 0,
                             'message': 'OK',
                             'hero': data})


class GetById(View):
    def get(self, request, id):

        # 查询英雄是否存在
        try:
            hero=HeroInfo.objects.get(id=id)
        except HeroInfo.DoesNotExist:
            return JsonResponse({"message": "Not Found"})

        hero_list=[]
        hero_dict={
            "id": hero.id,
            "hname": hero.hname,
            "hgender": hero.hgender,
            "hcomment": hero.hcomment,
            "hbook": hero.hbook.btitle
        }
        hero_list.append(hero_dict)
        return JsonResponse({"code": 0, "messgae": "ok", "heros": hero_list})

    def put(self, request, id):

        # ① 根据ID查询数据库获取指定的英雄人物数据
        try:
            hero=HeroInfo.objects.get(id=id)
        except HeroInfo.DoesNotExist:
            return JsonResponse({'code': 400,
                                 'message': '英雄数据不存在!'})

        request_data=json.loads(request.body)
        hname=request_data["hname"]
        hgender=request_data["hgender"]
        hcomment=request_data["hcomment"]
        hbook_id=request_data["hbook_id"]
        param=[hname, hgender, hcomment, hbook_id]

        if not all(param):
            return JsonResponse({"message": "参数不完整！"})

        try:
            hero=BookInfo.objects.get(id=hbook_id)
        except HeroInfo.DoesNotExist:
            return JsonResponse({"message": "Not Found"})

        try:
            hero=HeroInfo.objects.filter(id=id).update(hname=hname, hgender=hgender, hcomment=hcomment, hbook_id=hbook_id)
        except Exception as e:
            return JsonResponse({'code': 400,
                                 'message': '更新数据出错!'})

        hero = HeroInfo.objects.get(id=id)
        hero_list=[]
        hero_dict={
            "id": hero.id,
            "hname": hero.hname,
            "hgender": hero.hgender,
            "hcomment": hero.hcomment,
            "hbook": hero.hbook.btitle
        }
        hero_list.append(hero_dict)
        return JsonResponse({"code": 0, "messgae": "ok", "heros": hero_list})

    def delete(self, request, id):
        try:
            hero = HeroInfo.objects.get(id=id)
        except HeroInfo.DoesNotExist:
            return JsonResponse({'code': 400,'message': '英雄数据不存在!'})

        try:
            hero=HeroInfo.objects.filter(id=id).delete()
        except HeroInfo.DoesNotExist:
            return JsonResponse({"message": "参数不完整！"})

        return JsonResponse({"code": 0, "message": "OK"})
