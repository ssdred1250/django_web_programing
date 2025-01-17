# Generated by Django 2.2.6 on 2019-11-01 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('register_date', models.DateTimeField(verbose_name='Register Date')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtuber_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('review_text', models.CharField(max_length=300)),
                ('register_date', models.DateTimeField(verbose_name='Register Date')),
                ('delete_yn', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('youtuber_id', models.IntegerField()),
                ('register_date', models.DateTimeField(verbose_name='Register Date')),
            ],
        ),
        migrations.CreateModel(
            name='Youtuber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('profile_img', models.URLField(verbose_name='Profile Image')),
                ('video_url', models.URLField(verbose_name='Video URL')),
                ('description', models.CharField(max_length=500)),
                ('view', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(verbose_name='Create Date')),
            ],
        ),
        migrations.CreateModel(
            name='YoutuberCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtuber_id', models.IntegerField()),
                ('category_id', models.IntegerField()),
                ('register_date', models.DateTimeField(verbose_name='Register Date')),
            ],
        ),
    ]
