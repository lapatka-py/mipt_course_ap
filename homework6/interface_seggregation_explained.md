Interface segregation principle (ISP) - Принцип разделения интерфейса гласит, 
что ни один клиент не должен зависеть от методов, которые он не использует.

Пример - Xerox
Давным давно Xerox создала новую систему печати, 
которая могла выполнять множество задач, 
таких как сшивание и отправка факсов. Программное обеспечение 
для этой системы создавалось с нуля. По мере роста программного 
обеспечения внесение изменений становилось все труднее и труднее, 
так что даже самое маленькое изменение занимало цикл повторного 
развертывания в час, что делало разработку практически невозможной. 
Проблема проектирования заключалась в том, что практически для всех 
задач использовался один класс Job. Каждый раз, когда требовалось 
выполнить задание на печать или сшивание, вызывается класс Job. 
В результате получился «толстый» класс с множеством методов, 
специфичных для множества различных клиентов. Из-за этой конструкции 
задание сшивания будет знать обо всех методах задания печати, даже 
если они не нужны. Решение заключалось в применении ISP. Вместо одного 
большого класса Job был создан интерфейс Staple Job или интерфейс 
Print Job, который будет использоваться классами Staple или Print 
соответственно, вызывая методы класса Job.