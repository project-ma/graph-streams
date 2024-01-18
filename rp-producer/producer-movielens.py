from kafka import KafkaProducer   # Uses kafka-python from Apache >>> pip install kafka-python
# from kafka.errors import KafkaError
import csv
import json
import time

DATA_RATINGS = "./datasets/movielens/ratings.csv"
DATA_MOVIES = "./datasets/movielens/movies.csv"

stream_delay = 1
topic = "ratings"
movies_dict = {}

producer = KafkaProducer(
    bootstrap_servers = "localhost:19092"
)
   
def on_success(metadata):
  print(f"Message produced to topic '{metadata.topic}' at offset {metadata.offset}")

def on_error(e):
  print(f"Error sending message: {e}")

# Generate data from raw csv dataset
def generate():
    while True:
        with open(DATA_RATINGS) as file:
            csvReader = csv.DictReader(file)
            for rows in csvReader:
                data = {
                    'userId': rows['userId'],
                    'movie': movies_dict[rows['movieId']],
                    'rating': rows['rating'],
                    'timestamp': rows['timestamp'],
                }
                yield data

# Kafka/Redpanda Producer
def main():
    with open(DATA_MOVIES) as file:
        csvReader = csv.DictReader(file)
        for rows in csvReader:
            movieId = rows['movieId']
            movies_dict[movieId] = {
                'movieId': movieId,
                'title': rows['title'],
                'genres': rows['genres'].split('|')
            }

    message = generate()
    while True:
        try:
          mssg = json.dumps(next(message)).encode('utf8')
          future = producer.send(topic, mssg)
          print(mssg)

          future.add_callback(on_success)
          future.add_errback(on_error)
          # future.get(timeout=60)

          producer.flush()
          # producer.close()
          time.sleep(stream_delay)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
