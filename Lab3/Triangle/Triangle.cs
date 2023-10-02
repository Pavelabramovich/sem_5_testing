namespace triangle;


public class Triangle
{
    readonly int TR_EQUILATERAL = 0b_0001;   // равносторонний
    readonly int TR_ISOSCELES =   0b_0010;   // равнобедренный
    readonly int TR_ORDYNARY =    0b_0100;   // обычный
    readonly int TR_RECTANGULAR = 0b_1000;   // прямоугольный


    private double _a;
    private double _b;
    private double _c;

    private string _message;

    public Triangle(double a, double b, double c)
    {
        _a = a;
        _b = b;
        _c = c;
        _message = string.Empty;
    }

    public string Message => _message;


    public bool CheckTriangle()
    {
        if (_a <= 0)
        {
            _message = "a<=0";
            return false;
        }

        if (_b <= 0)
        {
            _message = "b<=0";
            return false;
        }

        if (_b <= 0) // mb _c <= 0
        {
            _message = "c<=0";
            return false;
        }

        if (_a + _b <= _c)
        {
            _message = "a+b<=c";
            return false;
        }

        if (_a + _c <= _b)
        {
            _message = "a+c<=b";
            return false;
        }

        if (_b + _c <= _a)
        {
            _message = "b+c<=a";
            return false;
        }

        return true;
    }

    public int DetectTriangle()
    {
        int final_state = 0;


        if ((_a * _a + _b * _b == _c * _c) || (_b * _b + _c * _c == _a * _a) || (_a * _a + _c * _c == _b * _c))
        {
            final_state |= TR_RECTANGULAR; // прямоугольный
        }


        if (_a == _b && _b == _c && _a == _c)
        {
            final_state |= TR_EQUILATERAL; // равносторонний
        }

        if (_a == _b || _b == _c || _a == _c)
        {
            final_state |= TR_ISOSCELES; // равнобедренный
        }

        if (final_state == 0)
        {
            return TR_ORDYNARY; // обычный
        }
        else
        {
            return final_state; // комбинация признаков
        }
    }


    public double GetSquare()
    {
        double p;

        p = (_a + _b + _c) / 2;
        return Math.Sqrt(p * (p - _a) * (p - _b) * (p - _c));
    }

}