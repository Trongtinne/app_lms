# Generated by Django 5.1.1 on 2024-09-23 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_quizquestionanswer_remove_useranswer_answer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useranswer',
            name='selected_answer',
            field=models.CharField(choices=[('answertext_1', 'Answer 1'), ('answertext_2', 'Answer 2'), ('answertext_3', 'Answer 3'), ('answertext_4', 'Answer 4')], default='No answer', max_length=255),
        ),
    ]
