import requests
import pandas as pd
import time
import matplotlib.pyplot as plt

# Define your API endpoint
API_URL = "http://ece444-pra5-env.eba-kvdagzgy.us-east-2.elasticbeanstalk.com/predict"  # Replace with your actual API endpoint

test_cases = {
    "fake_news": [
        "The moon is made of hamsters",
        "Sleep is not important"
    ],
    "real_news": [
        "Bunnies make me happy", 
        "UofT makes students stressed"
    ]
}

results = []

# Function to test API performance
def test_performance(news_type, news):
    for i in range(100):
        start_time = time.time()
        response = requests.post(API_URL, data={'input_text': news})
        latency = time.time() - start_time
        results.append({'news_type': news_type, 'latency': latency})

# Run performance tests for each test case
for news_type, news_list in test_cases.items():
    for news in news_list:
        test_performance(news_type, news)

# Convert results to a DataFrame
df = pd.DataFrame(results)

# Save to CSV
df.to_csv('latency_results.csv', index=False)

# Calculate average latency
average_latency = df.groupby('news_type')['latency'].mean()
print(average_latency)

# Generate boxplot
plt.figure(figsize=(10, 6))
df.boxplot(column='latency', by='news_type')
plt.title('API Latency Boxplot')
plt.suptitle('')  # Suppress the default title
plt.xlabel('News Type')
plt.ylabel('Latency (seconds)')
plt.savefig('latency_boxplot.png')  # Save the boxplot as a file
plt.show()
