import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from bertopic import BERTopic
from pathlib import Path
import plotly.io as pio

# ---------- Run SBERT + BERTopic ----------
def generate_embeddings_and_topics(
    input_path="data/df_processed.pkl",
    output_path="data/sbert_data.pkl",
    model_save_path="bertopic_model",
    model_name="all-MiniLM-L6-v2"   
    #"all-mpnet-base-v2" may also be a good choice but is more memory intensive
):
    print(f"📂 Loading {input_path}")
    df = pd.read_pickle(input_path)

    print(f"🔍 Loading SentenceTransformer model: {model_name}")
    model = SentenceTransformer(model_name)

    print("🧠 Encoding comments...")
    sentences = df["processed_comment"].tolist()
    embeddings = model.encode(sentences, show_progress_bar=True, batch_size=512)
    df["embedding"] = embeddings.tolist()

    print("🧩 Running BERTopic...")
    topic_model = BERTopic(embedding_model=model, verbose=True)
    topics, probs = topic_model.fit_transform(sentences, embeddings)

    print("🔖 Mapping topics and probabilities...")
    df["topic"] = topics
    df["probability"] = probs
    
    topic_info = topic_model.get_topic_info()
    
    topic_labels = topic_info.set_index("Topic")["Name"].to_dict()
    df["topic_label"] = df["topic"].map(topic_labels)

    print(f"💾 Saving results to {output_path}")
    df.to_pickle(output_path)

    print(f"📦 Saving BERTopic model to {model_save_path}")
    topic_model.save(model_save_path)

    print("✅ All done!")

# ---------- Main ----------
if __name__ == "__main__":
    df, topic_model = generate_embeddings_and_topics()

    # Create output directory
    Path("outputs").mkdir(exist_ok=True)

    print("📊 Generating BERTopic visualizations...")

    # 1. Interactive 2D Topic Scatter Plot (UMAP-based) — HTML only
    fig = topic_model.visualize_topics()
    fig.write_html("outputs/topic_map.html")

    # 2. Top Topics Bar Chart — PNG
    fig = topic_model.visualize_barchart(top_n_topics=20)
    fig.write_image("outputs/topic_barchart.png", format="png", scale=2)

    # 3. Topic Similarity Heatmap — PNG
    fig = topic_model.visualize_heatmap()
    fig.write_image("outputs/topic_heatmap.png", format="png", scale=2)

    