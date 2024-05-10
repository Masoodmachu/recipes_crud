
from django.urls import path, include
from recipe import views

urlpatterns = [

    # path('',views.create,name='create'),
    # path('recipedetail/<int:pk>',views.bookdetail,name='details')


    path('',views.Create.as_view()),
    path('details/<int:pk>',views.Details.as_view()),
    path('logout/',views.Logout.as_view()),
    path('reviewcreate/',views.createrev.as_view()),
    path('reviewdetailail/<int:pk>',views.detailrev.as_view()),
    path('Cuisinfilter/',views.Cuisinfilter.as_view()),
    path('Mealfilter/',views.Mealfilter.as_view()),
    path('Ingredientsfilter/',views.Ingredientsfilter.as_view()),
    path('search/',views.Search.as_view()),

    # path('register/',views.Register.as_view())
]
