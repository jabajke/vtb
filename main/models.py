from django.db import models


class BaseModel(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        abstract = True


class GeographicPosition(BaseModel):
    class Meta:
        verbose_name = 'Географическое положение области'
        verbose_name_plural = verbose_name


class EconomicDevelopment(BaseModel):
    class Meta:
        verbose_name = 'Хозяйственное развитие и специализации'
        verbose_name_plural = verbose_name


class Export(BaseModel):
    class Meta:
        verbose_name = 'Экспорт (чем мы гордимся)'
        verbose_name_plural = verbose_name


class Nature(BaseModel):
    class Meta:
        verbose_name = 'Животный и растительный мир. Особое'
        verbose_name_plural = verbose_name


class EcologicalCondition(BaseModel):
    class Meta:
        verbose_name = 'Экологическое состояние. Заповедники и заказники.'
        verbose_name_plural = verbose_name


class FamousBiologistAndGeographist(BaseModel):
    class Meta:
        verbose_name = 'Известные биологи и географы'
        verbose_name_plural = verbose_name


class ShortHistoricalFacts(BaseModel):
    class Meta:
        verbose_name = 'Краткая историческая справка'
        verbose_name_plural = verbose_name


class MemorablePlaces(BaseModel):
    class Meta:
        verbose_name = 'Памятные места - туристические маршруты'
        verbose_name_plural = verbose_name
