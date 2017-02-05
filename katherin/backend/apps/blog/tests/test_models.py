from loremipsum import generate_paragraph, generate_sentence
from django.test import TestCase

from apps.blog.models import Article, Comment, Activity
from apps.users.models import CustomUser


class TestBlogModels(TestCase):

    def setUp(self):
        CustomUser.objects.create_user(
            email='jack777@test.com',
            first_name='Jack',
            last_name='Nicholson',
            password='123123123',
        )
        for i in range(3):
            Article.objects.create(
                title='Test Article%d' % i,
                content=generate_paragraph()[2],
                author=CustomUser.objects.first()
            )

    def test_article_creation(self):
        article = Article.objects.create(
            title='Test Article',
            content=generate_paragraph()[2],
            author=CustomUser.objects.first()
        )
        print(article)

        self.assertEqual(4, Article.objects.count())

    def test_add_comments_to_article(self):
        NUM_OF_COMMENTS = 5
        article = Article.objects.last()

        for i in range(NUM_OF_COMMENTS):
            article.comments.create(
                content=generate_sentence()[2],
                author=CustomUser.objects.first()
            )

        self.assertEqual(NUM_OF_COMMENTS, Comment.objects.count())
        self.assertEqual(NUM_OF_COMMENTS, article.comments.count())

    def test_add_activities_to_article(self):
        NUM_OF_ACTIVITIES = 10
        article = Article.objects.last()

        for i in range(NUM_OF_ACTIVITIES):
            activity_type = Activity.ACTIVITY_TYPES[i % 4][0]
            article.activities.create(
                activity_type=activity_type,
                author=CustomUser.objects.first()
            )

        self.assertEqual(10, article.activities.count())
        self.assertEqual(10, Activity.objects.count())
        self.assertEqual(3, article.activities.filter(activity_type=Activity.FAVORITE).count())
        self.assertEqual(3, article.activities.filter(activity_type=Activity.LIKE).count())
        self.assertEqual(2, article.activities.filter(activity_type=Activity.UP_VOTE).count())
        self.assertEqual(2, article.activities.filter(activity_type=Activity.DOWN_VOTE).count())
