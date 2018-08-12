/**
  * An FFT object is used to convert an audio signal into its frequency domain representation. 
  * For more information about Minim and additional features, visit http://code.compartmental.net/minim/
  */

import ddf.minim.analysis.*;
import ddf.minim.*;
import ddf.minim.ugens.*;

     private FFT fft1;
     private FFT fft2;

float SAMPLERATE = 44100;
float BUFFERSIZE = 512;

Minim minim;  
AudioPlayer jingle;
Listener ears;
MySignal sign;
FFT fft;
FFT fftLog;
AudioOutput   out;
AudioRecorder recorder;
AudioSample sample;
AudioMetaData format;
PrintWriter output;
float height3;
float height23;
float spectrumScale = 4;
float[] left;
PFont font;

void setup()
{
  size(512, 480);
  height3 = height/3;
  height23 = 2*height/3;
  

  
  // "jingle.mp3"
  minim = new Minim(this);
  jingle = minim.loadFile("DrMcDreamy.wav", 1024);
  ears = new Listener();
  sign = new MySignal();
  // loop the file
  jingle.loop();
  format = jingle.getMetaData();
  out = minim.getLineOut();
  // create a recorder that will record from the output to the filename specified
  // the file will be located in the sketch's root folder.
  recorder = minim.createRecorder(sample, "myrecording.wav");
  // create an FFT object that has a time-domain buffer the same size as jingle's sample buffer
  // note that this needs to be a power of two 
  // and that it means the size of the spectrum will be 1024. 
  // see the online tutorial for more info.
  SAMPLERATE = jingle.sampleRate();
  BUFFERSIZE = jingle.bufferSize();
  fft = new FFT( jingle.bufferSize(), jingle.sampleRate() );
  left = new float[fft.specSize()];
  rectMode(CORNERS);
  font = loadFont("ArialMT-12.vlw");
}

void draw()
{
  background(0);
  
  textFont(font);
  textSize( 18 );
 
  float centerFrequency = 0;
  
  // perform a forward FFT on the samples in jingle's mix buffer
  // note that if jingle were a MONO file, this would be the same as using jingle.left or jingle.right
  fft.forward( jingle.mix );
  //fftLog.forward( jingle.mix );
    // draw the full spectrum
    noFill();
    for(int i = 0; i < fft.specSize()-10; i++)
    {
         left[i] = fft.indexToFreq(i+10);
         //left[i+1] = fft.indexToFreq(i+1);
    }
   //fft.inverse(left);
   //sample = minim.createSample(left,jingle.getFormat());
   sign.generate(left);
    if ( recorder.isRecording() )
  {
    text("Currently recording...", 5, 15);
  }
  else
  {
    text("Not recording.", 5, 15);
  }
  //sample.patch(out);
}








void keyReleased()
{
  if ( key == 'r' ) 
  {
    // to indicate that you want to start or stop capturing audio data, you must call
    // beginRecord() and endRecord() on the AudioRecorder object. You can start and stop
    // as many times as you like, the audio data will be appended to the end of the buffer 
    // (in the case of buffered recording) or to the end of the file (in the case of streamed recording). 
    if ( recorder.isRecording() ) 
    {
      recorder.endRecord();
    }
    else 
    {
      recorder.beginRecord();
    }
  }
  if ( key == 's' )
  {
    // we've filled the file out buffer, 
    // now write it to the file we specified in createRecorder
    // in the case of buffered recording, if the buffer is large, 
    // this will appear to freeze the sketch for sometime
    // in the case of streamed recording, 
    // it will not freeze as the data is already in the file and all that is being done
    // is closing the file.
    // the method returns the recorded audio as an AudioRecording, 
    // see the example  AudioRecorder >> RecordAndPlayback for more about that
    recorder.save();
    println("Done saving.");
  }
}


///////////////////////////////////////////////////////////////////////////////
//*************************Class DEFS******************************************
///////////////////////////////////////////////////////////////////////////////

     class Listener implements AudioListener {
           public void  samples(float[] sample){
             fft.forward(sample);
           }
           public void samples(float[] left, float[] right) {
             samples(left);
           }
     }
     
     
     
     
     
     
     
     
     
     
private class MySignal implements AudioSignal{
  public void generate(float[] out) {

      fft2 = new FFT(BUFFERSIZE, SAMPLERATE);

              // out = new float[BUFFERSIZE];
               int u=2;
               if(u==1){//method 1 
                     //FFT imaginary part used to reconstruct time info i think.
                     fft1.inverse(out);
               }else{
                     //only use real part of the FFT. no time information i think.
                   fft2.window(FFT.HAMMING);
                   for(int i=0;i<BUFFERSIZE/2;i++){
                     fft2.setBand(i, fft.getBand(i));
                   }                
                   fft2.inverse(out);
               }
                                       
               for(int i=0;i<out.length;i++){
                     out[i]=out[i];
               }
             }

           public void generate(float[] left, float[] right) {
               generate(right);
           }
     }
