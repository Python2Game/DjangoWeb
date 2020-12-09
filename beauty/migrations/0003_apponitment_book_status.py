

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0002_auto_20200520_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Apponitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date1', models.DateField(null=True)),
                ('time1', models.TimeField(null=True)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beauty.Customer')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beauty.Servise')),
                ('status', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beauty.Book_status')),
            ],
        ),
    ]
