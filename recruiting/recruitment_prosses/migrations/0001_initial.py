# Generated by Django 5.1 on 2024-09-02 17:19

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('candidates', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'industries',
            },
        ),
        migrations.CreateModel(
            name='Recruitment_prosses',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.TextField(blank=True)),
                ('candidate_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='candidates.candidate')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stage', to='recruitment_prosses.stages')),
            ],
            options={
                'db_table': 'recruitment_prosses',
            },
        ),
    ]
