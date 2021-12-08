# Генератор отчетов
## Структура

Для генерации отчетов необходимо разместить файлы ```report_generator.py```,```balaboba_request.py```,```config.json``` в одной директории с папками проектов, на основе которых будут генерироваться отчеты.

В ```report_generator.py``` определены константы ```TITUL_PAGE```, ```OUTPUT_PAGE```, ```CONFIG_JSON```, указывающие файл титульника, выходного документа и конфигурационный файл.

Конфигурационный файл ```config.json``` структурирован следующим образом:

```
{
    "tasks" : [
        {
            "folder" : "Папка_проекта_1",
            "include" : ["Название_файла_1", "Название_файла_2"],
            "topic" : "Тема проекта_1",
            "problem_statement" : "Постановка задачи" 
        },
        ...
        {
            "folder" : "Папка_проекта_2",
            "include" : ["Название_файла_1", "Название_файла_2"],
            "topic" : "Тема проекта_2",
            "problem_statement" : "Постановка задачи" 
        }
}
```
## Пример заполнения конфигурации
Например, если есть следующий каталог:
- **RecursionJava**
  - Task1
    - Fibonacci.java
    - Factorial.java
  - Task2
    - MaxMin.java
    - OddNums.java
- **ContainersJava**
  - Arrays
    - TestArrayList.java
    - TestArray.java
  - Lists
    - TestLinkedList.java
    - TestDoubleLikedList.java

И мы хотим составить отчет по двум проектам, то конфигурационный файл можно заполнить следующим образом:

```
{
    "tasks" : [
        {
            "folder" : "RecursionJava",
            "include" : ["Fibonacci", "MaxMin"],
            "topic" : "Рекурсия в Java",
            "problem_statement" : "Решить задачи с использованием рекурсии в Java" 
        },
        ...
        {
            "folder" : "ContainersJava",
            "include" : ["TestArrayList", "TestDoubleLikedList", "TestLinkedList"],
            "topic" : "Контейнеры в Java",
            "problem_statement" : "Изучить и протестировать контейнеры в Java" 
        }
}
```

## Пример сгенерированного отчета
![image](https://user-images.githubusercontent.com/71013663/145196055-3e92f700-702e-4196-82c9-b34cf746e4af.png)
