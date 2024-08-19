# DE Simple ETL Binance Project

Project for data processing using Apache Spark & Kafka, with PostgreSQL storage. Python.

## Project Structure

### Описание файлов и папок

- **/binance_streaming/**: Работа с Binance API
  - `__init__.py`: Инициализация пакета.
  - `binance_websocket.py`: Подключение к WebSocket и отправка данных в Kafka.
  
- **/spark_processing/**: Обработка данных с помощью Spark
  - `__init__.py`: Инициализация пакета.
  - `spark_streaming.py`: Чтение из Kafka, обработка и сохранение в PostgreSQL.
  
- **/configs/**: Конфигурационные файлы
  - `kafka_config.py`: Конфигурации Kafka.
  - `spark_config.py`: Конфигурации Spark.
  - `database_config.py`: Конфигурации базы данных.
  
- **main.py**: Основной файл для запуска всех компонентов.
- **requirements.txt**: Зависимости проекта.
- **.gitignore**: Файлы и папки, исключенные из контроля версий.
- **README.md**: Описание проекта.
