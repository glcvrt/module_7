from rest_framework import status
from rest_framework.test import APITestCase

from materials.models import Lesson, Course, Subscription
from users.models import User


class LessonTestCase(APITestCase):
    def setUp(self):
        self.lesson = Lesson.objects.create(
            title='test1',
            description_lesson='test1'
        )

    def test_get_list_lesson(self):
        response = self.client.get('education:lesson-list')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_lesson(self):
        data = {
            'title': 'test2',
            'description_lesson': 'test2',
            'link': 'http:youtube.com'
        }
        response = self.client.post('materials:lesson-create', data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_lesson(self):
        data = {
            'title': 'test3',
            'description_lesson': 'test2',
            'link': 'http:youtube.com'
        }
        response = self.client.put('materials:lesson-update', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lesson(self):
        response = self.client.delete('materials:lesson-delete')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscribeTestCase(APITestCase):
    def setUp(self):
        self.course = Course.objects.create(
            name='test12',
            description='test12',

        )

        self.user = User.objects.create(
            email='i1472138@yandex.ru',
            username='Admin',
            is_staff=True,
            is_superuser=True
        )
        self.user.save()
        self.client.force_authenticate(user=self.user)
        self.subscription = Subscription.objects.create(
            user=self.user,
            is_subscribed=True,
            course=self.course
        )

    def test_create_subscription(self):
        data = {
            'course': self.course.pk
        }

        response = self.client.post('materials:subscription', data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def test_subscription_list(self):
        response = self.client.get('materials:subscription')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update(self):
        data = {
            'course': self.course.pk
        }
        response = self.client.put('materials:subscription', data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_subscription(self):
        response = self.client.delete('materials:subscription')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
