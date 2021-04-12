from django.urls import path

from . import views

app_name = 'polls' # 여러 app에서 같은 viewname을 사용할 수 있기 떄문에 app name을 template에 명시하기 위함 ex. 'app_name:view_name'
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]