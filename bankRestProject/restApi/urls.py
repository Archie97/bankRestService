from django.urls import path
from django.conf.urls import url
from . import views
from .views import ListBankView
from .views import DetailBankView
from .views import CreateBankView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = {
    path('bank/', ListBankView.as_view(), name="bank-all"),
    path('bank/<int:pk>/', DetailBankView.as_view(), name="bank-one"),
    path('bank/add/', CreateBankView.as_view(), name="bank-add")
}

urlpatterns = format_suffix_patterns(urlpatterns)