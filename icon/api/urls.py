from django.urls import path
from icon.api.views import PictureView, LoginView, LogoutView, RegistrationView, CommentView, SingleCommentView, SinglePictureView, LikeView, SingleLikeView


urlpatterns = [
    path('pictures/', PictureView.as_view()),
    path('pictures/<int:pk>', SinglePictureView.as_view()),
    path('comments/', CommentView.as_view()),
    path('comments/<int:pk>', SingleCommentView.as_view()),
    path('likes/', LikeView.as_view()),
    path('likes/<int:pk>', SingleLikeView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('registration/', RegistrationView.as_view()),
]
