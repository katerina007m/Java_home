import java.util.Objects;

public class Laptop {
    private String brand;
    private double price;
    private int ram;

    public Laptop(String brand, double price, int ram) {
        this.brand = brand;
        this.price = price;
        this.ram = ram;
    }

    public String getBrand() {
        return brand;
    }

    public double getPrice() {
        return price;
    }

    public int getRam() {
        return ram;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Laptop laptop = (Laptop) o;
        return Double.compare(laptop.price, price) == 0 &&
               ram == laptop.ram &&
               Objects.equals(brand, laptop.brand);
    }

    @Override
    public int hashCode() {
        return Objects.hash(brand, price, ram);
    }
    
    @Override
    public String toString() {
        return brand + " - Цена: " + price + " - RAM: " + ram; // Добавим для удобства вывода
    }
}