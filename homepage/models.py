from django.db import models


# This model is used for the backend purpose from when user can change the frontend view
class Internet(models.Model):
    name = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2083)


class Homepage(models.Model):
    name = models.CharField(max_length=255)
    details = models.CharField(max_length=255)
    image_url = models.CharField(max_length=2083)
    link_to = models.CharField(max_length=255)


class News(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=2083)
    image_url = models.CharField(max_length=2083)
    news_link = models.CharField(max_length=255)


class Intro(models.Model) :
    intro_menu = models.CharField(max_length=20)
    intro_description = models.CharField(max_length=2083)
    intro_link = models.CharField(max_length=255)