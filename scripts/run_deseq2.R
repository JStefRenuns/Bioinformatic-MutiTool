# scripts/run_deseq2.R

log_file <- file(snakemake@log[[1]], open = "wt")
sink(log_file, type = "output")
sink(log_file, type = "message")

suppressPackageStartupMessages({
  library(DESeq2)
  library(ggplot2)
  library(dplyr)
  library(readr)
})

# 1. Parse Input Files from Snakemake
count_files <- snakemake@input[["counts"]]
sample_names <- gsub("_ReadsPerGene\.out\.tab$", "", basename(count_files))
condition_groups <- ifelse(grepl("^control", sample_names), "control", "treatment")

coldata <- data.frame(
  sample = sample_names,
  condition = factor(condition_groups, levels = c("control", "treatment")),
  row.names = sample_names
)

# 2. Load and Combine STAR ReadsPerGene Tables
counts_list <- lapply(count_files, function(file) {
  df <- read.table(file, skip = 4, header = FALSE, stringsAsFactors = FALSE)
  df[, c(1, 2)]
})

counts_matrix <- do.call(cbind, lapply(counts_list, function(df) df[, 2]))
rownames(counts_matrix) <- counts_list[[1]][, 1]
colnames(counts_matrix) <- sample_names

keep <- rowSums(counts_matrix) >= 10
counts_matrix <- counts_matrix[keep, ]

# 3. Perform Differential Expression Analysis
dds <- DESeqDataSetFromMatrix(
  countData = counts_matrix,
  colData = coldata,
  design = ~ condition
)

dds <- DESeq(dds)
res <- results(dds, name = "condition_treatment_vs_control")

res_df <- as.data.frame(res) %>%
  rownames_to_column(var = "gene_id") %>%
  arrange(padj)

write_csv(res_df, snakemake@output[["results_csv"]])

# 4. Generate Volcano Plot Visualization
res_df <- res_df %>%
  mutate(significance = case_when(
    padj < 0.05 & log2FoldChange > 1  ~ "Upregulated",
    padj < 0.05 & log2FoldChange < -1 ~ "Downregulated",
    TRUE                              ~ "Not Significant"
  ))

volcano_p <- ggplot(res_df, aes(x = log2FoldChange, y = -log10(padj), color = significance)) +
  geom_point(alpha = 0.6, size = 1.5) +
  scale_color_manual(values = c("Upregulated" = "#D55E00", "Downregulated" = "#0072B2", "Not Significant" = "gray70")) +
  geom_vline(xintercept = c(-1, 1), linetype = "dashed", color = "gray40") +
  geom_hline(yintercept = -log10(0.05), linetype = "dashed", color = "gray40") +
  labs(
    title = "Differential Expression: Treatment vs Control",
    x = expression(log[2] ~ "Fold Change"),
    y = expression(-log[10] ~ "(Adjusted P-value)"),
    color = "Status"
  ) +
  theme_minimal(base_size = 12) +
  theme(panel.grid.minor = element_blank())

ggsave(
  filename = snakemake@output[["volcano_plot"]],
  plot = volcano_p,
  width = 7,
  height = 5,
  dpi = 300
)

sink(type = "message")
sink(type = "output")
close(log_file)

