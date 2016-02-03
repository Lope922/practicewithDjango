from django.db import models
from django.utils import timezone

# Create your models here.


# just named this GUIS for now because this is just a test
class GUI(models.Model):
    #
    choices = (("H", "Home"),("A", "Away"))
    # date of the game
    game_day = models.DateField()
    # teams name
    opponent = models.TextField()
    # indicate wheater it is a home or away game
    venue = models.CharField(choices=choices, max_length=1)



    # insert the game data
    def insert_game_data(self):
        self.game_day = timezone.now()
        self.save()

    # this is equivalent to string method , but is being used as an example from online. May need to be converted to
    #DateTime
    def __str__(self):
        return self.game_day