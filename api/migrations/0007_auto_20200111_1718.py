# Generated by Django 3.0.2 on 2020-01-11 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_equipment_teams'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maintenanceticket',
            name='issue_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='maintenanceticket',
            name='resolution_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]