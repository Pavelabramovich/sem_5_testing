using triangle;


namespace Tests.TestCheckTriangle;

[TestClass]
public class UnitTest1
{
    [TestMethod]
    public void TestMethod1()
    {
        Triangle tr = new Triangle(3, 4, 5);

        Assert.AreEqual(tr.GetSquare(), 6);
    }
}