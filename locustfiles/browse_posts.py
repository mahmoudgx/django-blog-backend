from locust import HttpUser, task


class WebsiteUser(HttpUser):
    @task
    def view_posts(self):
        self.client.get('/api/posts/', name='/api/posts/')