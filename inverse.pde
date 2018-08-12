//import processing.core.PApplet;
import ddf.minim.*;
import ddf.minim.analysis.*;

private FFT fft;
private FFT fft2;
private AudioInput input;
private AudioOutput output;
private Minim minim;

private int SAMPLERATE = 44100;
private int BUFFERSIZE = 2048;

void setup() 
{
  size(300,200);
  minim = new Minim(this);
  fft = new FFT(BUFFERSIZE, SAMPLERATE); //fft.window(FFT.HAMMING);
  input = minim.getLineIn(Minim.MONO, BUFFERSIZE, SAMPLERATE);
  output = minim.getLineOut(Minim.MONO, BUFFERSIZE, SAMPLERATE);
  input.addListener(new Listener());
  output.addSignal(new MySignal());
  frameRate(1);
}

     
void draw()
{
 // background(random(100));
}
    
  
class Listener implements AudioListener 
{
  public void  samples(float[] sample){fft.forward(sample);}
  public void samples(float[] left, float[] right) {samples(left);}
}  
   
//private 
class MySignal implements AudioSignal
{
  public void generate(float[] out) 
  {//only use real part of the FFT. no time information i think.
    fft2 = new FFT(BUFFERSIZE, SAMPLERATE);
    // out = new float[BUFFERSIZE];
    int u=1;//method 1//FFT imaginary part used to reconstruct time info i think.
    if(u==1){fft.inverse(out);}
    else
    {
      fft2.window(FFT.HAMMING);
      //println(BUFFERSIZE);
      for(int i=0;i<BUFFERSIZE/2;i++){fft2.setBand(i, fft.getBand(i));}                
      fft2.inverse(out);
    }
    //for(int i=0;i<out.length;i++){out[i]=out[i];}
  }
  //if stereo
  public void generate(float[] left, float[] right) {generate(right);}
}
