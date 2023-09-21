#  The Thai Calendar Algorithm

## Introduction

I'm an Australian monk in the Thai Maha Nikaya order. I don't speak Thai nor do I have contact with people knowledgeable about how the lunar calendar works. Instead I approached this project starting with the dates provided in this icalendar file:

http://splendidmoons.github.io/ical/mahanikaya.ical 

This covers the years 2010 to 2030 and includes moon days and special holidays such as Vesak Day. I worked backward to get the algorithms for generating the dates and this document describes them.

## A typical season

There are three seasons in a year: hot, cold and rainy.

While there are variations that will be discussed below, most seasons follow this pattern:

- There are 8 uposathas, moon day observances for the full and new moons. These can vary slightly from the astronomical cycle.
- The uposathas are separated by either 14 or 15 days.
- The fourteen day uposathas occur on the third and seventh uposatha, always a new moon.

We describe the 14/15 day pattern of a normal season like so:

`(15, 15, 14, 15, 15, 15, 14, 15)`

Given the last day of the previous season we generate a season's worth of uposathas by adding 15 or 14 days to the previous. The first season is a special case where we supply the day before the season begins. In all other cases we just need the date of the last uposatha in the previous season. 

The moon phases alternate between full and moon, always starting with a new moon.

### Half moon observance

The half moon days occur on both waxing and waning moon phases, always 8 days after the previous uposatha, whether it is a 15 or 14 day uposatha. This sequence can be used:

`(8, 15, 15, 14, 15, 15, 15, 14)`

### A long hot season

To keep the lunar calendar in synch with the solar calendar a hot season is declared to be long, by adding two extra uposathas of 15 days. This gives us the following sequence to be added to the day before the season:

`(15, 15, 14, 15, 15, 15, 14, 15, 15, 15)`

Half moon days follow along:

`(8, 15, 15, 14, 15, 15, 15, 14, 15, 15)`

The long hot month years are stored internally as a list:

`[2010, 2012, 2015, 2018, 2021, 2023, 2026, 2029]`

This will need to be updated to deal with dates beyond 2030.

### Extra days

Given that the actual orbit of the moon is 29.53 days, the calendar still gets out of synch. When declared, a day is added to the 7th uposatha of the hot season. 

Uposatha durations:

`(15, 15, 14, 15, 15, 15, 15, 15)`

Half moon durations:

`(8, 15, 15, 14, 15, 15, 15, 15)`

Again these are stored in a list:

`[2016, 2020, 2025, 2030]`

Note that these do not coincide with extra month years. As far as I know they are mutually exclusive.

## Calendar bounds

At some point we don't know when the extra month and extra days are as they have not been announced (or this package is out of date!) Thus we start the generation with the day before a given season in a given year and end with a given season and year. For simplicity we only generate complete seasons.

## Holidays

We observe 4 holidays in this package: vesak, magha puja, asalha puja and the pavarana. These are calculated like so:

- The Pavarana is always the 6th uposatha in the rainy season.
- Vesak day occurs on the 4th uposatha in the hot season, or the 6th uposatha if the hot season is long.
- Asalha puja occurs on the 8th uposatha of the hot season, or the 10th in a long hot season.
- Magha puja is on the 6th uposatha of the cold season, or the 8th if the following hot season is long.