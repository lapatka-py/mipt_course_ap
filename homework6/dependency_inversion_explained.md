Dependency inversion principle - Принцип инверсии зависимостей - это особая форма 
разделения программных модулей. При следовании этому принципу обычные 
отношения зависимости, устанавливаемые от высокоуровневых модулей к 
низкоуровневым модулям, меняются местами, что делает модули высокого 
уровня независимыми от деталей реализации модуля нижнего уровня.

Принцип гласит:

Модули высокого уровня не должны зависеть от модулей низкого уровня.
Абстракции не должны зависеть от деталей. Детали (конкретные реализации) должны зависеть от абстракций.

Пример - Генеалогический модуль
Генеалогическая система может представлять отношения между людьми в 
виде графика прямых отношений между ними 
(отец-сын, отец-дочь, мать-сын, мать-дочь, муж-жена, жена-муж и т. Д.). 
Это очень эффективно и расширяемо, так как легко добавить бывшего мужа 
или законного опекуна. Но для некоторых модулей более высокого уровня 
может потребоваться более простой способ просмотра системы: у любого 
человека могут быть дети, родители, братья и сестры 
(включая сводных братьев и сестер), бабушек и дедушек, двоюродных 
братьев и т.п. В зависимости от использования генеалогического модуля, 
представление общих отношений в виде отдельных прямых свойств 
(скрытие графа) значительно облегчит связь между модулем более высокого 
уровня и генеалогическим модулем и позволит полностью изменить 
внутреннее представление прямых отношений. без какого-либо влияния на 
используемые ими модули. Он также позволяет встраивать точные определения
братьев и сестер или дядей в генеалогический модуль, тем самым обеспечивая 
соблюдение принципа единой ответственности. Наконец, если первый подход 
с расширяемым обобщенным графом кажется наиболее расширяемым, 
использование генеалогического модуля может показать, что более 
специализированная и более простая реализация отношений достаточна для 
приложения (приложений) и помогает создать более эффективную систему. 
В этом примере абстрагирование взаимодействия между модулями приводит 
к упрощенному интерфейсу модуля нижнего уровня и может привести к его 
более простой реализации.