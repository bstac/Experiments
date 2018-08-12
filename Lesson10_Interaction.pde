import beads.*;
import java.util.Arrays;

AudioContext ac;
Glide carrierFreq, modFreqRatio, modFreqRatio2;
float scale;
boolean check = false;
float exx, wyy;
boolean turnOn = true;
float count = .05;
void setup() {
  exx = 0;
  wyy = 0;
  size(300,300);
  ac = new AudioContext();
  scale = 1;
  /*
   * This is a copy of Lesson 3 with some mouse control.
   */
   //this time we use the Glide object because it smooths the mouse input.
  carrierFreq = new Glide(ac, 500);
  modFreqRatio = new Glide(ac, 1);
  modFreqRatio2 = new Glide(ac, 1);
  Function modFreq = new Function(carrierFreq, modFreqRatio, modFreqRatio2) {
    public float calculate() {
      return x[0] * x[1] * x[2];
    }
  };
  WavePlayer freqModulator = new WavePlayer(ac, modFreq, Buffer.SINE);
  Function carrierMod = new Function(freqModulator, carrierFreq) {
    public float calculate() {
      return x[0] * 400.0 + x[1];    
    }
  };
  WavePlayer wp = new WavePlayer(ac, carrierMod, Buffer.SINE);
  Gain g = new Gain(ac, 1, 0.1);
  g.addInput(wp);
  ac.out.addInput(g);
  ac.start();
}

/*
 * The drawing code also has some mouse listening code now.
 */
color fore = color(255, 102, 204);
color back = color(0,0,0);

/*
 * Just do the work straight into Processing's draw() method.
 */
void draw() {
  loadPixels();
  //set the background
  Arrays.fill(pixels, back);
  //scan across the pixels
  for(int i = 0; i < width; i++) {
    //for each pixel work out where in the current audio buffer we are
    int buffIndex = i * ac.getBufferSize() / width;
    //then work out the pixel height of the audio data at that point
    int vOffset = (int)((1 + ac.out.getValue(0, buffIndex)) * height / 2);
    //draw into Processing's convenient 1-D array of pixels
    pixels[vOffset * height + i] = fore;
  }
  updatePixels();
  //mouse listening code here
  if(turnOn)
  {
    exx = mouseX;
    wyy = mouseY;
  }
  modFreqRatio.setValue((1 - (float)exx / height) * 8 + 0.1);
  modFreqRatio2.setValue((1 - (float)wyy / width) * 2 + 0.1);
  
  if(keyPressed)
  {
    check = false;
     if(key == ' ')
     {
      check = true;
     }//stop
     if(key == '\n')
     {
      check = false;
     }//start
    if(key == '`'){scale = .21;}//scaler low low low LOW LOW
    if(key == '0'){scale = 4;}//scaler painfully high
    if(key == '1'){scale = .25;}//scaler low low low
    if(key == '2'){scale = .5;}//scaler
    if(key == '3'){scale = 1;}//scaler
    if(key == '4'){scale = 1.25;}//scaler
    if(key == '5'){scale = 1.3333;}//scaler 
    if(key == '6'){scale = 1.4062;}//scaler wierd
    if(key == '7'){scale = 1.5;}//scaler  wierd
    if(key == '8'){scale = 1.8;}//scaler  wierd
    if(key == '9'){scale = 2;}//scaler  wierd
    //now for the notes, full keyboard one octave, white notes for octive below
    if(key == 'z'){carrierFreq.setValue(220.0*scale);}//A low(sub3...wubwubwubw)
    if(key == 'x'){carrierFreq.setValue(246.94*scale);}//b low
    if(key == 'c'){carrierFreq.setValue(261.63*scale);}//c low
    if(key == 'v'){carrierFreq.setValue(293.66*scale);}//d low
    if(key == 'b'){carrierFreq.setValue(329.63*scale);}//e low
    if(key == 'n'){carrierFreq.setValue(349.23*scale);}//f low
    if(key == 'm'){carrierFreq.setValue(392.0*scale);}//g low
    if(key == 'a'){carrierFreq.setValue(440.0*scale);}//A   sub4
    if(key == 'w'){carrierFreq.setValue(466.16*scale);}//Asharp
    if(key == 's'){carrierFreq.setValue(493.88*scale);}//B
    if(key == 'd'){carrierFreq.setValue(523.25*scale);}//C     sub 5
    if(key == 'r'){carrierFreq.setValue(554.37*scale);}//C#
    if(key == 'f'){carrierFreq.setValue(587.33*scale);}//D
    if(key == 't'){carrierFreq.setValue(622.25*scale);}//D#
    if(key == 'g'){carrierFreq.setValue(659.26*scale);}//E
    if(key == 'h'){carrierFreq.setValue(698.46*scale);}//F
    if(key == 'u'){carrierFreq.setValue(740.0*scale);}//f#
    if(key == 'j'){carrierFreq.setValue(784.0*scale);}//g
    if(key == 'i'){carrierFreq.setValue(830.61*scale);}//g#
    if(key == 'k'){carrierFreq.setValue(880.0*scale);}//A
    if(key == 'o'){carrierFreq.setValue(932.33*scale);}//A#
    if(key == 'l'){carrierFreq.setValue(987.77*scale);}//b
    if(key == '='){count /= .9;}//fade faster
    if(key == '-'){count *= .9;}//fade slower
    if(key == ','){count = .01;}//fade, slow
    if(key == '.'){count = .05;}//fade norm, start
    if(key == '/'){count = .1;}//fade fast
    if(key == '='){println("Mouse: " +mouseX +" , "+mouseY);}
    if(key == '['){println("Chappelle");
                   exx=275;
                   wyy=117;
                   turnOn=false;
                  }
    if(key == ']'){println("Greenwood");
                   exx=279;
                   wyy=89;
                   turnOn=false;
                  }
    if(key == ';'){println("Frederick Harryhausen");
                   exx=126;
                   wyy=252;
                   turnOn=false;
                  }
    if(key == '\\'){println("Mouse control");
                   turnOn=!turnOn;
                  }                  
  }
  
  if(check)
  {
    float x = ac.out.getGain();
    if(x > 0)
    {
      ac.out.setGain(x - count);
    }
    else
    {
      ac.out.setGain(0);
    }
  }
  else
  {
    float x = ac.out.getGain();
    if(x < 1)
    {
      ac.out.setGain(x + count);
    }
    else
    {
      ac.out.setGain(1);
    }
  }
}
