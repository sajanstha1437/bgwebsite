from django.contrib import admin
from . models import Homepage, News, Intro

# Register your models here.

# admin is the module we have imported on line 1
# in this module we have class called ModelAdmin that contains all the functionality to manage admin area


class HomepageAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'link_to')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'news_link')

class IntroAdmin(admin.ModelAdmin):
    list_display = ('intro_menu', 'intro_description', 'intro_link'

                    )
admin.site.register(Homepage, HomepageAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Intro, IntroAdmin)
