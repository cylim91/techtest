from django.urls                    import path
import modules.hashmachine.views    as hm_view

app_name = 'hashmachine'

urlpatterns = [
    path('generate_hash/',            hm_view.RandomHashView.as_view(),         name='generate_hash'),
    path('get_odd_hash/',             hm_view.GetOddHashView.as_view(),         name='get_odd_hash'),
    path('get_optimized_odd_hash/',   hm_view.OptimizingOddHashView.as_view(),  name='get_optimized_odd_hash'),
]