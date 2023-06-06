from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt import views as jwt_views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from apps.users.views import (
    RegisterView,
    LoginView,
    UserViewSet,
    ChangePasswordView,
    ResetPasswordAPIView,
)

from apps.posts.views import (
    PostListCreateView,
    PostDetailView,
    PostListView,
    CommentCreateView,
    CommentListView,
)

from apps.feedback.views import (
    FeedbackMessageCreateView,
    FavoriteCreateDestroyView,
    FavoriteListView,
)

from apps.faq.views import (
    FAQListView,
)

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")

users_urls = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('change-password/', ChangePasswordView.as_view(), name='change_password'),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='reset_password'),
]

posts_urls = [
    path('create_post/', PostListCreateView.as_view(), name='post_list'),
    path('detailed_post/', PostDetailView.as_view(), name='post_detail'),
    path('all_posts/', PostListView.as_view(), name='all_postlist'),
    path('create_comment/', CommentCreateView.as_view(), name='comment_create'),
    path('all_comments/', CommentListView.as_view(), name='post-comments'),

]

feedback_urls = [
    path('create_feedback/', FeedbackMessageCreateView.as_view(), name='feedback_create'),
    path('add_to_favorite/', FavoriteCreateDestroyView.as_view(), name='favorite_create'),
    path('all_favorites/', FavoriteListView.as_view(), name='favorites_list')
]

faq_urls = [
    path('frequently_asked_questions/', FAQListView.as_view())
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(users_urls)),
    path('user/', include(router.urls)),
    path('posts/', include(posts_urls)),
    path('feedback/', include(feedback_urls)),
    path('faq/', include(faq_urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
