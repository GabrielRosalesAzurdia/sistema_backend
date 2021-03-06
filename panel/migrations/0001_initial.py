# Generated by Django 3.1.7 on 2021-04-07 23:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('teachers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('clase', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.class')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.grade')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('classes', models.ManyToManyField(to='panel.Class')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.grade')),
            ],
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=250)),
                ('description', models.CharField(default='', max_length=250)),
                ('score', models.IntegerField()),
                ('classes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.class')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.student')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.unit')),
            ],
        ),
        migrations.AddField(
            model_name='class',
            name='grades',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='panel.grade'),
        ),
        migrations.AddField(
            model_name='class',
            name='teachers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
