echo "Downloading single-line analysis model from Hugging Face..."

python - <<EOF
if not os.path.exists("models/"):
    os.makedirs("models/")

from huggingface_hub import hf_hub_download
import os
if os.path.exists("models/sla.h5"):
    print("Model already exists. Skipping download.")
else:
    hf_hub_download(
        repo_id="Kwankhao/oct-srf-classification",
        filename="sla.h5",
        local_dir="models"
    )
EOF

echo "Download single-line analysis model complete!"