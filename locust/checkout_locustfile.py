from locust import HttpUser, task, between

class CheckoutUser(HttpUser):
    wait_time = between(0.1, 0.3)  # Much faster users

    @task
    def checkout(self):
        self.client.get("/checkout", name="Checkout Page")
