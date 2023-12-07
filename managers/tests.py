from django.test import TestCase
from managers.models import Managers, Roles
from django.contrib.auth import get_user_model


class ManagersTestCase(TestCase):
    def test_create_managers(self):
        name = "test"
        roles = Roles.objects.create(name=name)
        manager = Managers.objects.create(
            email="test@example.com",
            first_name="test",
            last_name="test",
            staff_id="test",
            phone_number="test",
        )
        # set roles
        manager.roles.add(roles)
        manager.save()

        self.assertEqual(Managers.objects.count(), 1)

    # def test_create_mangers_with_invalid_email(self):
    #     name = "test"
    #     roles = Roles.objects.create(name=name)
    #     manager = Managers.objects.create(
    #         email=None,
    #         first_name="test",
    #         last_name="test",
    #         staff_id="test",
    #         phone_number="test",
    #     )
    #     # set roles
    #     manager.roles.add(roles)
    #     manager.save()
    #
    #     self.assertEqual(Managers.objects.count(), 0)
    #     self.assertRaises(ValueError)

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(

            email="test@example.com", password="test")

        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)
