# Generated by Django 2.2.6 on 2020-04-29 23:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20200424_0241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Allergies_List',
        ),
        migrations.AddField(
            model_name='customuser',
            name='dietary_preferences',
            field=djongo.models.fields.ListField(blank=True, default=list, null=True),
        ),
        migrations.AlterField(
            model_name='customrecipe',
            name='calories_per_serving',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='customrecipe',
            name='number_of_servings',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='customrecipe',
            name='recipe_name',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='diary',
            name='custom_recipe',
            field=models.ManyToManyField(blank=True, to='users.CustomRecipe'),
        ),
        migrations.AlterField(
            model_name='diary',
            name='meal_type',
            field=models.CharField(choices=[(1, 'Breakfast'), (2, 'Lunch'), (3, 'Dinner'), (4, 'Snack')], max_length=8),
        ),
        migrations.AlterField(
            model_name='diary',
            name='timestamp_entry',
            field=models.DateTimeField(max_length=16, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='profile_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='rating',
            name='recipe_id',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.CASCADE, to='users.Meals', to_field='recipe_id'),
        ),
    ]
