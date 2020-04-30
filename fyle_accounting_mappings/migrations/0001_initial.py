# Generated by Django 3.0.3 on 2020-03-24 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workspaces', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DestinationAttribute',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('attribute_type', models.CharField(help_text='Type of expense attribute', max_length=255)),
                ('display_name', models.CharField(help_text='Display name of attribute', max_length=255)),
                ('value', models.CharField(help_text='Value of expense attribute', max_length=255)),
                ('destination_id', models.CharField(help_text='Destination ID', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated at datetime')),
                ('workspace', models.ForeignKey(help_text='Reference to Workspace model', on_delete=django.db.models.deletion.PROTECT, to='workspaces.Workspace')),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseAttribute',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('attribute_type', models.CharField(help_text='Type of expense attribute', max_length=255)),
                ('display_name', models.CharField(help_text='Display name of expense attribute', max_length=255)),
                ('value', models.CharField(help_text='Value of expense attribute', max_length=255)),
                ('source_id', models.CharField(help_text='Fyle ID', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated at datetime')),
                ('workspace', models.ForeignKey(help_text='Reference to Workspace model', on_delete=django.db.models.deletion.PROTECT, to='workspaces.Workspace')),
            ],
        ),
        migrations.CreateModel(
            name='MappingSetting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source_field', models.CharField(help_text='Source mapping field', max_length=255)),
                ('destination_field', models.CharField(help_text='Destination mapping field', max_length=40, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated at datetime')),
                ('workspace', models.ForeignKey(help_text='Reference to Workspace model', on_delete=django.db.models.deletion.PROTECT, to='workspaces.Workspace')),
            ],
            options={
                'unique_together': {('source_field', 'workspace_id'), ('destination_field', 'workspace_id')},
            },
        ),
        migrations.CreateModel(
            name='Mapping',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('source_type', models.CharField(help_text='Fyle Enum', max_length=255)),
                ('destination_type', models.CharField(help_text='Destination Enum', max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Created at datetime')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Updated at datetime')),
                ('destination', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='fyle_accounting_mappings.DestinationAttribute')),
                ('source', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='fyle_accounting_mappings.ExpenseAttribute')),
                ('workspace', models.ForeignKey(help_text='Reference to Workspace model', on_delete=django.db.models.deletion.PROTECT, to='workspaces.Workspace')),
            ],
            options={
                'unique_together': {('source_type', 'source', 'workspace')},
            },
        ),
    ]