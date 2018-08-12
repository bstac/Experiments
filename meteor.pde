//program for 3d dome objects
//currently work with the path set to a helix
//
float x,y,z,r,t,u,ex,wy;
int count;
float theta,gamma;
float g = .01;
float rot = 0;
float rat = 0;
float[] Xray = new float[8];
float[] Yray = new float[8];
float[] Zray = new float[8];

/*
//----------------
Xray[0] = .1;
Yray[0] = .1;
Zray[0] = .1;
//----------------
Xray[1] = -.1;
Yray[1] = .1;
Zray[1] = .1;
//----------------
Xray[2] = .1;
Yray[2] = -.1;
Zray[2] = .1;
//----------------
Xray[3] = .1;
Yray[3] = .1;
Zray[3] = -.1;
//----------------
Xray[4] = -.1;
Yray[4] = -.1;
Zray[4] = .1;
//----------------
Xray[5] = -.1;
Yray[5] = .1;
Zray[5] = -.1;
//----------------
Xray[6] = .1;
Yray[6] = -.1;
Zray[6] = -.1;
//----------------
Xray[7] = -.1;
Yray[7] = -.1;
Zray[7] = -.1;
//----------------
*/


void setup() 
{
  size(600,600);
  x = 0;
  y = 1;
  z = 1;
  ellipseMode(CENTER);
  count = 0;
  theta = 0;
  gamma = 0;
}




void draw() 
{
  if(count == 4)
  {
    //changeCube();
    change();
    toSphere();
    toTwoDim();
    count = 0;
  //System.out.println("x,y,z");
  //System.out.println("" + x +"   "+ y + "   "+z);
  //System.out.println("t, u, r");
  //System.out.println("" + t +"   "+ u +"   "+ r);
  //System.out.println("ex and wy");
  //System.out.println("" + ex + "   "+ wy);
  }
  else
  {
    count++;
  }
  background(0);
  ellipse(ex + width/2 ,wy+height/2 ,r,r); 
  //drawCube();
}


void toSphere()
{
  r = (x*x) + (y*y) + (z*z);
  r = sqrt(r);
  if(r < 1)
  {
    r = 16;
  }
  t = acos(z/r);
  u = atan(y/x);
  r *= 3;
  if(x<0){u = (PI)+u;}
}

void toTwoDim()
{
  ex = ((PI/2) - t)*cos(u)*width/(PI);
  wy = ((PI/2) - t)*sin(u)*height/(PI);
}

void change()
{
  g+= PI/64;
  if(g>4*PI){
    g = 0.01;
  }
  /*rot += .04;
  rat += .05;
  if(rat > 7){ rot = 0; rat = 0;}*/
  
  x = sin(g);
  y = cos(g);
  z = g;
  
}



/*void changeCube()
//{
//  change();
  for( int i = 0; i < 8; i++)
  {
    toSphere();
    toTwoDim();
  }
}*/


//void drawCube()
//{
  
//}
