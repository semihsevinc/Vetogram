from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),

            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('animal_type', models.CharField(choices=[('DOG', 'Dog'), ('CAT', 'Cat'), ('BIRD', 'Bird'), ('FISH', 'Fish'), ('OTHER', 'Other')], default='OTHER', max_length=20)),
                ('breed', models.CharField(max_length=200)),
                ('pet_name', models.CharField(max_length=30)),
                ('age', models.IntegerField(default=0)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manager.owner')),
            ],
        ),
    ]
