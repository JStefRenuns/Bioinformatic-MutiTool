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
git clone https://github.com/JStefRenuns/Bioinformatic-MutiTool.git
cd Bioinformatic-MutiTool
conda env create -f environment.yml
conda activate bioinfo-master
snakemake --cores 4
\`\`\`

## 📈 Results & Visualizations

### Data Analysis Pipeline
* **t-SNE Script:** Review the complete data ingestion and scaling code in the [t-SNE Clustering Script](scripts/tsne_clustering.py)

### GATK Variant Quality & Depth QC
* **GATK QC Script:** Review the complete variant quality control code in the [GATK QC Script](scripts/gatk_qc.py)

### Pipeline Results & Execution
* **t-SNE Clustering:**
  ![t-SNE Plot](results/tsne_plot.png)
* **GATK QC:**
  ![GATK QC Plot](results/gatk_qc.png)

  * **Nextflow Pipeline:** Review the workflow orchestration code in the [Nextflow Example Pipeline](nextflow_example.nf)
 
## 🧬 Differential Expression Analysis (DESeq2)

The pipeline integrates automated RNA-Seq quantification using STAR followed by statistical differential expression analysis via DESeq2. 

### 📊 Results & Visualization
* **Volcano Plot Visualization:** 
  The plot below highlights statistically significant up- and down-regulated genes (highlighted in orange) based on log2 fold change and adjusted $p$-value thresholds.
  ![DESeq2 Differential Expression Volcano Plot](results/deseq2/volcano_plot.png)

### 📂 Pipeline Artifacts & Scripts
* **Analysis Script:** Review the core statistical modeling code in [DESeq2 Script](scripts/run_deseq2.R).
* **Execution Log:** Check the processing output details in [DESeq2 Execution Log](logs/deseq2/run.log).
* **Result Data:** Access the final tabulated gene metrics in [Differential Expression Results CSV](results/deseq2/differential_expression_results.csv).s
