from django.db import models



class DomainEntity(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


def get_upload_path(instance, filename):
    return f"{instance.image_name}/{filename}"


class StoreImage(DomainEntity):
    image_name = models.CharField(max_length=100)
    photo = models.URLField(max_length=2048)
