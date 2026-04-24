import asyncio

try:
    asyncio.set_event_loop(asyncio.new_event_loop())
except:
    pass

import pyshark
import pickle

# -----------------------------
# LOAD TRAINED MODEL
# -----------------------------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("✅ Model Loaded. Starting Real-Time Detection...\n")

# -----------------------------
# SELECT NETWORK INTERFACE
# -----------------------------
capture = pyshark.LiveCapture(interface='Wi-Fi')  # change if needed

previous_time = None

# -----------------------------
# START CAPTURE
# -----------------------------
for packet in capture.sniff_continuously(packet_count=50):

    try:
        # -----------------------------
        # EXTRACT FEATURES
        # -----------------------------
        current_time = float(packet.sniff_timestamp)
        length = int(packet.length)
        protocol = packet.highest_layer

        # -----------------------------
        # ENCODE PROTOCOL
        # -----------------------------
        protocol_map = {
            'TCP': 0,
            'UDP': 1,
            'ICMP': 2,
            'ICMPV6': 2
        }

        protocol_encoded = protocol_map.get(protocol, 3)

        # -----------------------------
        # TIME DIFFERENCE
        # -----------------------------
        if previous_time is None:
            time_diff = 0
        else:
            time_diff = current_time - previous_time

        previous_time = current_time

        # -----------------------------
        # PACKET RATE
        # -----------------------------
        packet_rate = 1 / (time_diff + 0.0001)

        # -----------------------------
        # PREPARE INPUT
        # -----------------------------
        import pandas as pd
        features = pd.DataFrame([[current_time, protocol_encoded, length, time_diff, packet_rate]],
        columns=['Time', 'Protocol', 'Length', 'Time_diff', 'Packet_rate'])

        # -----------------------------
        # PREDICTION
        # -----------------------------
        prediction = model.predict(features)
        if packet_rate > 50:
            prediction[0] = 1

        # -----------------------------
        # OUTPUT
        # -----------------------------
        if prediction[0] == 1:
            print("[ALERT] 🚨 Intrusion Detected!")
        else:
            print("[INFO] Normal Traffic")

    except Exception as e:
        continue