# Generated by Django 5.1.4 on 2025-05-08 16:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("organizations", "0004_alter_organization_name"),
        ("views", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="view",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="view",
            constraint=models.UniqueConstraint(
                condition=models.Q(("privacy", "public")),
                fields=("name", "organization"),
                name="unique_public_view_name_per_org",
            ),
        ),
        migrations.AddConstraint(
            model_name="view",
            constraint=models.UniqueConstraint(
                condition=models.Q(("privacy", "private")),
                fields=("name", "organization", "user"),
                name="unique_private_view_name_per_user_org",
            ),
        ),
    ]
