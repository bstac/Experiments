/**
 * RGB Cube.
 * 
 * The three primary colors of the additive color model are red, green, and blue.
 * This RGB color cube displays smooth transitions between these colors. 
 */

int xize = 200; 
float xmag, ymag = 0;
float newXmag, newYmag = 0; 
float rx = 0;
float ry =0;
 
void setup()  { 
  size(xize, xize, P3D); 
  
 stroke(180,200,0);
  

} 
 
void draw()  
{
  background(0);
  float cameraY = height/2.0;
  float fov = mouseX/float(width) * PI/2;
  float cameraZ = cameraY / tan(fov / 2.0);
  float aspect = float(width)/float(height);
  if (mousePressed) {
    aspect = aspect / 2.0;
  }
  perspective(fov, aspect, cameraZ/10.0, cameraZ*10.0);
  function();
} 

void function()
{
  for(int t=0; t<xize; t++)
  {
    translate(t*t, t/5.0, -t);
    sphere(10);
  }
}
