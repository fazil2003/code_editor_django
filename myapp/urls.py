from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.home,name='Home'),
    path('code/python/',views.code_python,name='Python'),
    path('run/python/',views.run_python,name='Python1'),
    path('code/c/',views.code_c,name='Python'),
    path('run/c/',views.run_c,name='Python1'),
    path('code/cpp/',views.code_cpp,name='Python'),
    path('run/cpp/',views.run_cpp,name='Python1'),
    path('editor/python/',views.editor_python,name='Python Editor'),
    path('editor/c/',views.editor_c,name='C Editor'),
    path('editor/cpp/',views.editor_cpp,name='CPP Editor'),
]
