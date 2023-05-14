# Generated by Django 4.0.10 on 2023-05-13 04:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wiki', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wiki_Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(default='', max_length=30)),
                ('order', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=3000, null=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user', to=settings.AUTH_USER_MODEL)),
                ('wiki_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wiki_id', to='wiki.wiki')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]