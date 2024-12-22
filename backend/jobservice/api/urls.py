from django.urls import path
from .views import JobDataListView, JobDataDetailView , ScrapeJobView

urlpatterns = [
    path('jobs/', JobDataListView.as_view(), name='job-list'),       
    path('jobs/<int:pk>/', JobDataDetailView.as_view(), name='job-detail'),  
    path('scrape-job/', ScrapeJobView.as_view(), name='scrape-job'),
]

