from django.db.models import Model, CharField, ForeignKey, CASCADE, DateTimeField


class Comment(Model):
    created = DateTimeField('дата добавления', auto_now_add=True)
    comment = CharField('Наименование', max_length=255)

    airport = ForeignKey(
        "avia.Airport",
        on_delete=CASCADE,
        related_name="comments",
        verbose_name='аэропорт',
    )

    user = ForeignKey(
        "auth.User",
        on_delete=CASCADE,
        related_name="comments",
        verbose_name='пользователь',
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return f'{self.user.email} ({self.created})'
