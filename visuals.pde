//http://bill.kutztown.edu/~parson/javadoc/parsonswe/
// send email to dr. parson for the other link
// 5 speakers, write down elsewhere.
/*
IDEAs:

1)whale swimming, 3d sound follows its movement
(from SC), reverb increases as it gets further away,
and the sound widens and quiets. use an instrument to control.

2)objects that are instruments, and are transformed by
sound (feedback, maybe done in a way that starts with a big bang) 
each object is an agent for musical synthesis with SC.

3) use SC for crazy computational randomized songs,
and just have visuals follow the sound. try non equal temperment
and patterns. additive vs subtracive synthesis. midi music with
patterns. also, try finishing some songs, and recording more
with ableton, and then having visuals for them. 
*/

Obj bob, jeff, carl;
int count = 0;
float[][] cuboid = new float[8][3];
float g = 0; //parameterize variable

void setup()
{
  
  size(600,600);
  background(0);
  ellipseMode(CENTER);
  stroke(0,60,230,40);
  fill(0,40,200,25);
  //create cube
  //verified to work
int ct = -1, cnt = -1;
count = -1;
for(int i = 7; i >= 0; i--)
{
  cuboid[i][0] = count;
  cuboid[i][1] = cnt;
  cuboid[i][2] = ct;
  ct *= -1;
  if(i%2 == 0)
  {
    cnt *= -1;
    if(i%4 == 0)
    {
      count *= -1;
    }
  }
}
 bob = new Obj(cuboid, 0, 0, 0);
 jeff = new Obj(cuboid, 0, 0, 3);
 carl = new Obj(cuboid, 0, 0, .3);
 count = 0;
}

void draw()
{
  
  g += PI/256;
  if(g >= 2*PI)
  {
    g = 0;
  }
  
  if(true) //count%512 == 0)
  {
  background(1);
  count = 0;
  }
  
  stroke(0,60,230);
  //stroke(0,60,230,5);
  fill(0,40,200,4);
  
  bob.rot = g;
  bob.x = sin(g);
  bob.y = cos(g);
  bob.z = g+1;
  bob.display();
  
  stroke(240,4,230);
  //stroke(240,4,230,5);
  fill(200,40,3,4);
  
  jeff.rut = g/2;
  jeff.x = -sin(g);
  jeff.y = cos(g);
  jeff.z = 3 - g;
  jeff.display();
  
  stroke(100,200,0,5);
  fill(150,200,0);
  
  carl.rot = g/6;
  carl.rut = g/4;
  carl.display();
  
  count++;
}
