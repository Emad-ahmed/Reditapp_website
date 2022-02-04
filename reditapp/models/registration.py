from django.db import models


choice_department = (
    ("CSE", "CSE"),
    ("ENGLISH", "ENGLISH"),
    ("BBA", "BBA"),
    ("BANGLA", "BANGLA"),
    ("ISLAMIC STUDIES", "ISLAMIC STUDIES"),
    ("EEE", "EEE"),
)

choice_versity = (
    ("Leading", "Leading"),
    ("Dhaka University", "Dhaka University"),
    ("North South", "North South"),
    ("Rajshahi", "Rajshahi"),

)


class Registration(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    phone = models.IntegerField()
    university = models.CharField(
        max_length=200, choices=choice_versity, default="CSE")
    departMent = models.CharField(
        max_length=200, choices=choice_department, default="CSE")
    password = models.CharField(max_length=120)

    def isExists(self):
        if Registration.objects.filter(email=self.email):
            return True

        return False

    @staticmethod
    def get_user_by_email(email):
        try:
            return Registration.objects.get(email=email)
        except:
            return False
