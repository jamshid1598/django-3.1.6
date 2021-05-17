from django.db import models
from django.utils.translation import ugettext_lazy as _
import datetime
from django.utils import timezone
# Create your models here.



class Question(models.Model):
    question = models.CharField(_("Question"), max_length=500)
    created_at = models.DateTimeField(_("Created Date"), auto_now_add=True)

    def __str__(self):
        return self.question
    
    def was_created_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(minutes=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question_choice')
    choice_text = models.CharField(_("Choice Text"), max_length=500)
    vote = models.IntegerField(_("Votes"), default=0)

    def __str__(self):
        return str(self.pk) + " | " +self.question.question

