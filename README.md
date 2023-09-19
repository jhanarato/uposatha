## API for the Thai Lunar Calendar

This package provides a simple API for working with the seasons, moon days and holidays of the Thai calendar. Some use cases might include creating a printable calendar or sending a notification when there is an upcoming holiday.


### Example: Rains Retreat 2017
```py
from uposatha.calendar import Calendar
from uposatha.elements import HolidayName, SeasonName

cal = Calendar()

rainy_season = [season for season in cal.seasons
                if season.name == SeasonName.RAINY and
                season.first_day.year == 2017][0]


pavarana = [holiday for holiday in rainy_season.holidays
            if holiday.name == HolidayName.PAVARANA][0]

start = rainy_season.first_day.strftime("%d/%m/%y")
end = pavarana.uposatha.falls_on.strftime("%d/%m/%y")

print(f"Rains 2017: {start} to {end}")
```
Prints: `Rains 2017: 09/07/17 to 05/10/17`

### The Calendar Class

Most users of the package will start like so:

```python
from uposatha.calendar import Calendar
cal = Calendar()
```

This covers a specific range of dates as we need to know when years have extra months and days provided. You can see the calender range:

```python
>>> cal.start_date
datetime.date(2010, 3, 1)
>>> cal.end_date
datetime.date(2030, 11, 10)
```

When created, the calendar will generate a tuple of all seasons:

```python
>>> len(cal.seasons)
62
```

There are two helper functions:

```python
cal.next_uposatha()
cal.current_season()
```

These return instances of the classes described below.

### The Season Class

`Season` is defined in the `uposatha.elements` module:

```python
>>> season = cal.seasons[0]
>>> season.first_day
datetime.date(2010, 3, 1)
>>> season.last_day
datetime.date(2010, 7, 26)
>>> season.name
<SeasonName.HOT: 'Hot'>
>>> season.type
<SeasonType.EXTRA_MONTH: 'Extra Month'>
```

`SeasonName` and `SeasonType` are `Enum` classes defined in `uposatha.elements`.

### The Uposatha Class

Each season has a tuple of Uposathas:

```python
>>> uposatha = season.uposathas[0]
>>> uposatha.falls_on
datetime.date(2010, 3, 15)
```

You can combine this information with the season:

```python
>>> f"Uposatha {uposatha.number_in_season} of {len(season.uposathas)}"
'Uposatha 1 of 10'
```

And we have another enum - `MoonPhase`:

```python
>>> uposatha.moon_phase
<MoonPhase.NEW: 'New'>
```

### The Holiday Class

There are four holidays:

- Vesak Day
- Magha Puja
- Asalha Puja
- Pavarana Day

`Holiday` instances can be found in two ways:

```python
>>> vesak = season.holidays[0]
>>> no_holiday = uposatha.holiday
```

Note that when we created `uposatha` it was not a holiday. `no_holiday` is `None`. Holidays also have a reference to their uposatha:

```python
>>> vesak.uposatha.number_in_season
6
```

The enum `HolidayName` is in `uposatha.elements`:

```python
>>> vesak.name
<HolidayName.VESAK: 'Vesak Day'>
```

### The HalfMoon Class

There is a tuple of half moons in each season. Each is just a date and moon phase.

```python
>>> half_moon = season.half_moons[0]
>>> half_moon.moon_phase
<MoonPhase.WANING: 'Waning'>
>>> half_moon.falls_on
datetime.date(2010, 3, 8)
```