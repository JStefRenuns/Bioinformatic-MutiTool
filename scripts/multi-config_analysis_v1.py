# ==========================================================
# Multi-Config Biomarker Analysis Pipeline (Config Folder Scan)
# ==========================================================

import os
import glob
import yaml
import pandas as pd
import numpy as np
from sklearn.datasets import load_breast_cancer, load_iris

# Ensure output and config directories exist
os.makedirs("results", exist_ok=True)
os.makedirs("config", exist_ok=True)

print("[INFO] Scanning 'config/' folder for configuration files...")

# Automatically scan exclusively for files inside the config/ folder
config_files = glob.glob("config/*.yaml") + glob.glob("config/*.yml")

if not config_files:
    print("[WARNING] No configuration files found in the 'config/' folder!")
else:
    print(f"[INFO] Found {len(config_files)} configuration file(s) in config/: {config_files}")

    for config_path in config_files:
        print("\n" + "="*60)
        print(f"[INFO] Processing workflow using config: {config_path}")
        print("="*60)
        
        # Load configuration parameters from the config file
        with open(config_path, "r") as f:
            config = yaml.safe_load(f)
            
        dataset_name = config.get("dataset_name", "breast_cancer")
        threshold_value = config.get("threshold_value", 11.0)
        output_csv = config.get("output_csv", "filtered_biomarkers.csv")
        
        print(f"  -> Dataset Type: {dataset_name}")
        print(f"  -> Filter Threshold: {threshold_value}")
        print(f"  -> Output Target: {output_csv}")
        
        # Load corresponding dataset dynamically
        if dataset_name == "breast_cancer":
            cancer = load_breast_cancer()
            X, y, target_names = cancer.data, cancer.target, cancer.target_names
            df_raw = pd.DataFrame(X, columns=cancer.feature_names)
            df_raw['diagnosis'] = [target_names[i] for i in y]
            
            # Apply filter based on config value
            filtered_df = df_raw[df_raw['mean radius'] > threshold_value]
            
        elif dataset_name == "iris":
            iris = load_iris()
            X, y, target_names = iris.data, iris.target, iris.target_names
            df_raw = pd.DataFrame(X, columns=iris.feature_names)
            df_raw['species'] = [target_names[i] for i in y]
            
            # Apply filter based on threshold from config
            filtered_df = df_raw[df_raw['sepal length (cm)'] > threshold_value]
        else:
            print(f"[ERROR] Unknown dataset name specified in {config_path}")
            continue
            
        # Export processed data
        filtered_df.to_csv(output_csv, index=False)
        print(f"  -> [SUCCESS] Filtered data saved to: {output_csv} (Rows: {len(filtered_df)})")

print("\n[SUCCESS] All configuration profiles from config/ folder processed successfully.")
