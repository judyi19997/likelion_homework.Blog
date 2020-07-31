# Generated by Django 3.0.6 on 2020-08-01 03:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Blog', '0003_blog_m_writer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_m',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField()),
                ('body', models.TextField()),
                ('commentAuthor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('commentBlog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog.Blog_m')),
            ],
        ),
    ]
