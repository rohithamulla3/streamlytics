-- Sentiment by region
SELECT
  user_location,
  sentiment,
  COUNT(*) AS count
FROM tweets_sentiment
WHERE user_location IS NOT NULL
GROUP BY user_location, sentiment
ORDER BY count DESC;
