from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostEdit, PostDelete, PostSearch, subscribe, CategoryListView
#AppointmentView , unsubscribe
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('articles/create/', PostCreate.as_view(), name='articles_create'),
    path('articles/<int:pk>/edit/', PostEdit.as_view(), name='articles_edit'),
    path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
 #   path('mail/', AppointmentView.as_view(template_name='appointment_created.html') ,name='appointment'),
 #   path('appointments/', AppointmentView.as_view(template_name='make_appointment.html'), name='appointment'),
 #   path('subscribe/<int:pk>', subscribe, name='subscribe'),
 #   path('unsubscribe/<int:pk>', unsubscribe, name='unsubscribe'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),

]
#path('<int:pk>/edit/', cache_page(60)(PostEdit.as_view()), name='post_edit'), кеш страницы