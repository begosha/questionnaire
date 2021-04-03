from django.db import models

class Poll(models.Model):
    question = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Question')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'polls'
        verbose_name = 'Poll'
        verbose_name_plural = 'Polls'

    def __str__(self):
        return self.question

class Choice(models.Model):
    text = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Choice text')
    poll = models.ForeignKey('webapp.Poll', related_name='master_poll', on_delete=models.CASCADE, verbose_name='Poll', null=False, blank=False)

    class Meta:
        db_table = 'choices'
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'

    def __str__(self):
        return "{}: {}".format(self.poll, self.text)

    