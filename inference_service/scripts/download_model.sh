echo "Downloading model from Hugging Face..."

python - <<EOF
from huggingface_hub import hf_hub_download

hf_hub_download(
    repo_id="Kwankhao/oct-srf-classification",
    filename="single-line-model.h5",
    local_dir="models"
)
EOF

echo "Download complete!"