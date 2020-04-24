# brogアプリのurlの紐づけ
# このファイルで定義したurlは、プロジェクト全体のurls.pyから参照される
from django.urls import path
from . import views

app_name = 'blog'
urlpatterns = [
	 path('' ,views.post_list ,name = 'post_list'),
]
	# path('' ,views.post_list ,name = 'post_list'),
	#path('' ,views.post_list.as_view()  ,name = 'post_list'),
 
