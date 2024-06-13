from django.test import TestCase
from django.urls import reverse
from http import HTTPStatus
from django.contrib.auth import get_user_model


class FormTestCase(TestCase):
    
    def setUp(self) -> None:
        self.data = {
            'username': 'Nikita',
            'password1': 'ZXCPUDGE228',
            'password2': 'ZXCPUDGE228',
            'email': 'bletigri@gmail.com',
            'birthday': '2009-02-01',
            'telephone_number': "+7 (919) 972-81-50",
            'tag_user': 'first',
            'first_name': 'Nikita',
            'last_name': 'Grigorev'
        }
    
    def test_one(self):
        path = reverse('user:regist')
        response = self.client.get(path)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'User/register.html')
    
    def test_form_post(self):
        user_model = get_user_model()
        
        path = reverse('user:regist')
        response = self.client.post(path=path, data=self.data)
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertRedirects(response, reverse('user:login'))
        self.assertTrue(user_model.objects.filter(tag_user=self.data['tag_user']).exists())