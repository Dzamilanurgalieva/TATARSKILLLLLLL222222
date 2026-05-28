from django import forms
from .models import Course, Lesson

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'short_description', 'level', 'price', 'is_free', 'icon_class',
                  'duration_weeks', 'lessons_count']

class LessonForm(forms.ModelForm):
    class Meta:
        model = Lesson
        fields = ['title', 'section', 'content', 'video_url', 'duration_minutes', 'is_free_preview', 'test']

class DragonRatingWidget(forms.RadioSelect):
    template_name = 'dragon_rating_widget.html'
from .models import CourseReview

class CourseReviewForm(forms.ModelForm):
    class Meta:
        model = CourseReview
        fields = ['comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Поделитесь впечатлениями о курсе...'}),
        }