from locust import HttpUser, task, between

from server import loadClubs, loadCompetitions


class ProjectPerfTest(HttpUser):
    wait_time = between(1, 5)
    competition = loadCompetitions()[0]
    club = loadClubs()[0]

    def on_start(self):
        self.client.get("/")
        self.client.post("/showSummary", data={"email": self.club["email"]})

    @task
    def get_booking_competition(self):
        self.client.get(f"/book/{self.competition['name']}/{self.club['name']}")

    @task
    def post_booking_competition(self):
        self.client.post(
            "/purchasePlaces",
            data={
                "places": 0,
                "club": self.club["name"],
                "competition": self.competition["name"],
            },
        )

    @task
    def display_points(self):
        self.client.get("/displayPoints", name="display_points_clubs")

    def on_stop(self):
        self.client.get("/logout")
