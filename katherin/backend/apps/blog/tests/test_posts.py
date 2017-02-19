from loremipsum import generate_paragraph, generate_sentence
from django.test import TestCase

from apps.blog.models import Post, Comment, Activity
from apps.users.models import CustomUser


class TestPosts(TestCase):

    def setUp(self):
        CustomUser.objects.create_user(
            email='jack777@test.com',
            first_name='Jack',
            last_name='Nicholson',
            password='123123123',
        )
        for i in range(3):
            Post.objects.create(
                content=generate_paragraph()[2],
                author=CustomUser.objects.first()
            )

    def test_post_creation(self):
        Post.objects.create(
            content=generate_paragraph()[2],
            author=CustomUser.objects.first()
        )

        self.assertEqual(4, Post.objects.count())

    def test_add_comments_to_post(self):
        NUM_OF_COMMENTS = 5
        post = Post.objects.last()

        for i in range(NUM_OF_COMMENTS):
            post.comments.create(
                content=generate_sentence()[2],
                author=CustomUser.objects.first()
            )

        self.assertEqual(NUM_OF_COMMENTS, Comment.objects.count())
        self.assertEqual(NUM_OF_COMMENTS, post.comments.count())

    def test_add_activities_to_post(self):
        NUM_OF_ACTIVITIES = 10
        post = Post.objects.last()

        for i in range(NUM_OF_ACTIVITIES):
            activity_type = Activity.ACTIVITY_TYPES[i % 4][0]
            post.activities.create(
                activity_type=activity_type,
                author=CustomUser.objects.first()
            )

        self.assertEqual(10, post.activities.count())
        self.assertEqual(10, Activity.objects.count())
        self.assertEqual(3, post.activities.filter(activity_type=Activity.FAVORITE).count())
        self.assertEqual(3, post.activities.filter(activity_type=Activity.LIKE).count())
        self.assertEqual(2, post.activities.filter(activity_type=Activity.UP_VOTE).count())
        self.assertEqual(2, post.activities.filter(activity_type=Activity.DOWN_VOTE).count())

    def test_abstract_base_add_comment(self):
        post = Post.objects.first()
        author = CustomUser.objects.first()

        self.assertEqual(0, post.comments.count())

        for i in range(3):
            post.add_comment(
                'sample comment text %d' % i,
                author,
                status=Comment.PUBLISHED
            )

        self.assertEqual(3, post.comments.count())
        self.assertEqual(3, post.comments.filter(status=Comment.PUBLISHED).count())

    def test_abstract_base_add_activity(self):
        post = Post.objects.first()
        author = CustomUser.objects.first()

        self.assertEqual(0, post.activities.count())

        for i in range(10):
            post.add_activity(
                activity_type=Activity.ACTIVITY_TYPES[i % 4][0],
                author=author
            )

        self.assertEqual(10, post.activities.count())
        self.assertEqual(10, Activity.objects.count())
        self.assertEqual(3, post.activities.filter(activity_type=Activity.FAVORITE).count())
        self.assertEqual(3, post.activities.filter(activity_type=Activity.LIKE).count())
        self.assertEqual(2, post.activities.filter(activity_type=Activity.UP_VOTE).count())
        self.assertEqual(2, post.activities.filter(activity_type=Activity.DOWN_VOTE).count())
