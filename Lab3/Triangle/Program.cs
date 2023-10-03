using System.Collections;
using System.Text;
using triangle;

namespace runner;



static class Programm
{
    public static void Main()
    {
        Triangle tr = new Triangle(1.0, 2.0, 2.0);

        Console.WriteLine(tr.CheckTriangle());
        Console.WriteLine(tr.Message);
        Console.WriteLine(tr.DetectTriangle());
    }
}