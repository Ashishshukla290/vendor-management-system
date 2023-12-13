# Generated by Django 4.1.4 on 2023-12-12 05:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="vendor",
            name="fulfiled_rate",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="avg_response_time",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="fullfilment_rate",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="on_time_delivery_rate",
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name="vendor",
            name="quality_rating_avg",
            field=models.FloatField(default=0),
        ),
    ]
