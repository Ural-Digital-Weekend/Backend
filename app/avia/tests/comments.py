from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase

from authorization.tests.helpers import create_test_user, get_auth_api_client
from avia.models import Airport, Comment


class CommentsTest(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super(CommentsTest, cls).setUpClass()
        call_command('refill_avia_data')
        airport = Airport.objects.order_by('name').first()

        user = User.objects.create_user(
            username="another_test_user",
            email="another@user.com",
            password="somepass123",
        )

        Comment.objects.bulk_create([
            Comment(
                comment=f"Комментарий №{i}",
                user_id=user.id,
                airport_id=airport.id
            )
            for i in range(3)])

    def setUp(self) -> None:
        user_data = create_test_user()
        self.user = User.objects.get(username=user_data['username'])
        self.client = get_auth_api_client(user_data['username'], user_data['password'])
        self.airport = Airport.objects.order_by('name').first()
        self.routes = {
            'list': f'/api/airports/{self.airport.id}/comments',
            'detail': '/api/airports/comments/{comment_id}'
        }

    def test_comment_list_by_airport(self):
        qs = Comment.objects.filter(airport_id=self.airport.id)
        comment = qs.first()
        comment_count = qs.count()

        response = self.client.get(self.routes['list'])

        self.assertEqual(200, response.status_code)
        self.assertEqual(comment_count, response.data.get('count'))
        self.assertEqual(comment.id, response.data.get('results')[0]['id'])
        self.assertEqual(comment.comment, response.data.get('results')[0]['comment'])

    def test_create_comment(self):
        response = self.client.post(self.routes['list'], data={
            'comment': "Хороший аэропорт"
        })
        self.assertEqual(201, response.status_code)

    def test_edit_comment(self):
        comment = Comment.objects.create(
            comment="Хороший аэропорт",
            user_id=self.user.id,
            airport_id=self.airport.id,
        )

        response = self.client.put(self.routes['detail'].format(comment_id=comment.id), data={
            'comment': "Плохой аэропорт"
        })

        self.assertEqual(200, response.status_code)

    def test_cant_edit_another_user_commment(self):
        comment = Comment.objects.exclude(user_id=self.user.id).first()

        response = self.client.put(self.routes['detail'].format(comment_id=comment.id), data={
            'comment': "Плохой аэропорт"
        })

        self.assertEqual(403, response.status_code)

    def test_delete_comment(self):
        comment = Comment.objects.create(
            comment="Хороший аэропорт",
            user_id=self.user.id,
            airport_id=self.airport.id,
        )

        response = self.client.delete(self.routes['detail'].format(comment_id=comment.id))

        self.assertEqual(204, response.status_code)
        self.assertEqual(0, Comment.objects.filter(id=comment.id).count())

    def test_cant_delete_another_user_comment(self):
        comment = Comment.objects.exclude(user_id=self.user.id).first()

        response = self.client.delete(self.routes['detail'].format(comment_id=comment.id))

        self.assertEqual(403, response.status_code)
