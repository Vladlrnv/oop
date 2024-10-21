# Работа с классами
## На данном этапе в программе реализованы классы Product и Category.

### Для класса Product определены следующие свойства:
* название(name);
* описание(description);
* цена(price);
* количество в наличии(quantity).

#### Для класса Product созданы наследующие классы:
##### Класс Smartphone:
* производительность(efficiency);
* модель(model);
* объем встроенной памяти(memory);
* цвет(color).
##### Класс LawmGrass:
* страна-производитель(country);
* срок прорастания(germination_period);
* цвет(color)
### Для класса Category определены следующие свойства:
* название(name);
* описание(description);
* список товаров категории(products).
### Функционал приложения создан таким образом, что можно складывать товары только из одинаковых классов продуктов.

### Все функциональности протестированы. Результаты покрытия тестами:
* src\category.py                100%
* src\product.py                 100%
* tests\conftest.py              100%
* tests\test_category.py         100%
* tests\test_product.py          100%
--------------------------------------------
* TOTAL                           100%