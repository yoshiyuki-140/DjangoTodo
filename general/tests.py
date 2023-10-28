from django.test import TestCase

# Create your tests here.

class TopPageTest(TestCase):
    def test_shouldReturn200StatusCode(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)
