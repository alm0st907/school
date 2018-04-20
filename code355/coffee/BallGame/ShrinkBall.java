import java.awt.Color;
public class ShrinkBall extends BasicBall
{
    private double init_rad;
    public ShrinkBall(double r, Color c)
    {
        super(r,c);//fixes inheritance error
        init_rad = r;
    }

    public boolean isHit(double x, double y) 
    {
 
        if ((Math.abs(rx-x)<=radius) && (Math.abs(ry-y)<=radius))
        {
            if(radius<(init_rad/3))
            {
                radius = init_rad;
                return true;
            }
            this.radius = radius*.66;
			return true;
        }
        else return false; 
    }
    public int getScore() {
    	return 20;
    }
}

