CREATE OR REPLACE TABLE workspace.default.weather_gold
USING DELTA
AS
SELECT *
FROM delta.`/Volumes/workspace/default/gold/weather_analytics`;