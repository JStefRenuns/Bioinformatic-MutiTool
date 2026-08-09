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
git clone [https://github.com/JStefRenuns/Bioinformatic-MultiTool.git](https://github.com/JStefRenuns/Bioinformatic-MutiTool/blob/main/README.md)
cd bioinformatics-genomics-pipeline
conda env create -f environment.yml
conda activate bioinfo-master
snakemake --cores 4
\`\`\`

## 📈 Results & Visualizations
### Functional Biomarker t-SNE Clustering
### Data Analysis Pipeline
* **t-SNE Script:** You can review the complete data ingestion and scaling code in the [t-SNE Clustering Script](https://github.com/JStefRenuns/Bioinformatic-MutiTool/blob/main/scripts/t-SNE_clustering)
![t-SNE Clustering](comprehensive_results/functional_ts.png)

### GATK Variant Quality & Depth QC
![GATK QC](comprehensive_results/gatk_qc.png)

