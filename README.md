# **Using Delta Lake with `deltalake` (No Spark Required!)**  

## **Overview**  
This repository demonstrates how to perform **DML operations** (`INSERT`, `UPDATE`, `DELETE`, **partitioned writes**) on **Delta Lake** **without Spark**, using Python libraries **`deltalake`**.  

## **Why Not Just Use Spark?**  
Spark is great but requires a dedicated cluster.
Sometimes, you just need a lightweight way to interact with Delta.
This approach provides a simpler alternative while still supporting partitioned data storage for efficient querying.

## **Key Benefits of This Approach**  
✔️ No Spark Cluster Required – Lightweight & efficient.
✔️ Supports Partitioning – Optimized for large datasets.
✔️ Works with Both S3 & HDFS – Flexible storage options.
✔️ Time Travel Support – Access previous data versions.

---

#### 📂 **Project Structure **  
```
deltalake-dml-python/
│── config/                  # Configuration files for storage
│   │── hdfs_config.py       # HDFS connection setup
│   │── s3_config.py         # S3 connection setup
│── examples/                # Example scripts for Delta Lake operations
│   │── 01-setup.py          # Initialize Delta Table (if not exists)
│   │── 02-insert-overwrite.py  # Overwrite existing records
│   │── 03-insert-append.py     # Append new records
│   │── 04-update-condition.py  # Conditional update of records
│   │── 05-update-partition.py  # Partition-based update
│   │── 06-delete-condition.py  # Conditional delete
│   │── 07-extra-time_travel.py # Time travel: access previous versions
│── .env.sample              # Environment variables template
│── README.md                # Documentation
│── requirements.txt         # Required dependencies
```

---

### 🚀 **Getting Started** (Merged Install & Configure)  
```bash
pip install -r requirements.txt
cp .env.sample .env  # Add your credentials in .env
```

---

### 🔧 **Configuration** 
Use `get_deltatable()` to connect to Delta tables on **S3 or HDFS**.

---

### 🛠 **Features Supported** 
✅ Insert (Append & Overwrite) | ✅ Update (Condition & Partition) | ✅ Delete (Condition) | ✅ Delta Time Travel  

---

Let me know if you need any refinements! 🚀
