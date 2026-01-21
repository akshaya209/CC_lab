from locust import HttpUser, task, between

class EventsUser(HttpUser):
    wait_time = between(1, 2)

    def on_start(self):
        self.headers = {
            "Accept": "application/json",
            "User-Agent": "LocustLoadTest"
        }

    @task(3)
    def view_events_page_1(self):
        self.client.get(
            "/events?page=1&limit=20",
            headers=self.headers,
            name="/events"
        )

    @task(1)
    def view_events_page_2(self):
        self.client.get(
            "/events?page=2&limit=20",
            headers=self.headers,
            name="/events"
        )
