# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from ..models import Question, Answer

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['text', 'clue', ]

class AnswerForm(forms.ModelForm):
	
	def __init__(self, question=None, *args, **kwargs):
		form = super(AnswerForm, self).__init__(*args, **kwargs)
		if question:
			self.fields['choices'].queryset = question.choices
		return form

	class Meta:
		model = Answer
		fields = ['choices']
		widgets = {
			'choices': forms.CheckboxSelectMultiple(attrs={},),
		}