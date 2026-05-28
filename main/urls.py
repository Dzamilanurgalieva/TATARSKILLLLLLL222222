from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('education/', views.education, name='education'),
    path('community/', views.community, name='community'),
    path('ratings/', views.ratings, name='ratings'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('api/chat/', views.chat_api, name='chat_api'),
    path('courses/', views.all_courses, name='all_courses'),
    path('communities/', views.all_communities, name='all_communities'),
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('course/<slug:course_slug>/lesson/<int:order>/', views.lesson_detail, name='lesson_detail'),
    path('lesson/<int:lesson_id>/test/', views.take_test, name='take_test'),
    path('lesson/<int:lesson_id>/test/submit/', views.submit_test, name='submit_test'),

    # Новые маршруты для лиг, магазина, достижений
    path('league/', views.league_table, name='league'),
    path('shop/', views.shop, name='shop'),
    path('shop/buy/<int:item_id>/', views.purchase_item, name='purchase_item'),
    path('shop/use/<int:inventory_id>/', views.use_item, name='use_item'),
    path('achievements/', views.achievements_list, name='achievements'),

    path('api/check-answer/', views.check_answer_ajax, name='check_answer_ajax'),
# НОВЫЙ МАРШРУТ ДЛЯ РЕЙТИНГА КУРСА (страница кланов)
    path('clan-leaderboard/', views.clan_leaderboard, name='clan_leaderboard'),
    #новые для тестов крч
    path('become-author/', views.become_author, name='become_author'),
    path('create-test/', views.create_test, name='create_test'),
    path('my-tests/', views.my_tests, name='my_tests'),
    path('public-tests/', views.public_tests, name='public_tests'),
    path('take-custom-test/<int:test_id>/', views.take_custom_test, name='take_custom_test'),
    path('course-leaderboard/<slug:slug>/', views.course_leaderboard, name='course_leaderboard'),
    path('become-author/', views.become_author, name='become_author'),
    path('course/<int:course_id>/add-lesson/', views.add_lesson, name='add_lesson'),
    path('create-course/', views.create_course, name='create_course'),
    path('course/<int:course_id>/edit/', views.edit_course, name='edit_course'),
    path('edit-custom-test/<int:test_id>/', views.edit_custom_test, name='edit_custom_test'),
    path('lesson/<int:lesson_id>/edit/', views.edit_lesson, name='edit_lesson'),
    path('delete-custom-test/<int:test_id>/', views.delete_custom_test, name='delete_custom_test'),
    path('delete-course/<int:course_id>/', views.delete_course, name='delete_course'),
    path('delete-lesson-test/<int:lesson_id>/', views.delete_lesson_test, name='delete_lesson_test'),
    path('course/<int:course_id>/attach-test/', views.attach_test_to_course, name='attach_test_to_course'),
    path('course/<slug:slug>/add-review/', views.add_course_review, name='add_course_review'),
    # TTS для озвучки (если будете использовать)
    # path('tts/', views.tts, name='tts'),  # раскомментируйте, когда добавите функцию tts в views.py
]