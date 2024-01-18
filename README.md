# Graph Streams and Visualisations

This Example repo of streaming data into a graph database Memgraph is in support of the Blog post article from [El Maestro](https://maestro.project-ma.com/posts/redpanda-memgraph-streaming-visualisation)

Data Analytics/Processing for streaming, batch data sources and sinks

- Redpanda
- Memgraph
- graphlytic

## Starting the Data Stack
The following will start Redpanda, Redpanda Console(Web), Memgraph Platform(includes Lab, Mage and core DB)
```
docker compose up redpanda rp-console memgraph-platform graphlytic
```
If you don't want to start all the above, just include the ones you want after docker compose up command. 

## Memgraph Streaming Ingestion
The Redpanda data producer is a python app(./rp-producer/producer-movielens.py) and the Consumer of this topic is Memgraph Streams (natively built into Memgraph)

Example Dataset used is from https://gdespot.medium.com/analyzing-real-time-movie-reviews-with-redpanda-and-memgraph-46704998e974

### Adding Transformation Modules for Memgraph Streams to a running Docker Container of Memgraph

1. Import Movielens Python Transform module into running Memgraph Query modules Docker container
```
docker cp ./datasets/movielens/movielens-transform.py <CONTAINER_ID>:/usr/lib/memgraph/query_modules/movielens.py
```

2. Login to Memgraph Lab </> "Query execution" and run the following Cypher query to load the transformation module;
```
CALL mg.load("movielens");
```

3. Within Memgraph Lab click on "Query Modules", Refresh and you should find the movielens module listed. 

4. Create Memgraph Stream to connect to Consume Redpanda Topic.  Using the following Cypher Query, copy it into the Memgraph Lab Query Execution console;
```
CREATE KAFKA STREAM movie_ratings 
TOPICS ratings 
TRANSFORM movielens.rating 
BOOTSTRAP_SERVERS 'redpanda:9092';
```

5. Within the Memgraph Lab web console, click on Streams and start the movielens stream consumer.
6. Turn on the data hose with;
```
python3 ./rp-producer/producer-movielens.py
```
