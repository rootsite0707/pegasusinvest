from django.db import models


class Bank(models.Model):
    name = models.CharField(max_length=60, default='')
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    nmb = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    contribution = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Вклад'
        verbose_name_plural = 'Вклады'

    def save(self, *args, **kwargs):
        contribution = self.price
        self.contribution = contribution
        self.total_price = int(self.nmb) * self.contribution

        super(Bank, self).save(*args, **kwargs)



