using MSTestExtensions;
using triangle;


namespace Tests.TestDetectTriangle;


[TestClass]
public class Triangle_DetectTriangle_Normal
{
    const int TR_EQUILATERAL = 0b_0001;   // равносторонний
    const int TR_ISOSCELES =   0b_0010;   // равнобедренный
    const int TR_ORDYNARY =    0b_0100;   // обычный
    const int TR_RECTANGULAR = 0b_1000;   // прямоугольный

    [TestMethod]
    public void DetectTriangle_OrdynaryAcute()
    {
        Triangle tr = new Triangle(15.0, 12.0, 14.0);

        int expectedRes = TR_ORDYNARY;
        int res = tr.DetectTriangle();

        Assert.AreEqual(expectedRes, res);
    }

    [TestMethod]
    public void DetectTriangle_IsoscelesAcute()
    {
        Triangle tr = new Triangle(6.0, 3.1, 6.0);

        int expectedRes = TR_ISOSCELES;
        int res = tr.DetectTriangle();

        Assert.AreEqual(expectedRes, res);
    }

    [TestMethod]
    public void DetectTriangle_OrdynaryRight()
    {
        Triangle tr = new Triangle(3.0, 4.0, 5.0);

        int expectedRes = TR_RECTANGULAR;
        int res = tr.DetectTriangle();

        Assert.AreEqual(expectedRes, res);
    }

    [TestMethod]
    public void DetectTriangle_IsoscelesRight()
    {
        Triangle tr = new Triangle(1.0, 1.0, Math.Sqrt(2.0));

        int expectedRes = TR_RECTANGULAR | TR_ISOSCELES;
        int res = tr.DetectTriangle();

        Assert.AreEqual(expectedRes, res);
    }

    [TestMethod]
    public void DetectTriangle_OrdynaryObtuse()
    {
        Triangle tr = new Triangle(1.4, 3.0, 4.0);

        int expectedRes = TR_ORDYNARY;
        int res = tr.DetectTriangle();

        Assert.AreEqual(expectedRes, res);
    }

    [TestMethod]
    public void DetectTriangle_IsoscelesObtuse()
    {
        Triangle tr = new Triangle(2.1, 2.1, 4.0);

        int expectedRes = TR_ISOSCELES;
        int res = tr.DetectTriangle();

        Assert.AreEqual(expectedRes, res);
    }

    [TestMethod]
    public void DetectTriangle_Equilateral()
    {
        Triangle tr = new Triangle(1.0, 1.0, 1.0);

        int expectedRes = TR_EQUILATERAL | TR_ISOSCELES;
        int res = tr.DetectTriangle();

        Assert.AreEqual(expectedRes, res);
    }
}


[TestClass]
public class Triangle_DetectTriangle_ImpossibleButSidesEqual
{
    [TestMethod]
    [ExpectedException(typeof(ArgumentException))]
    public void CheckTriangle_A_Plus_B_Equals_C()
    {
        Triangle tr = new Triangle(1.0, 1.0, 2.0);

        var _ = tr.DetectTriangle();
    }

    [TestMethod]
    [ExpectedException(typeof(ArgumentException))]
    public void CheckTriangle_B_Plus_C_Equals_A()
    {
        Triangle tr = new Triangle(2.0, 1.0, 1.0);

        var _ = tr.DetectTriangle();
    }

    [TestMethod]
    [ExpectedException(typeof(ArgumentException))]
    public void CheckTriangle_C_Plus_A_Equals_B()
    {
        Triangle tr = new Triangle(1.0, 2.0, 1.0);

        var _ = tr.DetectTriangle();
    }


    [TestMethod]
    [ExpectedException(typeof(ArgumentException))]
    public void DetectTriangle_PositiveInfinityAandB()
    {
        Triangle tr = new Triangle(double.PositiveInfinity, double.PositiveInfinity, 14.0);

        var _ = tr.DetectTriangle();
    }

    [TestMethod]
    [ExpectedException(typeof(ArgumentException))]
    public void DetectTriangle_PositiveInfinityBandC()
    {
        Triangle tr = new Triangle(15.0, double.PositiveInfinity, double.PositiveInfinity);

        var _ = tr.DetectTriangle();
    }

    [TestMethod]
    [ExpectedException(typeof(ArgumentException))]
    public void DetectTriangle_PositiveInfinityCandA()
    {
        Triangle tr = new Triangle(double.PositiveInfinity, 12.0, double.PositiveInfinity);

        var _ = tr.DetectTriangle();
    }

    [TestMethod]
    [ExpectedException(typeof(ArgumentException))]
    public void DetectTriangle_PositiveInfinityAll()
    {
        Triangle tr = new Triangle(double.PositiveInfinity, double.PositiveInfinity, double.PositiveInfinity);

        var _ = tr.DetectTriangle();
    }


    [TestMethod]
    [ExpectedException(typeof(ArgumentException))]
    public void CheckTriangle_NegativeInfinityAandB()
    {
        Triangle tr = new Triangle(double.NegativeInfinity, double.NegativeInfinity, 14.0);

        var _ = tr.DetectTriangle();
    }

    [TestMethod]
    [ExpectedException(typeof(ArgumentException))]
    public void CheckTriangle_NegativeInfinityBandC()
    {
        Triangle tr = new Triangle(15.0, double.NegativeInfinity, double.NegativeInfinity);

        var _ = tr.DetectTriangle();
    }

    [TestMethod]
    [ExpectedException(typeof(ArgumentException))]
    public void CheckTriangle_NegativeInfinityCandA()
    {
        Triangle tr = new Triangle(double.NegativeInfinity, 12.0, double.NegativeInfinity);

        var _ = tr.DetectTriangle();
    }

    [TestMethod]
    [ExpectedException(typeof(ArgumentException))]
    public void CheckTriangle_NegativeInfinityAll()
    {
        Triangle tr = new Triangle(double.NegativeInfinity, double.NegativeInfinity, double.NegativeInfinity);

        var _ = tr.DetectTriangle();
    }
}
