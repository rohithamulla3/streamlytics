-- Hourly sentiment trends
SELECT
  DATE_TRUNC('HOUR', created_at) AS hour,
  sentiment,
  COUNT(*) AS tweet_count
FROM tweets_sentiment
GROUP BY 1, 2
ORDER BY hour DESC;
