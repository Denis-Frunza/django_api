from django.contrib import admin

from .models import Movie, CustomUser


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = (
        "title",
        "genre",
        "year",
        "created_date",
        "updated_date",
    )
    list_display = (
        "title",
        "genre",
        "year",
        "created_date",
        "updated_date",
    )
    readonly_fields = (
        "created_date",
        "updated_date",
    )


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    fields = (
        "email",
        "username",
        "date_joined",
    )
    list_display = (
        "email",
        "username",
        "date_joined",
    )
    readonly_fields = (
        "date_joined",
    )
