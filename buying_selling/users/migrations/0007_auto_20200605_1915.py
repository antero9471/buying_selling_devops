# Generated by Django 2.2.10 on 2020-06-05 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_auto_20200605_1909"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="hostel",
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="users.Hostel"),
        ),
    ]
