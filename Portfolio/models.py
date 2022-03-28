from django.db import models

# Create your models here.


class Message(models.Model):
    e_mail = models.EmailField(verbose_name='E-mail')
    first_name = models.CharField(verbose_name='Nome', max_length=30)
    last_name = models.CharField(verbose_name='Sobrenome', max_length=30)
    phone_number = models.CharField(verbose_name='Telefone', max_length=15)
    liurl = models.CharField(verbose_name='Usuário do LinkedIn', max_length=20)
    subject = models.CharField(verbose_name='Assunto', max_length=255)
    message = models.TextField(verbose_name='Mensagem', max_length=512)

    def __str__(self) -> str:
        return ('Mensagem de ' + self.first_name + ' ' + self.last_name + ' - ' + self.e_mail)
