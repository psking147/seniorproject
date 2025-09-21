from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbclc', '0004_auto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='line',
            name='name',
        ),
    ]