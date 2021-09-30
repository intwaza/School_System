# Generated by Django 3.2.4 on 2021-09-30 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trainer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='age',
            field=models.PositiveSmallIntegerField(default='SOME STRING'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='bio',
            field=models.TextField(default='SOME STRING', max_length=700),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='contract',
            field=models.FileField(default='SOME STRING', upload_to='documents/'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='date_hired',
            field=models.DateField(default='SOME STRING'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='email_address',
            field=models.EmailField(default='SOME STRING', max_length=254),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='first_name',
            field=models.CharField(default='SOME STRING', max_length=12),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='gender',
            field=models.CharField(choices=[('1', 'Female'), ('2', 'male'), ('3', 'none')], default='SOME STRING', max_length=8),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='last_name',
            field=models.CharField(default='SOME STRING', max_length=12),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='phone_number',
            field=models.CharField(default='SOME STRING', max_length=12),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='profile',
            field=models.ImageField(default='SOME STRING', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='trainer',
            name='salary',
            field=models.PositiveBigIntegerField(default='SOME STRING'),
        ),
    ]
