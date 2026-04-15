echo "Downloading temporal sequence analysis model from Hugging Face..."

python - <<EOF
from huggingface_hub import hf_hub_download
import os

if not os.path.exists("../models/"):
    print("********** Creating models directory **********")
    os.makedirs("../models/")

if os.path.exists("models/tsa_feature_extractor.h5"):
    print("Model tsa_feature_extractor already exists. Skipping download.")
else:
    hf_hub_download(
        repo_id="Kwankhao/oct-srf-classification",
        filename="tsa_feature_extractor.h5",
        local_dir="models"
)

if os.path.exists("../models/tsa_lstm.keras"):
    print("Model tsa_lstm already exists. Skipping download.")
else:
    hf_hub_download(
        repo_id="Kwankhao/oct-srf-classification",
        filename="tsa_lstm.keras",
        local_dir="models"
)

EOF

echo "Download temporal sequence analysis model complete!"