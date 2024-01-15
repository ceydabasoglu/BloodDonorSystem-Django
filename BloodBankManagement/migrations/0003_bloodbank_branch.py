# Generated by Django 4.2.8 on 2024-01-13 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CreateQueryDonor', '0008_donor_branch_name'),
        ('BloodBankManagement', '0002_alter_bloodbank_donor'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodbank',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='CreateQueryDonor.bloodbankbranch'),
        ),
    ]
