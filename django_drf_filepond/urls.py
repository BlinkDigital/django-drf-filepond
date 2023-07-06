"""FilePond server-side URL configuration

Based on the server-side configuration details
provided at:
https://pqina.nl/filepond/docs/patterns/api/server/#configuration
"""
from django.urls import path, re_path, include
from django_drf_filepond.views import ProcessView, RevertView, LoadView,\
     RestoreView, FetchView, PatchView

urlpatterns = [
    re_path(r'^process/$', ProcessView.as_view(), name='process'),
    re_path(r'^patch/(?P<chunk_id>[0-9a-zA-Z]{22})$', PatchView.as_view(),
        name='patch'),
    re_path(r'^revert/$', RevertView.as_view(), name='revert'),
    re_path(r'^load/$', LoadView.as_view(), name='load'),
    re_path(r'^restore/$', RestoreView.as_view(), name='restore'),
    re_path(r'^fetch/$', FetchView.as_view(), name='fetch')
]
