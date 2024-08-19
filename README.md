<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DE Simple ETL Binance Project</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        .container {
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .folder, .file {
            margin-left: 20px;
        }
        .folder::before {
            content: "📂";
            margin-right: 8px;
        }
        .file::before {
            content: "📄";
            margin-right: 8px;
        }
        .comment {
            color: #555;
            margin-left: 40px;
            font-style: italic;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>DE Simple ETL Binance Project</h1>
        <p>Project for data processing using Apache Spark &amp; Kafka, with PostgreSQL storage. Python.</p>

        <div class="folder">
            <span class="file">/project/</span>

            <div class="folder">
                <span class="folder">/binance_streaming/</span>
                <div class="comment"># Работа с Binance API</div>
                <div class="file">init.py</div>
                <div class="file">binance_websocket.py</div>
                <div class="comment"># Подключение к WebSocket и отправка данных в Kafka</div>
            </div>

            <div class="folder">
                <span class="folder">/spark_processing/</span>
                <div class="comment"># Обработка данных с помощью Spark</div>
                <div class="file">init.py</div>
                <div class="file">spark_streaming.py</div>
                <div class="comment"># Чтение из Kafka, обработка и сохранение в PostgreSQL</div>
            </div>

            <div class="folder">
                <span class="folder">/configs/</span>
                <div class="comment"># Конфигурационные файлы</div>
                <div class="file">kafka_config.py</div>
                <div class="comment"># Конфигурации Kafka</div>
                <div class="file">spark_config.py</div>
                <div class="comment"># Конфигурации Spark</div>
                <div class="file">database_config.py</div>
                <div class="comment"># Конфигурации базы данных</div>
            </div>

            <div class="file">main.py</div>
            <div class="comment"># Основной файл для запуска всех компонентов</div>
            <div class="file">requirements.txt</div>
            <div class="comment"># Зависимости проекта</div>
            <div class="file">.gitignore</div>
            <div class="comment"># Файлы и папки, исключенные из контроля версий</div>
            <div class="file">README.md</div>
            <div class="comment"># Описание проекта</div>
        </div>
    </div>
</body>
</html>