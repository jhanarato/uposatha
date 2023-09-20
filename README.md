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

### Calendar Configuration

In order to generate the calendar some information is needed. This includes:

- Start date
- Start season
- End Season
- End year
- Years with extra month added.
- Years with extra day added.

This information is specified in the `configure` module and is available via the calendar object:

```python
>>> cal.config.start_date
datetime.date(2010, 2, 28)
>>> cal.config.extra_day_years
[2016, 2020, 2025, 2030]
```

**NB: If anyone knows this information beyond 2030, let me know!**

### Acknowledgements

The starting point of this project was the [Forest Sangha calendars](https://forestsangha.org/community/calendars/year_planners/). They in turn provide a link to an `ical` file for importing into various calendar applications. The code for generating this file is available at the [splendidmoons github page](https://github.com/splendidmoons). This is written in Go and does not provide a licence so I began by parsing the file in python. You can see the code at https://github.com/jhanarato/uposatha-ical

Leveraging that, I went back and wrote the uposatha package from scratch, testing with the data from `uposatha-ical`. Thanks to the Forest Sangha and the Splendid Moons developers!