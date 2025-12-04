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
Успешно

<img width="566" height="48" alt="Снимок экрана 2025-12-04 в 22 37 50" src="https://github.com/user-attachments/assets/6cd4450c-3ed1-4efd-9b04-be8ff040dfb0" />

# Удаленный вызов процедур

## Создать новый термин

```
grpcurl -plaintext \
  -d '{"keyword":"API","description":"Application Programming Interface"}' \
  localhost:50051 glossary.GlossaryService/CreateTerm
```
<img width="547" height="115" alt="Снимок экрана 2025-12-04 в 22 46 31" src="https://github.com/user-attachments/assets/28cdbad5-49e5-4cc3-8555-3a38c84b0c05" />

## Получить все термины

```
grpcurl -plaintext \
  localhost:50051 glossary.GlossaryService/GetTerms 
```
<img width="476" height="156" alt="Снимок экрана 2025-12-04 в 22 44 37" src="https://github.com/user-attachments/assets/54f3882f-8aab-45da-a075-b89fc36f814e" />

## Получить термин по ключевому слову

```
grpcurl -plaintext \
  -d '{"keyword":"API-2"}' \                                                  
  localhost:50051 glossary.GlossaryService/GetTerm 
```
<img width="547" height="209" alt="Снимок экрана 2025-12-04 в 22 48 22" src="https://github.com/user-attachments/assets/5eef40fc-36d2-4f0c-a2f1-ef0f5755cebe" />
<img width="547" height="115" alt="Снимок экрана 2025-12-04 в 22 49 00" src="https://github.com/user-attachments/assets/e6c83b3b-cfc2-4df0-9319-1e5b8f9f5218" />

## Обновить термин

```
grpcurl -plaintext \
  -d '{"keyword":"API","description":"Новое описание API"}' \
  localhost:50051 glossary.GlossaryService/UpdateTerm
```
<img width="510" height="309" alt="Снимок экрана 2025-12-04 в 22 50 40" src="https://github.com/user-attachments/assets/774b14f2-b2ae-4001-a8a2-7e5fde809988" />

## Удалить термин

```
grpcurl -plaintext \
  -d '{"keyword":"API"}' \                                   
  localhost:50051 glossary.GlossaryService/DeleteTerm
```
<img width="409" height="213" alt="Снимок экрана 2025-12-04 в 22 52 06" src="https://github.com/user-attachments/assets/31ca4a43-af2d-49f3-9a25-e0aec5cdd0ed" />
