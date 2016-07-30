"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^sales/', 'pages.views.SalesView', name = 'sales'),
    url(r'^purchases/', 'pages.views.PurchasesView', name = 'purchases'),
    url(r'^vacancies/', 'pages.views.VacanciesView', name = 'vacancies'),
    url(r'^contacts/', 'pages.views.ContactsView', name = 'contacts'),
    url(r'^receive_purchase/', 'requests.views.save_purchase_request', name = 'receive_purchase'),
    url(r'^receive_sale/', 'requests.views.save_sale_request', name = 'receive_sale'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', 'pages.views.IndexView', name = 'index'),
]