-- 1. Deduplicate and calculate overall conversion rate
WITH clean_data AS (
    SELECT DISTINCT user_id, device, "group", converted
    FROM checkout_ab_test_data
)
SELECT 
    "group",
    COUNT(user_id) AS total_visitors,
    SUM(converted) AS total_conversions,
    ROUND(AVG(converted) * 100, 2) AS conversion_rate_pct
FROM clean_data
GROUP BY "group";


-- 2. Segment Analysis: Exposing the Mobile Drop-off
WITH clean_data AS (
    SELECT DISTINCT user_id, device, "group", converted
    FROM checkout_ab_test_data
)
SELECT 
    device,
    "group",
    COUNT(user_id) AS total_visitors,
    SUM(converted) AS total_conversions,
    ROUND(AVG(converted) * 100, 2) AS conversion_rate_pct
FROM clean_data
GROUP BY device, "group"
ORDER BY device, "group";
