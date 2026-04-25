from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WorpData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('beginsnelheid_km_per_h', models.FloatField()),
                ('beginhoek_graden', models.FloatField()),
                ('vliegtijd_seconden', models.FloatField()),
                ('vliegafstand_meter', models.FloatField()),
            ],
        ),
    ]