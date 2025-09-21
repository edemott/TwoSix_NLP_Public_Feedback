#!/bin/bash --login
#SBATCH --job-name=sbert
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --gres=gpu:a100:1
#SBATCH --mem=250G
#SBATCH --time=24:00:00
#SBATCH --output=cleaning_%j.log
#SBATCH --error=cleaning_%j.err
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=netid@msu.edu # Replace with your MSU email address

module purge
module load Miniforge3
conda activate CMSE495-TwoSix
python -m spacy download en_core_web_sm

cd /mnt/research/TwoSix/$USER/TwoSix_Spring25

python sbert/sbert.py

# Optional speed/stability tweaks
export OPENBLAS_NUM_THREADS=1
