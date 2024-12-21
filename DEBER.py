using System;

namespace FigurasGeometricas
{
    // Clase para representar un Círculo
    public class Circulo
    {
        // Propiedad para el radio
        public double Radio { get; set; }

        // Constructor
        public Circulo(double radio)
        {
            Radio = radio;
        }

        // Método para calcular el área
        public double CalcularArea()
        {
            return Math.PI * Math.Pow(Radio, 2);
        }

        // Método para calcular el perímetro
        public double CalcularPerimetro()
        {
            return 2 * Math.PI * Radio;
        }
    }

    // Clase para representar un Cuadrado
    public class Cuadrado
    {
        // Propiedad para el lado
        public double Lado { get; set; }

        // Constructor
        public Cuadrado(double lado)
        {
            Lado = lado;
        }

        // Método para calcular el área
        public double CalcularArea()
        {
            return Math.Pow(Lado, 2);
        }

        // Método para calcular el perímetro
        public double CalcularPerimetro()
        {
            return 4 * Lado;
        }
    }

    // Clase principal para probar las figuras
    class Program
    {
        static void Main(string[] args)
        {
            // Crear un círculo con radio 5
            Circulo circulo = new Circulo(5);
            Console.WriteLine($"Círculo: Área = {circulo.CalcularArea()}, Perímetro = {circulo.CalcularPerimetro()}");

            // Crear un cuadrado con lado 4
            Cuadrado cuadrado = new Cuadrado(4);
            Console.WriteLine($"Cuadrado: Área = {cuadrado.CalcularArea()}, Perímetro = {cuadrado.CalcularPerimetro()}");
        }
    }
}
