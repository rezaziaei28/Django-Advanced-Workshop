from locust import HttpUser, task, between

class BlogUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        response = self.client.post("/accounts/api/v1/jwt/create/", json={
            "email": "rezaziaei28@gmail.com",
            "password": "Aa@123456"        
        })
        if response.status_code == 200:
            token = response.json().get("access")
            self.client.headers.update({"Authorization": f"Bearer {token}"})
        else:
            print("Login failed for Locust user!")

    @task
    def get_posts(self):
        self.client.get("/blog/api/v1/post/")