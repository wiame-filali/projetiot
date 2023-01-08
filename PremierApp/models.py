from django.core.mail import send_mail
from django.db import models
class Dht(models.Model):
    temp = models.FloatField(null=True)
    dt = models.DateTimeField(auto_now_add=True,null=True)
    def str(self):
        return "temperature= "+str(self.temp)

    def save(self, *args, **kwargs):
           if self.temp <2 :
                  # envoie du msg sur telegram
                  import telepot
                  token = '5871488790:AAFk46-VcQWONtcDc0pMnaSG5IUzLeRjq8c'
                  rece_id = 5706872166
                  bot = telepot.Bot(token)
                  bot.sendMessage(rece_id, 'depassement temp')
                  print(bot.sendMessage(rece_id, 'temperature critique .'))
                  # envoie du mail
                  send_mail(
                         'température dépasse la normale,' + str(self.temp),
                         'anomalie dans la machine',
                         'wiame.filali@ump.ac.ma',
                         ['wiamefilali014@gmail.com'],
                         fail_silently=False)
           return super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
           if self.temp >8:
                  # envoie du msg sur telegram
                  import telepot
                  token = '5871488790:AAFk46-VcQWONtcDc0pMnaSG5IUzLeRjq8c'
                  rece_id = 5706872166
                  bot = telepot.Bot(token)
                  bot.sendMessage(rece_id, 'depassement temp')
                  print(bot.sendMessage(rece_id, 'temperature critique .'))
                  # envoie du mail
                  send_mail(
                         'température dépasse la normale,' + str(self.temp),
                         'anomalie dans la machine',
                         'wiame.filali@ump.ac.ma',
                         ['wiamefilali014@gmail.com'],
                         fail_silently=False)
           return super().save(*args, **kwargs)
