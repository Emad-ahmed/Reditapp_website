from django.db import models


choice_department = (
    ("CSE", "CSE"),
    ("ENGLISH", "ENGLISH"),
    ("BBA", "BBA"),
    ("BANGLA", "BANGLA"),
    ("ISLAMIC STUDIES", "ISLAMIC STUDIES"),
    ("EEE", "EEE"),
)

choice_semsiter = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6"),
    ("7", "7"),
    ("8", "8"),
    ("9", "9"),
    ("10", "10"),
    ("11", "11"),
    ("12", "12"),
)

class ShareFile(models.Model):
    subject_name = models.CharField(max_length=120)
    subject_code = models.CharField(max_length=120)
    departMent = models.CharField(
        max_length=200, choices=choice_department, default="CSE")
    semister = models.CharField(
        max_length=200, choices=choice_semsiter, default="1")
    question_photo = models.ImageField(upload_to='images/', blank=True)
    question_file = models.FileField(upload_to='documents/', blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)
