#!/bin/bash --login
#SBATCH --job-name=cleaning
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --mem=128G
#SBATCH --time=5:00:00
#SBATCH --output=cleaning_%j.log
#SBATCH --error=cleaning_%j.err
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=netid@msu.edu     # Replace with your MSU email address

module purge
module load Miniforge3
conda activate CMSE495-TwoSix

cd /mnt/research/TwoSix/$USER/TwoSix_Spring25

python data/cleaning.py
