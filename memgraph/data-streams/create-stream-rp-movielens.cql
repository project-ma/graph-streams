CREATE KAFKA STREAM movie_ratings 
TOPICS ratings 
TRANSFORM movielens.rating 
BOOTSTRAP_SERVERS 'redpanda:9092';