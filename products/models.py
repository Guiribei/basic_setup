from django.db import models

class Suggestion(models.Model):
	text = models.CharField(max_length=400)

	def __str__(self) -> str:
		return self.text