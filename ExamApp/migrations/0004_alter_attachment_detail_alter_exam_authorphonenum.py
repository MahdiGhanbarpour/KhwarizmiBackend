# Generated by Django 5.0.1 on 2024-02-08 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ExamApp", "0003_attachment_option_question_alter_exam_authorphonenum"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attachment",
            name="detail",
            field=models.TextField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name="exam",
            name="authorPhoneNum",
            field=models.CharField(blank=True, default=None, max_length=11, null=True),
        ),
    ]
