from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sbclc', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='create_data',
            new_name='create_date',
        ),
    ]