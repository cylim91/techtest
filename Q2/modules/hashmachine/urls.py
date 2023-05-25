from django.urls                    import path
import modules.hashmachine.views    as hm_view

app_name = 'hashmachine'

urlpatterns = [
    path('generate_hash/',  hm_view.RandomHashView.as_view(), name='generate_hash'),
    path('check_hash/',     hm_view.CheckHashView.as_view(),  name='check_hash'),
]