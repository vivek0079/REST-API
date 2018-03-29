from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APIClient
# from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


# User = get_user_model()


from postings.models import BlogPost
class BlogPostAPITestCase(APITestCase):
    def setUp(self):
        user = User(username="root_admin", email="test@gmail.com")
        password = "root_admin"
        user.set_password(password)
        user.save()
        blog_post = BlogPost.objects.create(user=user, title="New Title1", content="Random content1")
        self.client = APIClient()
        self.client.login(username=user.username, password=password)
    
    def test_single_user(self):
        user_count = User.objects.count()
        return self.assertEqual(user_count, 1)

    def test_single_post(self):
        post_count = BlogPost.objects.count()
        return self.assertEqual(post_count, 1)

    def test_get_list(self):
        data = {}
        url = reverse("api-postings:post-create")
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
 
    def test_post_item(self):
        data = {"title":"Some Title", "content":"some more content"}
        url = reverse("api-postings:post-create")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)



    def test_get_item(self):
        blog_post = BlogPost.objects.first()
        url = blog_post.get_api_url()
        data = {"title":"Some Title", "content":"some more content"}        
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # print(response.data)
 
    def test_update_item(self):
        data = {"title":"Some Title", "content":"some more content"}
        url = reverse("api-postings:post-create")
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)