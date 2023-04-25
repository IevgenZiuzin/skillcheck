# Generated by Django 4.2 on 2023-04-15 20:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_rename_cat_quiz_category'),
        ('stats', '0002_completion_max_score_completion_total'),
    ]

    operations = [
        migrations.AddField(
            model_name='completion',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='completions', to='quiz.quizcategory'),
            preserve_default=False,
        ),
    ]