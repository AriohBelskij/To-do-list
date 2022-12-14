# Generated by Django 4.1.3 on 2022-11-14 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("tag", models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.CharField(max_length=100)),
                ("started_at", models.DateTimeField(auto_now_add=True)),
                ("deadline", models.DateTimeField(blank=True, null=True)),
                ("done", models.BooleanField(blank=True, default=False, null=True)),
                ("tags", models.ManyToManyField(related_name="tags", to="task.tag")),
            ],
            options={
                "ordering": ["done", "-started_at"],
            },
        ),
    ]
