# Generated by Django 4.0.1 on 2022-02-04 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=140)),
                ('role', models.CharField(max_length=140)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.images')),
            ],
        ),
    ]