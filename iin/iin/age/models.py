from django.db import models
from datetime import date


# Create your models here.
class Person(models.Model):
    iin = models.CharField(max_length=12, unique=True)

    @property
    def age(self) -> int:
        iin_date = iter(self.iin[0:6])
        # splitted_iin = [i + next(iin_date) for i in iin_date]
        splitted_iin = []
        for i in iin_date:
            splitted_iin.append(i + next(iin_date))

        iin_2_int = list(map(int, splitted_iin))
        curr_date = list(map(int, date.today().strftime("%y %m %d").split(' ')))

        try:
            curr_dt = date(curr_date[0], curr_date[1], curr_date[2])
            iin_dt = date(iin_2_int[0], iin_2_int[1], iin_2_int[2])
        except ValueError as VE:
            return {"400": 'Invalid Data!'}
        # age = ((curr_dt - iin_dt) /
        #        365).days if iin_dt < curr_dt else str(date.today().year - iin_2_int[0])[2:]

        if iin_dt < curr_dt:
            age = ((curr_dt - iin_dt) / 365.25).days
        else:
            age = str(date.today().year - iin_2_int[0])[2:]

        # data = {**pers.dict(), "age": int(age)}
        return int(age)
