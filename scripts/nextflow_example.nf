#!/usr/bin/env nextflow

nextflow.enable.dsl=2

params.reads = "data/raw/*_{1,2}.fastq.gz"
params.outdir = "results_nextflow"

log.info """
======================================================
 B I O I N F O R M A T I C   M U T I - T O O L (NF)
======================================================
reads          : ${params.reads}
outdir         : ${params.outdir}
"""

include { FASTQC } from './modules/fastqc'

workflow {
    read_pairs_ch = Channel.fromFilePairs(params.reads, checkIfExists: true)
    
    // Run FastQC Quality Control module
    FASTQC(read_pairs_ch)
}
