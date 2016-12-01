from rest_framework_nested import routers

from authentication.views import AccountViewSet

from django.conf.urls import url, include, patterns

from rest_framework.urlpatterns import format_suffix_patterns

router = routers.SimpleRouter()
router.register(r'', AccountViewSet)

urlpatterns = patterns(
    '',
    url('', include(router.urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)
