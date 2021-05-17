from django.urls import path


from .views import (
    home_v1,
    home_v2,
    home_v3,

    detail_v1,
    detail_v2,
    detail_v3,

    result_v1,
    result_v2,
    result_v3,
    
    vote_v1,
    vote_v2,
    vote_v3,
)

app_name='poll'

urlpatterns=[
    path('v1/', home_v1, name='home_v1'),
    path('v2/', home_v2, name='home_v2'),
    path('v3/', home_v3, name='home_v3'),
    
    path("detail/v1/<int:question_id>/", detail_v1, name='detail_v1'),
    path("detail/v2/<int:question_id>/", detail_v2, name='detail_v2'),
    path("detail/v3/<int:question_id>/", detail_v3, name='detail_v3'),

    path('result/v1/<int:question_id>/', result_v1, name='result_v1'),
    path('result/v2/<int:question_id>/', result_v2, name='result_v2'),
    path('result/v3/<int:question_id>/', result_v3, name='result_v3'),
    
    path('vote/v1/<int:question_id>/', vote_v1, name='vote_v1'),
    path('vote/v2/<int:question_id>/', vote_v2, name='vote_v2'),
    path('vote/v3/<int:question_id>/', vote_v3, name='vote_v3'),
]