from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbclc', '0003_line_stop'),
    ]

    operations = [
        migrations.AddField(
            model_name='stop',
            name='index',
            field=models.PositiveIntegerField(default=111111),
        ),
        migrations.DeleteModel(
            name='Answer',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]