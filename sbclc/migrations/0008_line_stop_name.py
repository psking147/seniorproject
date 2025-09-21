from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbclc', '0007_linecongestion_stopcongestion'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='stop_name',
            field=models.CharField(default='a', max_length=30),
        ),
    ]