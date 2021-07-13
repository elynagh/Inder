from django.forms import ModelForm
from . import models

class UserProfileForm(ModelForm):
	class Meta:
		model = models.User
		fields = ('first_name', 'last_name', 'show_last_name', 'bio', 'idea_generator', 'collaborator')

class CreateIdeaform(ModelForm):
	class Meta:
		model = models.Idea
		fields = ('user', 'idea_title', 'text')