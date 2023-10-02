namespace Tests.TestDetectTriangle;

[TestClass]
public class UnitTest1
{
    [TestMethod]
    public void TestMethod1()
    {
        Assert.IsFalse(1 != 1);
    }

    [TestMethod]
    public void TestMethod2()
    {
        Assert.IsFalse(1 != 2);
    }

    [TestMethod]
    public void TestMethod3()
    {
        throw new InvalidCastException();

        Assert.IsFalse(1 != 1);
    }
}