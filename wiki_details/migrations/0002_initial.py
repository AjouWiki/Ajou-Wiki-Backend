# Generated by Django 4.2.1 on 2023-05-22 15:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wiki_details", "0001_initial"),
        ("wikis", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="wiki_detail",
            name="wiki_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wiki_detail",
                to="wikis.wiki",
            ),
        ),
    ]