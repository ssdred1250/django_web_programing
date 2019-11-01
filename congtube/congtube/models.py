from django.db import models


class Youtuber(models.Model):
    name = models.CharField(max_length=50)
    profile_img = models.URLField('Profile Image')
    video_url = models.URLField('Video URL')
    description = models.CharField(max_length=500)
    view = models.IntegerField(default=0)
    create_date = models.DateTimeField('Create Date')

    def __str__(self):
        return self.name


class Category(models.Model):
    category_name = models.CharField(max_length=100)
    register_date = models.DateTimeField('Register Date')

    def __str__(self):
        return self.category_name


class YoutuberCategory(models.Model):
    youtuber_id = models.IntegerField(null=False)
    category_id = models.IntegerField(null=False)
    register_date = models.DateTimeField('Register Date')


class Subscriber(models.Model):
    user_id = models.IntegerField(null=False)
    youtuber_id = models.IntegerField(null=False)
    register_date = models.DateTimeField('Register Date')


class Review(models.Model):
    youtuber_id = models.IntegerField(null=False)
    user_id = models.IntegerField(null=False)
    review_text = models.CharField(max_length=300)
    register_date = models.DateTimeField('Register Date')
    delete_yn = models.CharField(max_length=10)

    def __str__(self):
        return self.review_text