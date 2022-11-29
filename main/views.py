from main.models import Store, Comment
from main.serializers import StoreListSerializer, CommentSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from main import function
from main import test
from main.function import *
import random
#파일 형서하는데 필요한 코드
# import json , csv, os, requests
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "onepaper.settings")
# import django
# django.setup()

# test.GetStoreId()

class StoreListView(APIView):
    def get(self, request):
        All_store = list(Store.objects.filter(star__gte=3.5))
        stores = random.sample(All_store, 6)
        # store = Store.objects.all() #테스트
        serializer = StoreListSerializer(stores, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


#머신러닝을 통한 검색
class StoreSearchView(APIView):
    def get(self, request, store_id) :
        store = Store.objects.get(id = store_id) # stores = 사형제횟짐
        store_obj = store.store_name

        function_stores = function.get_recommendations(store_obj, cosine_a) #stores=사형제횟집을 넣은 유사도검사 결과값을 function_stores에 넣음.
        function_stores_info = []
        for store in function_stores :
            store_info = Store.objects.get(store_name = store)  # 가장 비슷한 리뷰를 가진 상호명들 중에 a를 뽑아서 디비에서 a의 상호명을 가져와서 a의 모든 정보를 store_info에 넣음
            function_stores_info.append(store_info) # store_info을 function_stores_info에 차곡차곡 쌓음
        serializer = StoreListSerializer(function_stores_info, many=True) # 시리얼라이즈하기
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CommentView(APIView):
    def get(self, request, store_id):
        store = Store.objects.get(id=store_id)
        comments = store.comment_set.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, store_id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, store_id=store_id)
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 파일 저장하는 코드
# with open('storedata.csv', 'w', newline='') as csvfile:
#     fieldnames = ['id','store_url','store_name','content']
#     writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#     writer.writeheader()

#     for store in Store.objects.all():
#         writer.writerow({'id':store.id, 'store_url':store.store_url,'store_name':store.store_name,'content':store.content })