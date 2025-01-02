# Generated by Django 4.2.3 on 2024-12-22 12:31

from django.db import migrations, models
import django.utils.timezone
import uuid


PROCEDURE_SQL = """
CREATE PROCEDURE variable_upsert(
    p_name    text,
    p_value   jsonb
)
LANGUAGE plpgsql
AS $$
BEGIN
    -- add a new Variable or update an existing one
    INSERT INTO opencve_variables (id, created_at, updated_at, name, value)
    VALUES(uuid_generate_v4(), NOW(), NOW(), p_name, p_value)
    ON CONFLICT (name) DO
    UPDATE SET
      updated_at = NOW(),
      value = EXCLUDED.value;
END;
$$;
"""

PROCEDURE_REVERSE_SQL = """
DROP PROCEDURE variable_upsert(
    p_name    text,
    p_value   jsonb
);
"""


class Migration(migrations.Migration):

    dependencies = [
        ("cves", "0002_add_cve_upsert_procedure"),
    ]

    operations = [
        migrations.CreateModel(
            name="Variable",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now
                    ),
                ),
                ("name", models.CharField(max_length=256, unique=True)),
                ("value", models.JSONField(default=dict)),
            ],
            options={
                "db_table": "opencve_variables",
            },
        ),
        migrations.RunSQL(sql=PROCEDURE_SQL, reverse_sql=PROCEDURE_REVERSE_SQL),
    ]