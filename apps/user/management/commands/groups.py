import logging

from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from apps.user.models import Permissions

PERMISSIONS = ['Admin', 'Read Only']


def create_basic_permissions_group():
    group, created = Group.objects.get_or_create(name="Basic Permissions")
    content_type = ContentType.objects.get_for_model(Permissions)
    all_permission = Permission.objects.exclude(content_type=content_type)
    for permission in all_permission:
        group.permissions.add(permission)


def create_group():
    for permission in PERMISSIONS:
        group, created = Group.objects.get_or_create(name=permission)
        content_type = ContentType.objects.get_for_model(Permissions)
        permission, created = Permission.objects.get_or_create(codename=permission.replace(' ', '_').lower(),
                                                               name=permission, content_type=content_type)
        group.permissions.add(permission)


class Command(BaseCommand):
    help = 'Creates read only default permission groups for users'

    def handle(self, *args, **options):
        create_basic_permissions_group()
        create_group()

