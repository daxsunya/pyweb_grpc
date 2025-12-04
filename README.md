# Запуск проекта

## Установка необходимых зависимостей

```
pip install -r requirements.txt
```

Генерация на основе .proto файла

```
python -m grpc_tools.protoc -I./protos --python_out=. --pyi_out=. --grpc_python_out=. ./protos/glossary.proto
```

## Запуск

Запуск сервера

```
python3 glossary_server.py 
```
