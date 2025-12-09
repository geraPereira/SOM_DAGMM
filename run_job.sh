#!/bin/bash
#SBATCH --job-name=meu_projeto
#SBATCH --output=logs/%x_%j.out
#SBATCH --error=logs/%x_%j.err
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32G
#SBATCH --gres=gpu:1
#SBATCH --partition=short-simple
#SBATCH --time=12:00:00

echo "🚀 Iniciando job em $(hostname)"
date

# Carrega o módulo python
module load Python/3.10.8-GCCcore-12.2.0

# Ativa o ambiente Python
source ~/SOM_DAGMM/venv/bin/activate

# Caminho do projeto
cd ~/projeto

# Mostra GPU disponível
nvidia-smi

# Executa o código
python train.py

echo "✅ Job finalizado!"
date