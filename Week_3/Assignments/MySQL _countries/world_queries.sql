-- 1
-- What query would you run to get all the countries that speak Slovene? Your query should 
-- return the name of the country, language and language percentage. Your query should arrange 
-- the result by language percentage in descending order. (1)
SELECT countries.name as country,languages.language as language,languages.percentage as percentage
FROM countries 
JOIN languages 
ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

-- 2
-- 2. What query would you run to display the total number of cities for each country? 
-- Your query should return the name of the country and the total number of cities. 
-- Your query should arrange the result by the number of cities in descending order. (3)
SELECT countries.name as country,COUNT(cities.name) as total_number_of_cities
FROM countries
JOIN cities
ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY total_number_of_cities DESC;

-- 3
-- 3.What query would you run to get all the cities in Mexico with a population of greater 
-- than 500,000? Your query should arrange the result by population in descending order. (1)
SELECT cities.name as city ,cities.population as population_greater_than_500000
FROM cities
JOIN countries
ON cities.country_id = countries.id
WHERE cities.population > 500000 AND countries.name = 'Mexico'
ORDER BY cities.population DESC;

-- 4
-- What query would you run to get all languages in each country with a percentage greater than 89%?
-- Your query should arrange the result by percentage in descending order. (1)
SELECT countries.name as country,languages.language as language,languages.percentage as percentage_greater_than_89
FROM languages
JOIN countries on languages.country_id = countries.id
WHERE languages.percentage > 89
ORDER BY percentage DESC;

-- 5
-- 5.What query would you run to get all the countries with Surface Area below 501 and Population greater than 100,000? (2)
SELECT * 
FROM countries
WHERE surface_area < 501 and population > 100000;

-- 6
-- What query would you run to get countries with only Constitutional Monarchy with a capital greater 
-- than 200 and a life expectancy greater than 75 years? (1)
SELECT * 
FROM countries
WHERE government_form = 'Constitutional Monarchy' 
and capital > 200 
and life_expectancy > 75;

-- 7
-- 7.What query would you run to get all the cities of Argentina inside the Buenos Aires district and 
-- have the population greater than 500, 000? The query should return the Country Name, City Name, 
-- District and Population. (2)
SELECT countries.name as country_name,cities.name as city_name,cities.district as district_name,cities.population as city_population
FROM cities
JOIN countries 
ON cities.country_id = countries.id 
WHERE cities.district = 'Buenos Aires'
AND cities.population > 500000;

-- 8
-- 8. What query would you run to summarize the number of countries in each region? The query should 
-- display the name of the region and the number of countries. Also, the query should arrange the result 
-- by the number of countries in descending order. (2)
SELECT countries.region as region,COUNT(countries.name) as number_of_countries
FROM countries
GROUP BY countries.region
ORDER BY  number_of_countries DESC;

