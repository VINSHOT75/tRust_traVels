from django.urls import path

from . import views

urlpatterns = [
 path('',views.home,name="home"),
path("contact/",views.contact,name = "contact"),
path("about/",views.about,name = "about"),
path("tours/",views.tour,name = "tours"),
path("search/",views.search,name = "search"),
path("hotel_search/",views.hotel_search,name = "hotel_search"),
path("tours/discover/<int:myid>",views.discover,name = "discover"),
path("tours/discover/<int:myid>/hotel/",views.hotel,name = "hotel"),
path("tours/discover/<int:myid>/hotel/<int:myyid>/",views.hotel_view,name = "hotel_view"),
path("tours/discover/<int:myid>/hotel/<int:myyid>/payment/",views.payment,name = "payment"),
]
