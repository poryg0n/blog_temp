# Generated by Django 4.2.1 on 2024-03-03 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('title_tag', models.CharField(max_length=255, null=True)),
                ('body', models.TextField()),
                ('post_date', models.DateField(auto_now_add=True)),
                ('category', models.CharField(default='Publications', max_length=100)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('attached_file', models.FileField(blank=True, null=True, upload_to='files/')),
                ('url', models.URLField(blank=True, max_length=255, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
