# Generated by Django 3.2.4 on 2021-08-12 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='nationality_id',
        ),
        migrations.AddField(
            model_name='student',
            name='course_name',
            field=models.CharField(max_length=18, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='date_of_enrollment',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='district',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email_address',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('1', 'Female'), ('2', 'male'), ('3', 'none')], max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='guardian_name',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='languages',
            field=models.CharField(choices=[('1', 'English'), ('2', 'Kinyarwanda'), ('3', 'French'), ('4', 'Kiswahili'), ('5', 'Luganda')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='laptop_number',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='medical_report',
            field=models.FileField(null=True, upload_to='documents/'),
        ),
        migrations.AddField(
            model_name='student',
            name='nationality',
            field=models.CharField(choices=[('1', 'Rwandan'), ('2', 'Kenyan'), ('3', 'Ugandan'), ('4', 'South Sudanese'), ('5', 'Sudanese')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='phone_number',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='profile',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='last_name',
            field=models.CharField(max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='national_id',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
