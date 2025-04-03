-- Top keywords by sentiment (hypothetical view)
SELECT
  sentiment,
  keyword,
  COUNT(*) AS frequency
FROM tweets_sentiment_keywords
GROUP BY sentiment, keyword
ORDER BY sentiment, frequency DESC;
