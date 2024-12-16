from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    wait_time = between(1,5)

    @task(4)
    def view_posts(self):
        print('view posts')
        self.client.get('/api/posts/', name='/api/posts/')
    @task(2)
    def add_comment(self):
        print('add comment')
        self.client.post(
            f'/api/posts/9/comments/', name='api/posts/9/comments/',
            json={
    "name": "mahmoud",
    "email": "mahmoud@mahmoudibrahim.me",
    "content": "test"
}
        )