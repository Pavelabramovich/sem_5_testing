using triangle;


namespace Tests.TestCheckTriangle;


[TestClass]
public class Triangle_CheckTriangle_Normal
{
    [TestMethod]
    public void CheckTriangle_OrdynaryAcute()
    {
        Triangle tr = new Triangle(15.0, 12.0, 14.0);

        Assert.IsTrue(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_IsoscelesAcute()
    {
        Triangle tr = new Triangle(6.0, 3.1, 6.0);

        Assert.IsTrue(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_OrdynaryRight()
    {
        Triangle tr = new Triangle(3.0, 4.0, 5.0);

        Assert.IsTrue(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_IsoscelesRight()
    {
        Triangle tr = new Triangle(1.0, 1.0, Math.Sqrt(2.0));

        Assert.IsTrue(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_OrdynaryObtuse()
    {
        Triangle tr = new Triangle(1.4, 3.0, 4.0);

        Assert.IsTrue(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_IsoscelesObtuse()
    {
        Triangle tr = new Triangle(2.1, 2.1, 4.0);

        Assert.IsTrue(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_Equilateral()
    {
        Triangle tr = new Triangle(1.0, 1.0, 1.0);

        Assert.IsTrue(tr.CheckTriangle());
    }
}


[TestClass]
public class Triangle_CheckTriangle_ZeroSides
{
    [TestMethod]
    public void CheckTriangle_ZeroA()
    {
        Triangle tr = new Triangle(0.0, 12.0, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_ZeroB()
    {
        Triangle tr = new Triangle(15.0, 0.0, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_ZeroC()
    {
        Triangle tr = new Triangle(15.0, 12.0, 0.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_ZeroAandB()
    {
        Triangle tr = new Triangle(0.0, 0.0, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_ZeroBandC()
    {
        Triangle tr = new Triangle(15.0, 0.0, 0.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_ZeroCandA()
    {
        Triangle tr = new Triangle(0.0, 12.0, 0.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_ZeroAll()
    {
        Triangle tr = new Triangle(0.0, 0.0, 0.0);

        Assert.IsFalse(tr.CheckTriangle());
    }


    [TestMethod]
    public void CheckTriangle_NegativeZeroA()
    {
        Triangle tr = new Triangle(-0.0, 12.0, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeZeroB()
    {
        Triangle tr = new Triangle(15.0, -0.0, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeZeroC()
    {
        Triangle tr = new Triangle(15.0, 12.0, -0.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeZeroAandB()
    {
        Triangle tr = new Triangle(-0.0, -0.0, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeZeroBandC()
    {
        Triangle tr = new Triangle(15.0, -0.0, -0.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeZeroCandA()
    {
        Triangle tr = new Triangle(-0.0, 12.0, -0.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeZeroAll()
    {
        Triangle tr = new Triangle(-0.0, -0.0, -0.0);

        Assert.IsFalse(tr.CheckTriangle());
    }
}


[TestClass]
public class Triangle_CheckTriangle_NegativeSides
{
    [TestMethod]
    public void CheckTriangle_NegativeA()
    {
        Triangle tr = new Triangle(-15.0, 12.0, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeB()
    {
        Triangle tr = new Triangle(15.0, -12.0, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeC()
    {
        Triangle tr = new Triangle(15.0, 12.0, -14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeAandB()
    {
        Triangle tr = new Triangle(-15.0, -12.0, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeBandC()
    {
        Triangle tr = new Triangle(15.0, -12.0, -14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeCandA()
    {
        Triangle tr = new Triangle(-15.0, 12.0, -14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeAll()
    {
        Triangle tr = new Triangle(-15.0, -12.0, -14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }
}


[TestClass]
public class Triangle_CheckTriangle_NanSides
{
    [TestMethod]
    public void CheckTriangle_NanA()
    {
        Triangle tr = new Triangle(double.NaN, 12.0, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NanB()
    {
        Triangle tr = new Triangle(15.0, double.NaN, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NanC()
    {
        Triangle tr = new Triangle(15.0, 12.0, double.NaN);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NanAandB()
    {
        Triangle tr = new Triangle(double.NaN, double.NaN, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NanBandC()
    {
        Triangle tr = new Triangle(15.0, double.NaN, double.NaN);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NanCandA()
    {
        Triangle tr = new Triangle(double.NaN, 12.0, double.NaN);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NanAll()
    {
        Triangle tr = new Triangle(double.NaN, double.NaN, double.NaN);

        Assert.IsFalse(tr.CheckTriangle());
    }
}


[TestClass]
public class Triangle_CheckTriangle_InfinitySides
{
    [TestMethod]
    public void CheckTriangle_PositiveInfinityA()
    {
        Triangle tr = new Triangle(double.PositiveInfinity, 12.0, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_PositiveInfinityB()
    {
        Triangle tr = new Triangle(15.0, double.PositiveInfinity, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_PositiveInfinityC()
    {
        Triangle tr = new Triangle(15.0, 12.0, double.PositiveInfinity);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_PositiveInfinityAandB()
    {
        Triangle tr = new Triangle(double.PositiveInfinity, double.PositiveInfinity, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_PositiveInfinityBandC()
    {
        Triangle tr = new Triangle(15.0, double.PositiveInfinity, double.PositiveInfinity);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_PositiveInfinityCandA()
    {
        Triangle tr = new Triangle(double.PositiveInfinity, 12.0, double.PositiveInfinity);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_PositiveInfinityAll()
    {
        Triangle tr = new Triangle(double.PositiveInfinity, double.PositiveInfinity, double.PositiveInfinity);

        Assert.IsFalse(tr.CheckTriangle());
    }


    [TestMethod]
    public void CheckTriangle_NegativeInfinityA()
    {
        Triangle tr = new Triangle(double.NegativeInfinity, 12.0, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeInfinityB()
    {
        Triangle tr = new Triangle(15.0, double.NegativeInfinity, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeInfinityC()
    {
        Triangle tr = new Triangle(15.0, 12.0, double.NegativeInfinity);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeInfinityAandB()
    {
        Triangle tr = new Triangle(double.NegativeInfinity, double.NegativeInfinity, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeInfinityBandC()
    {
        Triangle tr = new Triangle(15.0, double.NegativeInfinity, double.NegativeInfinity);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeInfinityCandA()
    {
        Triangle tr = new Triangle(double.NegativeInfinity, 12.0, double.NegativeInfinity);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_NegativeInfinityAll()
    {
        Triangle tr = new Triangle(double.NegativeInfinity, double.NegativeInfinity, double.NegativeInfinity);

        Assert.IsFalse(tr.CheckTriangle());
    }


    [TestMethod]
    public void CheckTriangle_PositiveInfinityA_NegativeInfinityB()
    {
        Triangle tr = new Triangle(double.PositiveInfinity, double.NegativeInfinity, 14.0);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_PositiveInfinityB_NegativeInfinityC()
    {
        Triangle tr = new Triangle(15.0, double.PositiveInfinity, double.NegativeInfinity);

        Assert.IsFalse(tr.CheckTriangle());
    }

    [TestMethod]
    public void CheckTriangle_PositiveInfinityC_NegativeInfinityA()
    {
        Triangle tr = new Triangle(double.PositiveInfinity, 12.0, double.NegativeInfinity);

        Assert.IsFalse(tr.CheckTriangle());
    }
}




