from pydantic import BaseModel
from fastapi import APIRouter

from datetime import date

import json


class Person(BaseModel):
    iin: str


route = APIRouter()


@ route.get('/people/{iin}', status_code=200)
async def get_age(iin: str):
    with open('person.json', 'r') as f:
        data = json.load(f)

    if data['iin'] == iin:
        return {"iin": iin, "age": data['age']}


@ route.post('/people/', status_code=201)
async def post_age(pers: Person):
    iin_date = iter(pers.iin[0:6])
    # splitted_iin = [i + next(iin_date) for i in iin_date]
    splitted_iin = []
    for i in iin_date:
        try:
            splitted_iin.append(i + next(iin_date))
        except StopIteration:
            pass

    iin_2_int = list(map(int, splitted_iin))
    curr_date = list(map(int, date.today().strftime("%y %m %d").split(' ')))

    try:
        curr_dt = date(curr_date[0], curr_date[1], curr_date[2])
        iin_dt = date(iin_2_int[0], iin_2_int[1], iin_2_int[2])
    except ValueError: pass

    # age = ((curr_dt - iin_dt) /
    #        365).days if iin_dt < curr_dt else str(date.today().year - iin_2_int[0])[2:]

    if iin_dt < curr_dt:
        age = ((curr_dt - iin_dt) / 365.25).days
    else:
        age = str(date.today().year - iin_2_int[0])[2:]

    data = {**pers.dict(), "age": int(age)}

    with open('person.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    return data if len(pers.iin) == 12 else 'Invalid IIN: length > 12!'
