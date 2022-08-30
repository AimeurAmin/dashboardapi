from django.db import models

# CITY
class City(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  city_name = models.TextField(
    max_length=64,
    null=False,
    blank=False
  )

  city_code = models.TextField(
    max_length=3,
    null=False,
    blank=False,
    default=''
  )

  class Meta:
    db_table = 'Cities'

# USER
class User(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  first_name = models.TextField(
    max_length=250,
    null=False,
    blank=False
  )

  last_name = models.TextField(
    max_length=250,
    null=False,
    blank=False
  )

  phone = models.TextField(
    max_length=14,
    null=False,
    blank=False
  )

  email = models.TextField(
    max_length=250,
    null=False,
    blank=False
  )

  city = models.ForeignKey(
    City, 
    related_name='users',
    on_delete=models.CASCADE
  )

  creation_date = models.DateTimeField(
    auto_now_add=True,
    null=False,
    blank=False
  )

  class Meta:
    db_table = 'Users'

# DOMAINES
class Domain(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  domain_name = models.TextField(
    max_length=250,
    null=False,
    blank=False
  )

  class Meta:
    db_table = 'Domains'

# COMMENT
class Comment(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  comment = models.TextField(
    max_length=500,
    null=False,
    blank=False
  )

  domain = models.ForeignKey(
    Domain, 
    on_delete=models.CASCADE
  )

  user = models.ForeignKey(
    User,
    on_delete=models.CASCADE
  )
  
  calssification = models.TextField(
    max_length=25,
    null=False,
    blank=False
  )

  creation_date = models.DateTimeField(
    auto_now_add=True,
    null=False,
    blank=False
  )

  class Meta:
    db_table = 'Comments'

# QUESTOION
class Question(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  question = models.TextField(
    max_length=500,
    null=False,
    blank=False
  )

  domain = models.ForeignKey(
    Domain, 
    on_delete=models.CASCADE
  )

  class Meta:
    db_table = 'Questions'

# ANSWER
class Answer(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  answer = models.TextField(
    max_length=500,
    null=False,
    blank=False
  )

  question = models.ForeignKey(
    Question,
    related_name='answers',
    on_delete=models.CASCADE
  )

  class Meta:
    db_table = 'Answers'

# USER_ANSWER
class UserAnswer(models.Model):
  id = models.AutoField(
    primary_key=True
  )

  answer = models.ForeignKey(
    Answer, 
    on_delete=models.CASCADE
  )

  user = models.ForeignKey(
    User, 
    on_delete=models.CASCADE
  )

  comment = models.ForeignKey(
    Comment, 
    on_delete=models.CASCADE
  )

  creation_date = models.DateTimeField(
    auto_now_add=True,
    null=False,
    blank=False
  )

  class Meta:
    db_table = 'UsersAnswers'
