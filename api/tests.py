from django.test import TestCase, Client

class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_view_renders_correct_template(self):
        response = self.client.get('/login/')
        self.assertTemplateUsed(response, 'pages/login/login_page.html')
