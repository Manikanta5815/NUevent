# Generated by Django 3.0.8 on 2020-07-11 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sub', '0002_auto_20200711_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('priority', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('image', models.ImageField(blank=True, default='default.jpg', upload_to='team')),
                ('url', models.CharField(default='#', max_length=255)),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sub.Title')),
            ],
        ),
    ]
