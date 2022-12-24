from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('blogs/', views.blognews, name='blognews'),
    path('addpost/', views.addpost, name='addpost'),
    path('blogs/editpost/<id>/',views.editpost,name='editpost'),

    path('blogs/',views.search,name="search"),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)



#fix error
#got id number (     path('blogs/editpost/<id>/',views.editpost,name='editpost'),        )

#add something else to the url