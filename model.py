from sklearn.ensemble import IsolationForest


FEATURES = [
    "cpu_usage",
    "memory_usage",
    "network_usage",
    "request_rate",
    "latency"
]


class AnomalyDetector:

    def __init__(self, contamination=0.05):

        self.model = IsolationForest(
            contamination=contamination,
            random_state=42,
            n_estimators=150
        )

    def train(self, dataframe):

        self.model.fit(
            dataframe[FEATURES]
        )

        return self

    def predict(self, dataframe):

        dataframe = dataframe.copy()

        predictions = self.model.predict(
            dataframe[FEATURES]
        )

        scores = self.model.decision_function(
            dataframe[FEATURES]
        )

        dataframe["status"] = [
            "Anomaly" if value == -1
            else "Normal"
            for value in predictions
        ]

        dataframe["anomaly_score"] = scores

        return dataframe
