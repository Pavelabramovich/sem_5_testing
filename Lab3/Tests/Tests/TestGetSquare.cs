using triangle;


namespace Tests.TestGetSquare;

[TestClass]
public class Triangle_GetSquare_Normal
{
    [TestMethod]
    public void GetSquare_OrdynaryAcute()
    {
        Triangle tr = new Triangle(15.0, 12.0, 14.0);

        double p = (15.0 + 12.0 + 14.0) / 2;
        double expectedRes = Math.Sqrt(p * (p - 15.0) * (p - 12.0) * (p - 14.0));
        double res = tr.GetSquare();

        Assert.AreEqual(expectedRes, res);
    }

    [TestMethod]
    public void GetSquare_IsoscelesAcute()
    {
        Triangle tr = new Triangle(6.0, 3.1, 6.0);

        double p = (6.0 + 3.1 + 6.0) / 2;
        double expectedRes = Math.Sqrt(p * (p - 6.0) * (p - 3.1) * (p - 6.0));
        double res = tr.GetSquare();

        Assert.AreEqual(expectedRes, res);
    }

    [TestMethod]
    public void GetSquare_OrdynaryRight()
    {
        Triangle tr = new Triangle(3.0, 4.0, 5.0);

        double expectedRes = 6.0;
        double res = tr.GetSquare();

        Assert.AreEqual(expectedRes, res);
    }

    [TestMethod]
    public void GetSquare_IsoscelesRight()
    {
        Triangle tr = new Triangle(1.0, 1.0, Math.Sqrt(2.0));

        double expectedRes = 0.5;
        double res = tr.GetSquare();

        Assert.AreEqual(expectedRes, res);
    }

    [TestMethod]
    public void GetSquare_OrdynaryObtuse()
    {
        Triangle tr = new Triangle(1.4, 3.0, 4.0);

        double p = (1.4 + 3.0 + 4.0) / 2;
        double expectedRes = Math.Sqrt(p * (p - 1.4) * (p - 3.0) * (p - 4.0));
        double res = tr.GetSquare();

        Assert.AreEqual(expectedRes, res);
    }

    [TestMethod]
    public void GetSquare_IsoscelesObtuse()
    {
        Triangle tr = new Triangle(2.1, 2.1, 4.0);

        double p = (2.1 + 2.1 + 4.0) / 2;
        double expectedRes = Math.Sqrt(p * (p - 2.1) * (p - 2.1) * (p - 4.0));
        double res = tr.GetSquare();

        Assert.AreEqual(expectedRes, res);
    }

    [TestMethod]
    public void GetSquare_Equilateral()
    {
        Triangle tr = new Triangle(1.0, 1.0, 1.0);

        double expectedRes = 1.0 * Math.Sqrt(3.0) / 4.0;
        double res = tr.GetSquare();

        Assert.AreEqual(expectedRes, res);
    }
}