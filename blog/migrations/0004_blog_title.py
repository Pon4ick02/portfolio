# Generated by Django 4.2.16 on 2025-02-15 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_blog_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='Без названия', max_length=200),
            preserve_default=False,
        ),
    ]
