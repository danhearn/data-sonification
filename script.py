from pythonosc import udp_client
import pandas as pd
import semantic
import os
from ast import literal_eval
import random
import time

# Import dataset
df = pd.read_csv('tanc-etan_system-dataset.csv')
df['Countries'] = df['Countries'].apply(lambda x: literal_eval(x) if pd.notnull(x) else x)

df['Vectors'] = semantic.make_vectors(4)

client = udp_client.SimpleUDPClient("127.0.0.1", 9000)
client2 = udp_client.SimpleUDPClient("127.0.0.1", 10000)

# SEMANTIC
while True:
    random_index = random.randint(0, len(df) - 1)
    row = df.iloc[random_index]
    print(f"Processing index: {random_index}, Country: {row['Countries']} Label and vectors: {[row['Label']] + list(row['Vectors'])}")
    vectors = [float(value) for value in row['Vectors']]
    if row['Label'] == 1:
        client.send_message("/positive", vectors)
    else: 
         client2.send_message("/negative", vectors)
    # SEMANTIC
    
   #client.send_message("/vectors", [int(row['Label'])] + vectors)

    time.sleep(5)  # Add a three-second delay
