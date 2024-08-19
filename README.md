# DE Simple ETL Binance Project

Project for data processing using Apache Spark & Kafka, with PostgreSQL storage. Python.

## Project Structure

### File and Folder Descriptions

**📂 /binance_streaming/**: Work with Binance API
- `__init__.py`: Packages initialization.
- `binance_websocket.py`: Connect to WebSocket and send data to Kafka.

**📂 /spark_processing**: Data processing using Spark
- `__init__.py`: Packages initialization.
- `spark_streaming.py`: Read from Kafka, process, and save to PostgreSQL.

**📂 /configs/**: Configuration files.
- `kafka_config.py`: Kafka configurations.
- `spark_config.py`: Spark configurations.
- `database_config.py`: DataBase configurations.

`main.py`: The main file to run all components.  
`requirements.txt`: Project dependencies.  
`.gitignore`: Files and folders excluded from version control.  
`README.md`: Project description.