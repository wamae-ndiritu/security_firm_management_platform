# Generated by Django 5.2 on 2025-05-06 13:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_hiring', '0010_alter_user_options_alter_user_managers_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Service',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='email',
        ),
        migrations.RemoveField(
            model_name='applicant',
            name='name',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='email',
        ),
        migrations.RemoveField(
            model_name='jobapplication',
            name='name',
        ),
        migrations.AddField(
            model_name='applicant',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='job',
            name='security_company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job_hiring.securitycompany'),
        ),
        migrations.AddField(
            model_name='jobapplication',
            name='applicant',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='job_hiring.applicant'),
        ),
        migrations.AddField(
            model_name='securitycompany',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='company_logos/'),
        ),
        migrations.AddField(
            model_name='securitycompany',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='securitycompany',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
