import streamlit as st

from data import generate_metrics
from model import AnomalyDetector
from optimizer import generate_recommendation


# --------------------------------
# Page Configuration
# --------------------------------

st.set_page_config(
    page_title="AI Cloud Infrastructure Optimizer",
    page_icon="☁️",
    layout="wide"
)


# --------------------------------
# Header
# --------------------------------

st.title(
    "☁️ AI Cloud Infrastructure Optimizer"
)

st.write(
    "ML-powered infrastructure monitoring, "
    "anomaly detection and resource optimization."
)


# --------------------------------
# Generate Infrastructure Data
# --------------------------------

df = generate_metrics(1000)


# --------------------------------
# Train Anomaly Detection Model
# --------------------------------

detector = AnomalyDetector()

detector.train(df)

results = detector.predict(df)


# --------------------------------
# Dashboard Metrics
# --------------------------------

st.subheader("📊 Infrastructure Overview")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Average CPU",
    f"{df['cpu_usage'].mean():.1f}%"
)

col2.metric(
    "Average Memory",
    f"{df['memory_usage'].mean():.1f}%"
)

col3.metric(
    "Average Latency",
    f"{df['latency'].mean():.0f} ms"
)

anomalies = (
    results["status"] == "Anomaly"
).sum()

col4.metric(
    "Detected Anomalies",
    anomalies
)


st.divider()


# --------------------------------
# Infrastructure Charts
# --------------------------------

st.subheader("📈 Resource Utilization")

st.line_chart(
    df[
        [
            "cpu_usage",
            "memory_usage"
        ]
    ]
)


st.subheader("🌐 Application Latency")

st.line_chart(
    df[
        ["latency"]
    ]
)


# --------------------------------
# Anomaly Detection
# --------------------------------

st.subheader("🚨 Detected Infrastructure Anomalies")

anomaly_data = results[
    results["status"] == "Anomaly"
]

if len(anomaly_data) > 0:

    st.dataframe(
        anomaly_data.head(20),
        use_container_width=True
    )

else:

    st.success(
        "No infrastructure anomalies detected."
    )


# --------------------------------
# Optimization Engine
# --------------------------------

st.divider()

st.subheader(
    "⚙️ Infrastructure Optimization"
)

col1, col2, col3 = st.columns(3)

with col1:

    cpu = st.slider(
        "CPU Usage (%)",
        min_value=0,
        max_value=100,
        value=55
    )

with col2:

    memory = st.slider(
        "Memory Usage (%)",
        min_value=0,
        max_value=100,
        value=60
    )

with col3:

    latency = st.slider(
        "Latency (ms)",
        min_value=0,
        max_value=1000,
        value=200
    )


if st.button(
    "🔍 Generate Recommendation"
):

    result = generate_recommendation(
        cpu,
        memory,
        latency
    )

    st.subheader(
        f"Recommended Action: {result['action']}"
    )

    st.write(
        f"**Severity:** {result['severity']}"
    )

    st.write(
        f"**Reason:** {result['reason']}"
    )
