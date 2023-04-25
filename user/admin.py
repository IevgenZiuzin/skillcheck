from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.utils.translation import gettext_lazy as _
from .models import QuizAppUser


class QuizAppUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = QuizAppUser

    list_display = ['pk', 'username']
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "username", "password1", "password2"),
            },
        ),
    )
    fieldsets = UserAdmin.fieldsets + (
        (_('Moderation', ), {'fields': ('is_moderator',)}),
    )


admin.site.register(QuizAppUser, QuizAppUserAdmin)
