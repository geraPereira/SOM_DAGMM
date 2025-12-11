#!/bin/bash
#SBATCH --job-name=som_kdd
#SBATCH --partition=gpu
#SBATCH -p short-complex
#SBATCH --qos=complex
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=32G
#SBATCH --gres=gpu:1
#SBATCH --time=2-00:00:00
#SBATCH --output=logs/som_kdd_%j.out
#SBATCH --error=logs/som_kdd_%j.err


# Carrega o módulo do Miniforge
module load miniforge3

# Habilita o comando conda dentro do job
source "$(conda info --base)/etc/profile.d/conda.sh"


# Ir para o diretório do projeto
cd $HOME/SOM_DAGMM

# Só pra conferência
nvidia-smi
echo "Iniciando treino em $(hostname)"
echo "Começou em $(date)"

# Rodar o train
python3 train.py \
  --dataset kdd \
  --embed label_encode \
  --features numerical \
  --epoch 100 \
  --batch_size 1024

python eval.py \
  --dataset kdd \
  --embed label_encode \
  --features numerical \
  --threshold 20

echo "Terminou em $(date)"