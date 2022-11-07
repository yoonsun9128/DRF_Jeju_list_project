from django.urls import path, include
from main import views
app_name = 'main'


urlpatterns = [
    path('', views.StoreListView.as_view(), name='storelist_view'), # 메인페이지에 처음 별점 높은 가게 순으로 보여줌.
    path('<int:store_id>/', views.StoreSearchView.as_view(), name='storeSearch_view'), # 검색창에 검색했을 때 검색한 가게만 보여줌
    path('<int:store_id>/comment/', views.CommentView.as_view(), name='comment_view'),
]
