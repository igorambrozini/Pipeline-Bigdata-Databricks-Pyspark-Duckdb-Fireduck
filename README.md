# 🧊 ETL - Pipeline with Databricks, PySpark, DuckDB & Fireduck

> Efficiently processing 1 billion rows using modern data engineering tools.

## 📌 Introduction

The goal of this project is to demonstrate how to efficiently process a massive dataset containing **1 billion rows** to compute statistics, including **aggregation and sorting**, which are computationally heavy operations. The implementation is done in **Python**.

The dataset consists of temperature measurements from various weather stations. Each record follows the format:

```
<string: station name>;<double: temperature>
```

Temperatures are provided with **one decimal place** of precision.

### 🔍 Example (10 lines from the dataset):

```
Hamburg;12.0
Bulawayo;8.9
Palembang;38.8
St. Johns;15.2
Cracow;12.6
Bridgetown;26.9
Istanbul;6.2
Roseau;34.4
Conakry;31.2
Istanbul;23.0
```

The task is to develop a Python program capable of reading this file and calculating the **minimum**, **mean (rounded to one decimal place)**, and **maximum** temperature for each station, displaying the results in a table sorted by station name.

---

### 📊 Sample Output

| station        | min_temperature | mean_temperature | max_temperature |
|----------------|------------------|-------------------|------------------|
| Abha           | -31.1            | 18.0              | 66.5             |
| Abidjan        | -25.9            | 26.0              | 74.6             |
| Abéché         | -19.8            | 29.4              | 79.9             |
| Accra          | -24.8            | 26.4              | 76.3             |
| Addis Ababa    | -31.8            | 16.0              | 63.9             |
| Adelaide       | -31.8            | 17.3              | 71.5             |
| ...            | ...              | ...               | ...              |
| İzmir          | -34.4            | 17.9              | 67.9             |

---

## 🧠 Project Scope

- **Technologies explored:** Databricks, PySpark, DuckDB, Fireduck, Polars
- **Focus:** Efficient processing and benchmarking of massive datasets
- **Inspiration:** One Billion Row Challenge (1BRC)

### 🎯 Objectives

- Benchmark different tools and techniques for processing large-scale data
- Explore modern libraries like **DuckDB**, **Fireduck**, **Polars**, and **Databricks Notebooks**
- Share learnings and performance insights with the data engineering community

---

## 🤝 Contributing

Feel free to open issues or pull requests to suggest improvements or explore new tools. Contributions are welcome!

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

