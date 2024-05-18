import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Laptop {
    private String brand;
    private double price;
    private int ram;

    // Конструктор класса Laptop
    public Laptop(String brand, double price, int ram) {
        this.brand = brand;
        this.price = price;
        this.ram = ram;
    }

    // Геттер для бренда ноутбука
    public String getBrand() {
        return brand;
    }

    // Геттер для цены ноутбука
    public double getPrice() {
        return price;
    }

    // Геттер для объема RAM ноутбука
    public int getRam() {
        return ram;
    }

    // Переопределение метода equals для сравнения ноутбуков по бренду, цене и RAM
    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Laptop laptop = (Laptop) o;
        return Double.compare(laptop.price, price) == 0 &&
               ram == laptop.ram &&
               brand.equals(laptop.brand);
    }

    // Переопределение метода hashCode для правильного хеширования объектов
    @Override
    public int hashCode() {
        return brand.hashCode() + Double.hashCode(price) + Integer.hashCode(ram);
    }

    // Переопределение метода toString для представления информации о ноутбуке в виде строки
    @Override
    public String toString() {
        return brand + " - Цена: " + price + " - RAM: " + ram;
    }

    // Основной метод main программы
    public static void main(String[] args) {
        Set<Laptop> laptops = new HashSet<>();
        laptops.add(new Laptop("Dell", 1200.0, 8));
        laptops.add(new Laptop("HP", 1000.0, 16));
        laptops.add(new Laptop("HP", 1000.0, 16));// Пример дубликата объекта
        laptops.add(new Laptop("Apple", 1500.0, 8));
        laptops.add(new Laptop("Apple", 1500.0, 8)); // Пример дубликата объекта

        // Создание объекта Scanner для ввода данных пользователем
        Scanner scanner = new Scanner(System.in);

        // Запрос у пользователя максимальной цены ноутбука
        System.out.print("Введите максимальную цену: ");
        double maxPrice = scanner.nextDouble();

        // Запрос у пользователя минимального объема RAM
        System.out.print("Введите минимальный объем RAM: ");
        int minRam = scanner.nextInt();

        // Создание нового множества для отфильтрованных ноутбуков
        Set<Laptop> filteredLaptops = new HashSet<>();
        // Фильтрация ноутбуков по заданным критериям
        for (Laptop laptop : laptops) {
            if (laptop.getPrice() <= maxPrice && laptop.getRam() >= minRam) {
                filteredLaptops.add(laptop);
            }
        }

        // Вывод отфильтрованных ноутбуков
        System.out.println("Ноутбуки по вашим критериям:");
        for (Laptop laptop : filteredLaptops) {
            System.out.println(laptop);
        }
    }
}