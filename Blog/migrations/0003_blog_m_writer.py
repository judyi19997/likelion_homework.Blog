# Generated by Django 3.0.6 on 2020-07-15 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_blog_m_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_m',
            name='writer',
            field=models.CharField(max_length=100, null=True),
        ),
    ]