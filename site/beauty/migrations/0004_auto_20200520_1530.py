
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beauty', '0003_apponitment_book_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_Paid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('paid', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='apponitment',
            name='paid',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beauty.Booking_Paid'),
        ),
    ]