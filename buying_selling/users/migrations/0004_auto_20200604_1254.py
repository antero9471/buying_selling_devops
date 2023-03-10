# Generated by Django 2.2.10 on 2020-06-04 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_auto_20200605_1857"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="hostel",
            field=models.CharField(
                choices=[
                    ("A", "Hostel A"),
                    ("B", "Hostel B"),
                    ("C", "Hostel C"),
                    ("D", "Hostel D"),
                    ("E", "Hostel E"),
                    ("F", "Hostel F"),
                    ("G", "Hostel G"),
                    ("H", "Hostel H"),
                    ("I", "Hostel I"),
                    ("J", "Hostel J"),
                    ("K", "Hostel K"),
                    ("L", "Hostel L"),
                    ("M", "Hostel M"),
                    ("FRD", "Hostel FRD"),
                    ("FRE", "Hostel FRE"),
                ],
                default="H",
                max_length=1,
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="profile",
            name="isHosteler",
            field=models.BooleanField(default=True),
        ),
    ]
