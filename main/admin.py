from django.contrib import admin
from .models import Course, Lesson, Community, Achievement, Profile, Question, LessonCompletion
from .models import League, LeagueInstance, UserLeagueMembership, SeasonalEvent, AchievementLevel, AchievementProgress, ShopItem, UserInventory, UserSubscription, DailyRewardLog, CustomTest, CustomQuestion, CustomTestResult
from .models import CourseReview
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'total_points', 'coins', 'tulips', 'level', 'streak_days', 'lessons_completed', 'is_author', 'created_at']
    search_fields = ['user__username', 'user__email']
    list_editable = ['coins', 'tulips', 'is_author']

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'level', 'price', 'is_free', 'status', 'lessons_count', 'is_official', 'created_at']
    list_filter = ['status', 'level', 'is_free', 'is_official', 'created_at']
    search_fields = ['title', 'description', 'author__username']
    list_editable = ['status', 'is_official']
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = (
        ('Основная информация', {'fields': ('title', 'slug', 'description', 'short_description', 'author')}),
        ('Детали курса', {'fields': ('level', 'duration_weeks', 'lessons_count')}),
        ('Цена и акции', {'fields': ('price', 'old_price', 'is_free'), 'classes': ('collapse',)}),
        ('Визуальное оформление', {'fields': ('icon_class', 'badge_text', 'badge_color'), 'classes': ('collapse',)}),
        ('Статус и даты', {'fields': ('status', 'order', 'published_at', 'is_official'), 'classes': ('collapse',)}),
    )

    actions = ['make_published', 'make_draft', 'make_official', 'make_unofficial']

    def make_published(self, request, queryset):
        from django.utils import timezone
        queryset.update(status='published', published_at=timezone.now())
    make_published.short_description = 'Опубликовать выбранные курсы'

    def make_draft(self, request, queryset):
        queryset.update(status='draft')
    make_draft.short_description = 'Снять с публикации'

    def make_official(self, request, queryset):
        queryset.update(is_official=True)
    make_official.short_description = 'Сделать официальными'

    def make_unofficial(self, request, queryset):
        queryset.update(is_official=False)
    make_unofficial.short_description = 'Сделать народными'


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title', 'course', 'section', 'order', 'duration_minutes', 'is_free_preview']
    list_filter = ['course', 'section', 'is_free_preview']
    search_fields = ['title', 'content']
    list_editable = ['order', 'duration_minutes']


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ['name', 'member_count', 'is_active', 'order']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    list_editable = ['order', 'member_count', 'is_active']


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ['name', 'points', 'is_active']
    list_filter = ['is_active']
    search_fields = ['name', 'description']
    list_editable = ['points', 'is_active']


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'lesson', 'correct_option']
    list_filter = ['lesson']
    search_fields = ['text']


@admin.register(LessonCompletion)
class LessonCompletionAdmin(admin.ModelAdmin):
    list_display = ['user', 'lesson', 'test_score', 'completed_at']
    list_filter = ['lesson__course', 'lesson']
    search_fields = ['user__username', 'lesson__title']


@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = ['tatar_name', 'rank_order', 'min_users', 'max_users']


@admin.register(LeagueInstance)
class LeagueInstanceAdmin(admin.ModelAdmin):
    list_display = ['league', 'instance_number', 'current_week_start']


@admin.register(UserLeagueMembership)
class UserLeagueMembershipAdmin(admin.ModelAdmin):
    list_display = ['user', 'league_instance', 'week_start', 'weekly_xp', 'rank']


@admin.register(SeasonalEvent)
class SeasonalEventAdmin(admin.ModelAdmin):
    list_display = ['tatar_name', 'start_date', 'end_date', 'is_active']


@admin.register(AchievementLevel)
class AchievementLevelAdmin(admin.ModelAdmin):
    list_display = ['achievement', 'level', 'required_value', 'points_reward', 'coin_reward']


@admin.register(AchievementProgress)
class AchievementProgressAdmin(admin.ModelAdmin):
    list_display = ['user', 'achievement', 'current_value', 'current_level']


@admin.register(ShopItem)
class ShopItemAdmin(admin.ModelAdmin):
    list_display = ['tatar_name', 'item_type', 'price_coins', 'price_tulips', 'is_active']


@admin.register(UserInventory)
class UserInventoryAdmin(admin.ModelAdmin):
    list_display = ['user', 'item', 'quantity', 'expires_at', 'used_at']


@admin.register(UserSubscription)
class UserSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['user', 'start_date', 'end_date', 'is_active']


@admin.register(DailyRewardLog)
class DailyRewardLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'claimed', 'streak_bonus']


@admin.register(CustomTest)
class CustomTestAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'difficulty', 'created_at']
    list_filter = ['status', 'difficulty']
    search_fields = ['title', 'author__username']
    list_editable = ['status']


@admin.register(CustomQuestion)
class CustomQuestionAdmin(admin.ModelAdmin):
    list_display = ['test', 'text', 'correct_option']


@admin.register(CustomTestResult)
class CustomTestResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'test', 'score', 'earned_coins', 'completed_at']
    list_filter = ['test', 'user']

@admin.register(CourseReview)
class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'course', 'rating', 'is_approved', 'created_at']
    list_filter = ['is_approved', 'course', 'rating']
    search_fields = ['user__username', 'course__title', 'comment']
    list_editable = ['is_approved']
    list_display_links = ['user']