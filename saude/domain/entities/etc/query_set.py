from django.db import models


class QuerySet(models.QuerySet):
    def active(self):
        return self.filter(deleted=False)
