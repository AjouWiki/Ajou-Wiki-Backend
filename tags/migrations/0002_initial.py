# Generated by Django 4.2.1 on 2023-05-22 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("tags", "0001_initial"),
        ("wikis", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="tag",
            name="wiki_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tag",
                to="wikis.wiki",
            ),
        ),
    ]
