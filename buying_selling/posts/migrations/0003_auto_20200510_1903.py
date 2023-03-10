# Generated by Django 2.2.10 on 2020-05-10 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0002_auto_20200509_2359"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="age",
            field=models.CharField(
                choices=[
                    ("l6", "Less than 6 months"),
                    ("6to1", "6 months to 1 year"),
                    ("1to3", "1-3 years"),
                    ("3to5", "3-5 years"),
                    ("g5", "More than 5 years"),
                ],
                max_length=4,
            ),
        ),
        migrations.AlterField(
            model_name="post",
            name="condition",
            field=models.CharField(
                choices=[
                    ("VB", "Very Bad"),
                    ("BA", "Bad"),
                    ("G", "Good"),
                    ("BE", "Best"),
                    ("E", "Couldn't be better"),
                ],
                max_length=3,
            ),
        ),
    ]
