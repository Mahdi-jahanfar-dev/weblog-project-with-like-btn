# Generated by Django 5.0.6 on 2024-06-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('post', models.ManyToManyField(related_name='categories', to='blog.post')),
            ],
        ),
    ]
