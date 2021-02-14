from django.db import models

# Create your models here.

class ItemCategory(models.Model):
    categoryName = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return str(self.categoryName)


class Items(models.Model):
    itemCategory = models.ForeignKey(ItemCategory, related_name="item_category", on_delete=models.CASCADE)
    itemName = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('itemCategory', 'itemName',)

    def __str__(self):
        return str(itemName) + " : " + str(self.itemCategory)