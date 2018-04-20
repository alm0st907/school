import java.awt.Color;
public class ShrinkBall extends BasicBall
{
    public ShrinkBall(double r, Color c)
    {
        super(r,c);//fixes inheritance error
    }

    public boolean isHit(double x, double y) 
    {
        if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius))
        {
            this.radius = radius*.66;
			return true;
        }
        else return false; 
    }
}

