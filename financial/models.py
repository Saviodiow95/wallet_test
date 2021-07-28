from django.contrib.auth.models import User
from django.db import models


# Create your models here.
from django.db.models import Sum


class Wallet(models.Model):
    owner = models.OneToOneField(User, verbose_name='Proprietário', on_delete=models.PROTECT, related_name='wallet')

    def balance(self):
        funds = 0
        assets = Asset.objects.filter(application__wallet=self)

        for asset in assets:
            applications_amount = Application.objects.filter(
                asset=asset,
                wallet=self
            ).aggregate(balance=Sum('amount')).get('balance')
            rescues_amount = Rescue.objects.filter(
                asset=asset,
                wallet=self
            ).aggregate(balance=Sum('amount')).get('balance')
            if rescues_amount:
                funds += (applications_amount - rescues_amount)*asset.price
            else:
                funds += applications_amount * asset.price
        return funds

    def balance_asset(self):
        json = {}
        assets = Asset.objects.filter(application__wallet=self)

        for asset in assets:
            applications_amount = Application.objects.filter(
                asset=asset,
                wallet=self
            ).aggregate(balance=Sum('amount')).get('balance')
            rescues_amount = Rescue.objects.filter(
                asset=asset,
                wallet=self
            ).aggregate(balance=Sum('amount')).get('balance')
            if rescues_amount:
                json[asset.name] = (applications_amount - rescues_amount) * asset.price
            else:
                json[asset.name] = applications_amount * asset.price
        return json

    def __str__(self):
        return str(self.owner)

    class Meta:
        verbose_name = 'Carteira'
        verbose_name_plural = 'Carteiras'


class Asset(models.Model):
    CHOICES_MODALITY = (
        ('rf', 'Renda Fixa'),
        ('rv', 'Renda Variável'),
        ('cp', 'Cripto')
    )
    name = models.CharField(max_length=50, verbose_name='Nome')
    modality = models.CharField(max_length=2, choices=CHOICES_MODALITY, verbose_name='Modalidade')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Ativo'
        verbose_name_plural = 'Ativos'


class Application(models.Model):
    wallet = models.ForeignKey(Wallet, verbose_name='Carteira', on_delete=models.PROTECT, null=True, blank=True)
    asset = models.ForeignKey(Asset, verbose_name='Ativo', on_delete=models.PROTECT)
    amount = models.IntegerField(verbose_name='Quantidade')
    price_unit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço Unitário')
    date = models.DateTimeField(verbose_name='Data', auto_now_add=True, null=True, blank=True)
    ip_access = models.GenericIPAddressField(verbose_name='Endereço de IP', null=True, blank=True)

    def __str__(self):
        return 'Carteira: ' + str(self.wallet) + " Ativo: " + str(self.asset)

    class Meta:
        verbose_name = 'Aplicação'
        verbose_name_plural = 'Aplicações'


class Rescue(models.Model):
    wallet = models.ForeignKey(Wallet, verbose_name='Carteira', on_delete=models.PROTECT, null=True, blank=True)
    asset = models.ForeignKey(Asset, verbose_name='Ativo', on_delete=models.PROTECT)
    amount = models.IntegerField(verbose_name='Quantidade')
    price_unit = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Preço Unitário')
    date = models.DateTimeField(verbose_name='Data', auto_now_add=True, null=True, blank=True)
    ip_access = models.GenericIPAddressField(verbose_name='Endereço de IP', null=True, blank=True)

    class Meta:
        verbose_name = 'Resgate'
        verbose_name_plural = 'Resgates'
