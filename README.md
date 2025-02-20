# DailyAutomationHub

🚀 PyAutomateDaily: Simplify your life with 21 Python scripts that automate everyday tasks effortlessly. Save time, code smarter! ✨

### Bulk File Renamer 📂

This program automates renaming multiple files in a folder by replacing a specified part of their names with a new one. Ideal for quickly organizing files with consistent naming conventions!


| **File Name**              | **Renamed To**          |  
|----------------------------|-------------------------|  
| `old_report_2023.txt`      | `new_report_2023.txt`   |  
| `old_summary.docx`         | `new_summary.docx`      |  
| `old_invoice.pdf`          | `new_invoice.pdf`       |  
| `some_other_file.txt`      | `some_other_file.txt`   |  

---

### Files Backup 

backs up these files to a designated backup folder.

```
project_directory/
│
├── script.py       # Main script file
├── test_folder/    # Folder containing generated files
│   ├── old_report_2023.txt
│   ├── old_summary.docx
│   ├── old_invoice.pdf
│   └── some_other_file.txt
├── BackUpfolder/   # Folder for backed-up files
```
---
### Install ML library And Update All Existing Library

This script automates the process of installing and updating Python packages. It reads package names from a `requirements.txt` file and ensures that all specified packages, as well as currently installed packages, are up-to-date with their latest versions.

``` requirements.txt ``` - conains the basic and various advange ML, DL, GEN AI library that are required by an ML engineer

#### Features

- **Automatic Installation**: Installs packages listed in `requirements.txt`.
- **Automatic Upgrades**: Upgrades all installed packages to their latest versions.
- **Concurrency**: Utilizes multiple threads to speed up the installation and upgrade process.
- **Error Handling**: Captures and reports any installation failures.

#### Why Use This Script?

- **Efficiency**: Save time by automating the installation and upgrade of multiple packages.
- **Consistency**: Ensure all your packages are up-to-date with the latest versions.
- **Convenience**: Easily manage package installations and upgrades with a single script.

#### Usage

1. Place your package names in a file named `requirements.txt`.
2. Run the script to install and upgrade packages.

---

#### Sequential Execution

The URLs are fetched one after the other. This method is straightforward but can be inefficient for multiple tasks that could be run concurrently.

```
+-------------------+     +-------------------+     +-------------------+
| Fetch URL 1       | --> | Fetch URL 2       | --> | Fetch URL 3       |
+-------------------+     +-------------------+     +-------------------+
```

#### Threaded Execution

Using threads, the URLs are fetched concurrently. This method improves performance when there are multiple I/O-bound operations (like HTTP requests) by utilizing multiple threads to perform tasks simultaneously.

```
+-------------------+     +-------------------+     +-------------------+
| Fetch URL 1       |     | Fetch URL 2       |     | Fetch URL 3       |
+-------------------+     +-------------------+     +-------------------+
        |                      |                      |
        +----------+-----------+-----------+----------+
                   |                       |
                   v                       v
                     Concurrent Execution
```

---

### PostgreSQL Data Upload Script

#### Overview
Automates CSV data upload into PostgreSQL by cleaning table/column names, generating schemas, creating tables, and bulk inserting data.

#### Steps
1. **Clean Names:** Standardizes table/column names.
2. **Schema Mapping:** Converts pandas dtypes to SQL types.
3. **Table Creation:** Drops and recreates the table.
4. **Bulk Insert:** Loads data efficiently with `COPY`.

#### Benefits
- **Fast & Efficient** data loading.
- **Automated** table setup.
- **Flexible** for different data schemas.



