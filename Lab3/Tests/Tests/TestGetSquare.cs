using triangle;


namespace Tests.TestGetSquare;

[TestClass]
public class TestGetSquare
{
    [TestMethod]
    public void TestMethod1()
    {
        Triangle tr = new Triangle(3, 4, 5);

        Assert.AreEqual(tr.GetSquare(), 6);
    }
}