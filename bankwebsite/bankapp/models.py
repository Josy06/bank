from django.db import models


# Meet the team

class Team(models.Model):
    Name=models.CharField(max_length=300)
    Img=models.ImageField(upload_to='photo')
    Role=models.TextField()
    def __str__(self):
        return self.Name




# dropdown

class Districts(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Branch(models.Model):
    districts = models.ForeignKey(Districts, on_delete=models.CASCADE)
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=124)
    districts = models.ForeignKey(Districts, on_delete=models.SET_NULL, blank=True, null=True)
    branch = models.ForeignKey(Branch, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name