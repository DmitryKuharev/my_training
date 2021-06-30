import peewee

database_proxy = peewee.Proxy()


class DataWeather(peewee.Model):
    weather = peewee.CharField()
    date = peewee.CharField()
    t_day = peewee.CharField()
    t_night = peewee.CharField()

    class Meta:
        database = database_proxy
