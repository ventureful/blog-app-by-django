from django.test import SimpleTestCase
from django.urls import resolve, reverse

from ..views import AboutPageView, HomePageView


class HomePageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("home")
        self.response = self.client.get(url)

    def test_home_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_home_page_template(self):
        self.assertTemplateUsed(self.response, "pages/home.html")

    def test_home_page_contains_correct_html(self):
        self.assertContains(self.response, "Welcome to the Blog API")

    def test_home_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Not the Homepage")

    def test_homepage_url_resolves_homepageview(self):
        view = resolve("/")
        self.assertEqual(
            view.func.__name__,
            HomePageView.as_view().__name__,
        )


class AboutPageTests(SimpleTestCase):
    def setUp(self):
        url = reverse("about")
        self.response = self.client.get(url)

    def test_about_page_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_about_page_template(self):
        self.assertTemplateUsed(self.response, "pages/about.html")

    def test_about_page_contains_correct_html(self):
        self.assertContains(self.response, "About page")

    def test_about_page_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Not the About page")

    def test_aboutpage_url_resolves_aboutpageview(self):
        view = resolve("/about/")
        self.assertEqual(
            view.func.__name__,
            AboutPageView.as_view().__name__,
        )
