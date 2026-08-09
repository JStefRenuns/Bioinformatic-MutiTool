# Bioinformatic-MutiTool
Translational Bioinformatics Multi-Tool Pipeline
Production-grade genomics workflow combining **Galaxy/Snakemake**, **GATK4**, **Julia/Pandas**, **Docker**, and **Nextflow** benchmarked on the Breast Cancer Wisconsin diagnostic dataset.

## 📊 Pipeline Architecture & Tools
1. **Containerization:** Docker & Conda environment specifications (`Dockerfile`, `environment.yml`).
2. **Orchestration:** Snakemake DAG execution managing modular tasks.
3. **Variant Discovery:** GATK `HaplotypeCaller` & hard filtering (`QUAL > 40`, `DP > 15`).
4. **Data Analytics:** High-speed DataFrame parsing & t-SNE functional clustering.

## 🚀 Quick Start & Installation
\`\`\`bash
git clone https://github.com/JStefRenuns/Bioinformatics-MultiTool.git
cd bioinformatics-genomics-pipeline
conda env create -f environment.yml
conda activate bioinfo-master
snakemake --cores 4
\`\`\`

## 📈 Results & Visualizations
### Functional Biomarker t-SNE Clustering
![t-SNE Clustering](comprehensive_results/functional_tsne.png)

### GATK Variant Quality & Depth QC
![GATK QC](comprehensive_results/gatk_qc.png)

