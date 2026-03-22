import datetime


def check_time(check_t: datetime.time, start_t: datetime.time,
               delta_dt: datetime.timedelta | None = None,
               end_t: datetime.time | None = None) -> bool:
    # Переводим всё в секунды для удобства
    def to_sec(t):
        return t.hour * 3600 + t.minute * 60 + t.second

    start_sec = to_sec(start_t)
    check_sec = to_sec(check_t)

    if end_t:
        end_sec = to_sec(end_t)
    elif delta_dt:
        # Считаем конец и нормализуем его по модулю суток (86400 секунд)
        end_sec = (start_sec + int(delta_dt.total_seconds())) % 86400
    else:
        end_sec = start_sec

    # Логика для интервалов, проходящих через полночь
    if start_sec <= end_sec:
        # Обычный случай (напр. 09:00 - 18:00)
        return start_sec <= check_sec <= end_sec
    else:
        # Случай через полночь (напр. 22:00 - 02:00)
        return check_sec >= start_sec or check_sec <= end_sec


def check_time_interval(check_dt: datetime.datetime | datetime.time,
                        start_dt: datetime.datetime | datetime.time,
                        delta_dt: datetime.timedelta | None = None,
                        end_dt: datetime.datetime | datetime.time | None = None) -> bool:
    # Если на вход пришло время, используем логику для времени
    if isinstance(start_dt, datetime.time):
        # Важно: check_dt тоже должен быть time для этой ветки
        check_t = check_dt if isinstance(check_dt, datetime.time) else check_dt.time()
        # end_dt тоже приводим к time, если он передан как datetime
        end_t = end_dt
        if isinstance(end_dt, datetime.datetime):
            end_t = end_dt.time()
        return check_time(check_t, start_dt, delta_dt, end_t)

    if isinstance(start_dt, datetime.date):
        start_dt = datetime.datetime.combine(start_dt, datetime.time.min)

    # Логика для полных дат (datetime)
    if end_dt is None:
        if delta_dt is not None:
            end_dt = start_dt + delta_dt
        else:
            end_dt = start_dt

    return start_dt <= check_dt <= end_dt


#
if __name__ == '__main__':
    a = check_time_interval(
        check_dt=datetime.datetime.now().time(),
        start_dt=datetime.time(hour=9, minute=0),
        delta_dt=datetime.timedelta(minutes=10))
    print(a)

    a = check_time_interval(
        check_dt=datetime.datetime.now(),
        start_dt=datetime.datetime(2026, 1, 23, hour=9, minute=0),
        end_dt=datetime.datetime(2026, 1, 23, hour=12, minute=20),

    )
    print(a)
