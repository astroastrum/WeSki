from django.urls import path,re_path
from . import views
app_name= "reviews"

urlpatterns = [
    # re_path(r"create\Z",views.create,name="create"),
    # re_path(r"delete/(?P<review_pk>\d+)\Z",views.delete, name="delete"),
    # re_path(r"likes/(?P<review_pk>\d+)\Z",views.likes,name="likes"),
    # re_path(r"update/(?P<review_pk>\d+)\Z",views.update,name="update"),
    # re_path(r"image_delete/(?P<review_pk>\d+)/(?P<reviewimage_pk>\d+)\Z",views.image_delete,name="image_delete"),
    # re_path(r"image_add/(?P<review_pk>\d+)\Z",views.image_add,name="image_add"),
    # re_path(r"(?P<review_pk>\d+)\Z",views.detail,name="detail"),
    path("",views.index,name="index"),
    path("create/",views.create,name="create"),
    path("<int:review_pk>/delete/",views.delete, name="delete"),
    path("<int:review_pk>/likes/",views.likes,name="likes"),
    path("<int:review_pk>/update/",views.update,name="update"),
    path("<int:review_pk>/<int:reviewimage_pk>/image_delete/",views.image_delete,name="image_delete"),
    path("<int:review_pk>/image_add/",views.image_add,name="image_add"),
    path("<int:review_pk>/",views.detail,name="detail"),
    ]
