# S<sup>2</sup>DGR: Stable-State Diffusion for Generative Recommendation

S<sup>2</sup>DGR is a masked-diffusion generative recommendation framework that improves training with Stability-Aware Noising (SAN) and inference with State-Unique Denoising (SUD).

## Environment Setup

```bash
conda create -n s2dgr python=3.10 -y
conda activate s2dgr
pip install -r requirements.txt
```

## Implementation Notes
The main SAN logic is implemented in `genrec/models/S2DGR/model.py`, and SUD beam selection is implemented in `genrec/models/S2DGR/beam.py`.

## Experiments

### Sports and Outdoors

```bash
python -u main.py \
  --model=S2DGR \
  --category=Sports_and_Outdoors \
  --train_batch_size=1024 \
  --n_digit=4 \
  --masking_strategy=stability_guided \
  --stability_steps=auto \
  --stability_num_probes=2 \
  --stability_lambda=0.01 \
  --encoder_n_layer=1 \
  --decoder_n_layer=4 \
  --n_head=4 \
  --n_embd=256 \
  --n_inner=1024 \
  --train_sliding=true \
  --min_hist_len=2 \
  --eval_start_epoch=20 \
  --lr=0.003 \
  --label_smoothing=0.1 \
  --sent_emb_model="sentence-transformers/sentence-t5-base" \
  --sent_emb_dim=768 \
  --sent_emb_pca=256 \
  --sent_emb_batch_size=256 \
  --normalize_after_pca=true \
  --force_regenerate_opq=false \
  --share_decoder_output_embedding=true \
  > S2DGR_sports.log 2>&1
```

### Beauty

```bash
python -u main.py \
  --model=S2DGR \
  --category=Beauty \
  --train_batch_size=1024 \
  --n_digit=4 \
  --masking_strategy=stability_guided \
  --stability_steps=auto \
  --stability_num_probes=4 \
  --stability_lambda=0.01 \
  --encoder_n_layer=1 \
  --decoder_n_layer=4 \
  --n_head=4 \
  --n_embd=256 \
  --n_inner=1024 \
  --train_sliding=true \
  --min_hist_len=2 \
  --eval_start_epoch=20 \
  --lr=0.01 \
  --label_smoothing=0.2 \
  --sent_emb_model="sentence-transformers/sentence-t5-base" \
  --sent_emb_dim=768 \
  --sent_emb_pca=256 \
  --sent_emb_batch_size=256 \
  --normalize_after_pca=true \
  --force_regenerate_opq=false \
  --share_decoder_output_embedding=true \
  > S2DGR_beauty.log 2>&1
```

### Toys and Games

```bash
python -u main.py \
  --model=S2DGR \
  --category=Toys_and_Games \
  --train_batch_size=1024 \
  --n_digit=4 \
  --masking_strategy=stability_guided \
  --stability_steps=auto \
  --stability_num_probes=4 \
  --stability_lambda=0.01 \
  --encoder_n_layer=1 \
  --decoder_n_layer=4 \
  --n_head=8 \
  --n_embd=1024 \
  --n_inner=1024 \
  --train_sliding=true \
  --min_hist_len=2 \
  --eval_start_epoch=10 \
  --lr=0.003 \
  --label_smoothing=0.15 \
  --sent_emb_model="sentence-transformers/sentence-t5-base" \
  --sent_emb_dim=768 \
  --sent_emb_pca=256 \
  --sent_emb_batch_size=256 \
  --normalize_after_pca=true \
  --force_regenerate_opq=false \
  --share_decoder_output_embedding=true \
  > S2DGR_toys.log 2>&1
```

## Generated Files

Running `main.py` automatically creates dataset-specific cache files under:

```bash
cache/AmazonReviews2014/<category>/
```

For example, after running Sports and Outdoors:

```bash
cache/AmazonReviews2014/Sports_and_Outdoors/
├── raw/
└── processed/
```

The `processed/` folder contains the preprocessed interaction files, semantic embeddings, generated SID/token files, and item-token mappings used by the model. Set `--force_regenerate_opq=true` to regenerate the SID/tokenization files.

Model checkpoints and training outputs are saved under:

```bash
saved/
```
