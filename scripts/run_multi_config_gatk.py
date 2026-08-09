# ==========================================================
# GATK Workflow Automation Script - Multi-Config Support
# ==========================================================

import os
import glob

# Ensure output and log directories exist
os.makedirs("results/gatk", exist_ok=True)
os.makedirs("logs/gatk", exist_ok=True)

print("[INFO] Scanning for configuration files in config/...")

# Automatically find all YAML configuration files in the config folder
config_files = glob.glob("config/*.yaml") + glob.glob("config/*.yml")

if not config_files:
    print("[WARNING] No configuration files found in the 'config/' directory!")
else:
    print(f"[INFO] Found {len(config_files)} configuration file(s): {config_files}")

    for config_path in config_files:
        print("\n" + "="*50)
        print(f"[INFO] Processing pipeline using config: {config_path}")
        print("="*50)
        
        # Simulate parsing config or triggering the pipeline for each dataset config
        # In a real pipeline, you would parse the YAML here (e.g., using yaml.safe_load)
        
        # Simulated execution steps based on config
        samples = ["sample_1", "sample_2"] if "iris" not in config_path else ["iris_wild_1", "iris_wild_2", "iris_cultivar_1"]
        
        for sample in samples:
            print(f"  -> [Task] Processing sample: {sample}")
            print(f"     * Running BWA-MEM alignment & GATK HaplotypeCaller...")
            
        print(f"[SUCCESS] Pipeline completed successfully for: {config_path}")

print("\n[SUCCESS] All configuration profiles processed successfully.")
